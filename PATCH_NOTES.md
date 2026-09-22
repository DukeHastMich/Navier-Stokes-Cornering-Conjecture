# Incremental update — Checkpoints 84–86

Baseline: `22ce932` — Initial research snapshot: Failure to Corner  
Commit: `aa504c0` — Checkpoint 84-86: reduce escape variables to a core gate

## Main changes

- Derives the necessary coherent-core gate `A_delta Re_delta y >= c_nu` whenever `y=a^2/delta^2` is nonincreasing.
- Shows the two former escape variables are coupled: if `a/delta -> 0`, their product must diverge at least like `1/y`.
- Derives remote-pusher scaling `Re_source ≳ (d/a)^2` up to model geometry constants.
- Connects the `Re_delta` escape heuristically to critical `L^3` amplitude, while explicitly retaining the distinction from a full PDE theorem.
- Instruments the corrected closed-relay model to compare stretching at the shrinking ruler, within `2 delta`, and globally.
- Adds a three-resolution/core sweep and records that nonlocal/outsourced stretching improves the gate, while the relay still loses its collapsing cyclic state.
- Freezes `MANIFEST.md` explicitly as the initial-release manifest so later incremental commits do not pretend to preserve those original hashes.

## Apply

Preferred Git-native application from the repository root:

```bash
git am Navier-Stokes-Cornering-Conjecture-update-84-86.patch
```

Or copy the delta ZIP contents over the repository and commit manually.

## Verification

The local repository passed:

```text
python tools/verify_repo.py
Compiled 19/19 scripts.

git diff --check
# clean
```
