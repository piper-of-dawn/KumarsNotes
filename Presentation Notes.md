

  

“Just a heads-up — I’m keeping this a bit informal and light on jargon. It’s easier to communicate the ideas that way.”

  

“We had very large MTM matrices, and comparing them trade by trade was expensive and hard to reason about. Mostly painful.

The solution was to collapse the entire trade MTM matrix into a single deterministic number. That number acts as a fingerprint for the whole matrix.

  Same number means nothing changed. Different number means something definitely changed  no debates required.

  The tricky parts were floating-point noise and ordering. Floating-point math doesn’t like being hashed, and trade ordering isn’t guaranteed.

  

The benefit is that when you see a diff, you immediately know it comes from a real trade MTM change.

That turns long investigations into much quicker root-cause analysis.”
# linux first

I’m a Linux-first developer. I do my day-to-day work on Linux, and that naturally put me in the role of handling Linux issues for the team.

Linux is the truth environment for us. If something fails on Linux, it will fail in production, so those failures matter.

In practice, that means when something breaks on Linux, it usually becomes my problem.

About once a month on average, I’m debugging a segfault in code I didn’t write, don’t know, and didn’t expect to touch.

That kind of work is hard, but it’s also where real production issues get found and fixed.
## Cloud


The key realization for me was the leverage you get from cloud virtual machines.

Instead of treating machines as long-lived setups, I started treating them as disposable and scalable compute.

  

I used Google Cloud VMs to spin up Linux-first environments that are much closer to production than local machines.

That also shifted the mindset for me: local machines are limited, the VM is the source of truth.

  

I showed that these VMs are not just for large batch jobs, but can be used for day-to-day engineering work.

As a proof of concept, I was able to build NOLA in under five minutes on a fresh VM.

  

That led to an important insight: build time was an infrastructure limitation, not a code problem.

With a deterministic VM setup, builds became reproducible and debugging became much faster.

  

This proof of concept naturally led to the next step, which is designing an official NOLA Docker image.

The goal is one image with the same behavior everywhere: development, CI, IT, and production.

The outcome is faster onboarding, fewer environment issues, and cleaner regressions.”

