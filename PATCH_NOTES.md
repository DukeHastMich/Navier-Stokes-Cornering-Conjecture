# Checkpoint 87–90 incremental update

Base commit: `aa504c0`  
New commit: `a8466c7` — **Checkpoint 87-90: isolate the Type-II escape window**

## Main findings

- Same coherent instantaneous vortex tube: `div omega=0` fixes the vorticity flux/circulation across cross-sections, so changing ruler inside one tube does not itself increase `Gamma/nu`.
- An abstract circulation-amplifying cascade `Gamma_n=m^n`, `delta_n=q^n` has a nonempty formal finite-budget window `q<1/m^2`; current scale/core/energy/Zeno-time inequalities alone therefore do not rule out Type-II escape.
- Constantin–Iyer statistical Kelvin backtracking converts small-scale growing circulation into a rapidly growing stochastic back-to-label area-distortion requirement.
- Combining the backward-area requirement with the other reduced gates still leaves a formal Type-II parameter window. The next advance requires a genuinely NSE-specific estimate rather than another dimensional budget.

## Apply

Preferred:

```bash
git am Navier-Stokes-Cornering-Conjecture-update-87-90.patch
git push
```

Alternatively overlay the ZIP contents onto the repository, then:

```bash
git add .
git commit -m "Checkpoint 87-90: isolate the Type-II escape window"
git push
```

All 23 checkpoint Python scripts compile and `git diff --check` passed before packaging.
