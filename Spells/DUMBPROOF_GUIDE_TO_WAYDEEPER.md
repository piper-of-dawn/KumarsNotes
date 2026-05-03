# Dumbproof Guide to Waydeeper

## TL;DR

Waydeeper takes a flat wallpaper image and makes it react to your mouse in 3D — like a parallax effect. It does this by guessing the depth of every pixel using an AI model, then shifting near and far things by different amounts as your cursor moves.

---

## Component Breakdown

Each source file is one self-contained job.

### `main.rs`
Entry point. Does nothing except boot the logger and hand off to `cli`.

---

### `cli.rs`
Parses every command you type (`waydeeper run`, `waydeeper reload`, `waydeeper stop`, etc.) and routes it to the right function. It is the only thing that talks to the user directly via terminal output.

---

### `config.rs`
Reads and writes `~/.config/waydeeper/config.json`. Stores per-monitor settings: wallpaper path, parallax strength, FPS, animation speed, idle timeout, which AI model to use. Also defines where caches and models live on disk.

---

### `models.rs`
A registry of downloadable AI depth models (Depth Anything V3, MiDaS Small, Depth Pro). Knows their URLs, file formats, and where to save them. Also handles finding the right `.onnx` file on disk when the user hasn't specified one.

---

### `depth_estimator.rs`
Loads an ONNX depth model and runs it on a wallpaper image. Takes a flat RGB photo → outputs a grayscale depth map where **white = close, black = far**. Handles different model input layouts (channels-first, channels-last, 5D tensors). Post-processes output: normalizes values, resizes back to original resolution, applies a light blur to smooth edges.

---

### `cache.rs`
Avoids re-running the AI every time. Hashes the image file + model name → stores the depth map as a PNG in `~/.cache/waydeeper/`. On next run, checks the hash first and returns the cached result if it exists. Also handles the same caching logic for inpaint PLY meshes.

---

### `inpaint.rs`
Launches `inpaint.py` (a Python script) as a subprocess. That script takes the image + depth map and builds a real 3D mesh (a `.ply` file) by "painting in" the gaps that appear behind objects when you shift the camera. This is the optional higher-quality mode — without it, parallax is done with a flat shader trick.

---

### `mesh.rs`
Reads the `.ply` 3D mesh file that `inpaint.py` produces. Parses its binary format into vertex positions, colors, UV texture coordinates, and triangle indices — ready to be uploaded to the GPU. Also reads metadata baked into the PLY header (field of view, image aspect ratio).

---

### `daemon.rs`
The long-running process that owns everything after launch. It:
1. Calls `depth_estimator` to generate (or load from cache) the depth map
2. Optionally calls `inpaint` to generate the 3D mesh
3. Starts the IPC socket (so other `waydeeper` commands can talk to it)
4. Hands off to `wayland` to start rendering

Also handles hot-reload: when you run `waydeeper reload`, the daemon swaps in a new wallpaper without restarting.

---

### `ipc.rs`
A Unix socket that lets CLI commands (`stop`, `reload`, `status`) talk to a running daemon. The daemon listens; CLI commands connect and send JSON messages. Commands: `PING`, `STATUS`, `STOP`, `RELOAD`.

---

### `wayland.rs`
Connects to the Wayland compositor. Creates a layer-shell surface (a surface that sits below all windows, acting as wallpaper). Listens for mouse movement events. Feeds mouse coordinates into the renderer every frame. Handles fractional scaling for HiDPI monitors.

---

### `renderer.rs`
The OpenGL (via `glow`) drawing code. Every frame it:
- Takes current mouse position
- Computes how much to shift the wallpaper based on depth (near pixels shift more, far pixels shift less)
- Draws either: a flat quad with a depth-shader parallax trick, or the full 3D inpaint mesh
- Handles smooth interpolation (the camera eases toward the cursor, not snapping to it)
- Goes idle when the mouse hasn't moved for `idle_timeout` milliseconds

---

### `egl_bridge.c`
A thin C shim. Rust can't directly call EGL (the OpenGL↔Wayland glue layer), so this file exposes the minimal EGL functions Rust needs: initialize EGL from a Wayland display, create a window surface, swap buffers, destroy context.

---

### `math.rs`
Two matrix functions used by the 3D renderer: a perspective projection matrix and a translation matrix. Nothing more.

---

## Synthesis — How They Connect

```
User types: waydeeper run wallpaper.jpg --monitor DP-1
         │
         ▼
      cli.rs          ← parses command
         │
         ▼
      daemon.rs       ← orchestrates everything
         │
         ├──▶ depth_estimator.rs  ← AI depth map
         │         │
         │         ▼
         │      cache.rs          ← save/load result
         │
         ├──▶ inpaint.rs          ← (optional) 3D mesh via Python
         │         │
         │         ▼
         │      cache.rs          ← save/load PLY
         │
         ├──▶ ipc.rs              ← start Unix socket
         │
         └──▶ wayland.rs          ← connect to compositor, start event loop
                   │
                   └──▶ renderer.rs  ← draw frame on mouse move
                              │
                              ├── math.rs        ← projection matrices
                              ├── mesh.rs        ← parse PLY if inpaint mode
                              └── egl_bridge.c   ← OpenGL surface via EGL
```

Config is read by `daemon.rs` and `cli.rs` at startup. `models.rs` is used by `cli.rs` (for `download-model`) and `depth_estimator.rs` (to find the model file).

---

## Core Intuition — Why It Works

A flat image has no depth. The trick: an AI model trained on millions of real photos can *guess* which parts of a scene are close and which are far — just from how things look (lighting, blur, occlusion, texture). That guess (the depth map) is good enough to drive a convincing parallax. Your eye fills in the rest.

The inpaint mode goes further: it builds an actual 3D surface and textures it with the original image. When you reveal the "behind" of an object by moving the camera, the gaps that appear are filled with plausible continuation — inpainted by the Python model. This is slower but more realistic.

---

## How the Math Works

### 1. Smooth cursor tracking

The mouse position isn't used directly. There is a "ghost cursor" that chases the real one. Every frame it closes a fraction of the remaining gap — never teleporting, always easing.

$$\alpha = 0.02 + s \times 0.28$$

- $s$ — `animation_speed` from config (0 to 1). How snappy the chase is.
- $\alpha$ — the fraction of the gap to close per 60 Hz frame. At $s=0$ it closes 2% per frame (slow, floaty). At $s=1$ it closes 30% (fast, snappy).

To make the speed the same at any FPS:

$$n = \Delta t \times 60$$

$$\lambda = 1 - (1 - \alpha)^{n}$$

- $\Delta t$ — seconds since the last frame. At 60 FPS this is ~0.016. At 30 FPS it is ~0.033.
- $n$ — how many 60 Hz frames worth of time elapsed this tick.
- $\lambda$ — the actual fraction to close this tick. The exponent compounds $\alpha$ over $n$ frames so the result is FPS-independent.

$$x_\text{current} \mathrel{+}= (x_\text{mouse} - x_\text{current}) \times \lambda$$
$$y_\text{current} \mathrel{+}= (y_\text{mouse} - y_\text{current}) \times \lambda$$

- $x_\text{mouse}, y_\text{mouse}$ — where the real cursor is right now (0 to 1).
- $x_\text{current}, y_\text{current}$ — where the ghost cursor is. This is what the renderer actually uses.

When the mouse leaves the screen, the target becomes $(0.5,\ 0.5)$ — the center — so the wallpaper floats back to rest.

---

### 2. Flat mode — per-pixel depth shift

This runs on the GPU once per pixel, every frame. Every pixel has two inputs: its color (wallpaper image) and its depth (AI depth map, where white = close = 1.0, black = far = 0.0).

**Mouse offset**

$$\vec{m} = \vec{p}_\text{mouse} - 0.5$$

- $\vec{p}_\text{mouse}$ — mouse position, each axis 0 (left/top) to 1 (right/bottom).
- $\vec{m}$ — how far the mouse is from the center of the screen, range $[-0.5,\ +0.5]$. Center = zero, meaning no parallax pull.

**Parallax amount**

$$a = 1 - d$$

- $d$ — depth value for this pixel from the AI map. Near = 1.0, far = 0.0.
- $a$ — how much this pixel should move. Near pixels get $a \approx 0$ (barely move). Far pixels get $a \approx 1$ (shift the most). This is why the foreground stays put while the background slides — like looking out a car window.

**UV offset**

$$\vec{o} = \vec{m} \times a \times \vec{k}$$

- $\vec{k}$ — `parallax_strength` from config, one value per axis. Scales the total shift up or down.
- $\vec{o}$ — the UV shift to apply to this pixel. A far pixel with the mouse at the far right gets the biggest shift; a near pixel gets nearly zero.

**Zoom**

$$z = 1 + \max(k_x,\ k_y) \times 2$$

- $z$ — zoom factor. Shifting pixels toward the image edges would expose empty space past the image boundary. Zooming in slightly ensures there is always real image content to show. Stronger parallax = more zoom.

**Scale (aspect ratio correction)**

$$\vec{u} = \begin{cases} \left(\dfrac{A_\text{screen}}{A_\text{image}},\ 1\right) & \text{if image is wider than screen} \\[6pt] \left(1,\ \dfrac{A_\text{image}}{A_\text{screen}}\right) & \text{otherwise} \end{cases} \quad \div\ z$$

- $A_\text{screen} = W/H$ — screen width divided by screen height (e.g. 1.78 for 16:9).
- $A_\text{image}$ — same ratio for the wallpaper image.
- $\vec{u}$ — the UV scale vector. Corrects for mismatched shapes so the image fills the screen without stretching, then divides by $z$ to apply the zoom.

**Final sample coordinate**

$$\vec{c} = (\vec{q} - 0.5) \times \vec{u} + 0.5 + \vec{o}$$

- $\vec{q}$ — the UV coordinate of this pixel (0 to 1 in each axis).
- Subtracting 0.5 centers UV around the image middle so scale is applied from the center outward.
- Adding 0.5 shifts it back to $[0,1]$ space, then $\vec{o}$ applies the parallax.
- The color is read from $\vec{c}$ in the wallpaper texture.

---

### 3. Mesh mode — moving a real 3D camera

In inpaint mode the scene is a real 3D triangle mesh. Parallax is done by physically moving a virtual camera left/right/up/down — not by shifting UVs. Objects closer to the camera naturally shift more in screen space than distant ones: physically correct parallax.

**Camera travel range**

$$T_x = z_\text{near} \times 0.015 \times \frac{k_x}{0.02}, \quad T_y = z_\text{near} \times 0.015 \times \frac{k_y}{0.02}$$

- $z_\text{near}$ — distance from the camera to the closest geometry in the mesh. Closer geometry = tighter travel range, so the nearest surface never slides off screen.
- $0.015$ — calibrated constant. At the default strength ($k=0.02$) it limits the nearest pixel's shift to ~3% of the screen half-width.
- $k_x, k_y$ — `parallax_strength` per axis. Scales travel linearly.
- $T_x, T_y$ — the maximum distance the camera can slide in each direction.

**Camera position**

$$t_x = -(x_\text{current} - 0.5) \times 2 \times T_x$$
$$t_y = -(y_\text{current} - 0.5) \times 2 \times T_y$$

- $x_\text{current}, y_\text{current}$ — the ghost cursor position from step 1.
- Subtracting 0.5 centers the range to $[-0.5,\ +0.5]$, multiplying by 2 brings it to $[-1,\ +1]$, then scaled by $T$.
- The leading minus sign flips the direction: the camera moves opposite to the mouse so the scene appears to follow the cursor.

**Translation matrix** (`math.rs → translation()`)

The camera offset is encoded as a $4\times4$ matrix that slides every vertex before projection:

$$V = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ t_x & t_y & t_z & 1 \end{bmatrix}$$

- $t_x, t_y$ — camera shift from above. Moves the whole world sideways.
- $t_z = 0$ — camera stays at the same depth; only lateral movement.

**Perspective matrix** (`math.rs → perspective()`)

Maps 3D world positions to 2D screen positions — objects farther away appear smaller, exactly like a real camera lens:

$$P = \begin{bmatrix} f/A & 0 & 0 & 0 \\ 0 & f & 0 & 0 \\ 0 & 0 & \frac{z_f+z_n}{z_n-z_f} & -1 \\ 0 & 0 & \frac{2 z_f z_n}{z_n-z_f} & 0 \end{bmatrix}, \quad f = \frac{1}{\tan(\theta/2)}$$

- $\theta$ — vertical field of view in radians. Wider angle = more scene visible but more distorted.
- $f$ — focal length. Derived from $\theta$. Larger $f$ = narrower, more telephoto view.
- $A$ — screen aspect ratio ($W/H$). Corrects horizontal scale so circles look round, not oval.
- $z_n, z_f$ — near and far clip distances. Geometry closer than $z_n$ or farther than $z_f$ is not drawn.

Every vertex goes through: $\text{clip position} = P \times V \times \text{vertex}$

**Cover FoV**

If the image is a different shape than the monitor, a plain FoV would leave black bars. The renderer finds the narrowest $\theta$ that still fills both axes:

$$\phi_x = 2\arctan\!\left(\frac{A_\text{image} \cdot \tan(\theta/2)}{A_\text{screen}}\right)$$

$$\theta_\text{cover} = \min(\theta,\ \phi_x)$$

- $\phi_x$ — the FoV that makes the image's width exactly fill the screen width.
- $\theta_\text{cover}$ — the smaller (more zoomed-in) of the two, guaranteeing coverage on both axes.

Then the same zoom-for-parallax logic as flat mode is applied:

$$\theta_\text{final} = \frac{\theta_\text{cover}}{1 + \max(k_x,k_y) \times 2}$$

Narrowing the FoV is equivalent to zooming in — it prevents the camera's lateral movement from revealing empty space past the mesh edges.

---

## Common Mistakes

**"It's just CSS parallax"** — No. It's per-pixel depth-shifted rendering in OpenGL with an AI-generated depth map. CSS parallax uses fixed layers.

**"The depth map IS the 3D model"** — In the basic mode, yes, it's a shader hack. In inpaint mode, a real triangle mesh is built from it.

**"Reloading restarts everything"** — No. `waydeeper reload` sends a message over the IPC socket. The daemon regenerates assets in the background and swaps them in without touching the Wayland surface.

**"It re-runs the AI every launch"** — No. Results are cached by content hash. Same image + same model = instant load.
