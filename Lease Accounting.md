
## How Leases “Wear Off” Under IFRS 16 vs US GAAP (ASC 842)

### Non-negotiable rule (both IFRS & US GAAP)
For lessees, under **IFRS 16** and **ASC 842**:

- You **must** recognize:
  - a Right-of-Use (ROU) asset, and
  - a Lease liability
- For **almost all leases**, finance *and* operating.

No more off–balance sheet leases, except IFRS short-term / low-value policy choices.

**Memory hook:** “If you lease it, you show it.”

### Lease liability (both IFRS & GAAP)
Under **both** frameworks:

- Lease liability is measured using the **effective interest rate method**:
  - Interest expense = Opening liability × discount rate
  - Principal = Cash payment – Interest
  - Closing liability = Opening liability + Interest – Payment

**Key point:**  
Only the **principal** portion reduces the liability.  
This is why early in the lease, the liability falls slowly and you end up in a **net lease liability position** (liability > ROU asset).

---

### IFRS 16 — Lessee (Single Economic Model)

For all non-trivial leases:

- **Liability**: EIRM (as above).  
- **ROU asset**: typically depreciated **straight-line** over the lease term.  
- **Income statement**:
  - Depreciation expense
  - Interest expense
- **Expense pattern**: front-loaded because interest is higher in early years.
- **Balance sheet over time**:
  - ROU asset falls **evenly**.
  - Lease liability falls **non-linearly** (slow at first, faster later).
  - Very often → **net liability position** after a while.

**Memory hook:** “IFRS: always finance-lease economics.”

---

### US GAAP ASC 842 — Lessee

Under ASC 842, lessees classify leases as **finance** or **operating**, but:

- **Both** put ROU + liability on the balance sheet.
- **Both** use EIRM for the liability.

#### Finance lease (GAAP)
Economically same as IFRS:

- Liability: EIRM  
- ROU asset: generally amortized **straight-line**  
- P&L:  
  - Interest expense  
  - Amortization (presented with other depreciation/amortization)  
- Expense pattern: front-loaded (just like IFRS finance lease).

#### Operating lease (GAAP)
Here is the key twist:

- Liability: still EIRM  
- Total lease cost: must be **straight-line** over the term.  
- Mechanics:
  - Compute straight-line lease expense for the whole term.  
  - Each period:  
    - Interest = EIRM on liability  
    - **ROU amortization = Straight-line lease cost – Interest**
- Presentation:
  - P&L shows **one lease expense line**, not separate interest + depreciation.

So for GAAP operating leases:

- **Total expense** = smooth straight-line.  
- **ROU amortization is NOT straight-line**; it is a plug so that  
  `interest + amortization = straight-line lease expense`.

**Memory hook:** “GAAP: one balance sheet; two income statement shapes.”

---

### Net liability position (intuitive recap)

At t = 0:
- ROU asset ≈ Lease liability.

Over time (finance lease IFRS / GAAP; operating lease GAAP behind the scenes):

- Liability reduces only by principal.
- Principal early in the term is small (interest is large).
- ROU asset (if straight-line) falls faster than liability.

Result:

- ROU asset < Lease liability → **net liability**.
- The difference flows through **equity** via cumulative lease expenses.

**Memory hook:**  
“ROU wears out with use, liability pays down with cash — those two clocks don’t tick at the same speed.”