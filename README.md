# Failure to Corner

Exploratory notes, symbolic checks, reduced vortex-filament simulations, finite-core models, and renormalized-state experiments motivated by a geometric question about the 3-D unforced incompressible Navier–Stokes equations:

> Can a viscous vortex generate and sustain the increasingly sharp geometry required for a finite-time singularity using only its own internally generated strain?

**Status:** research notebook / adversarial exploration, **not a proof**. See [NOTICE.md](NOTICE.md) and [docs/RESEARCH_NOTE.md](docs/RESEARCH_NOTE.md).

## What is in this repository

- `docs/RESEARCH_NOTE.md` — consolidated checkpointed notebook containing derivations, corrections, literature anchors, and current proof target.
- `docs/FORENSIC_LOG.md` — chronological audit log preserving failed approaches and corrections.
- `docs/checkpoints/` — shorter status snapshots from later runs.
- `src/` — portable copies of the Python checks and reduced simulations. Generated files are written to `outputs/` when the scripts are run from the repository root.
- `archive/original_scripts/` — exact sandbox-era scripts as originally executed; these may contain `/mnt/data/...` output paths.
- `results/text/` — captured text output from symbolic checks and simulations.
- `data/csv/` — generated traces and parameter sweeps.
- `data/npy/` — saved geometry/state arrays created during the experiments.
- `FINDINGS.md` — concise separation of established identities, model/numerical findings, retractions, and unresolved escape routes.
- `MANIFEST.md` — file inventory with SHA-256 hashes.

## Quick start

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python tools/verify_repo.py
```

Run an individual checkpoint from the repository root, for example:

```bash
python src/checkpoint_52_pair_contact_verify.py
python src/checkpoint_60_closed_relay_test.py
python src/checkpoint_81_resolved_zrelay.py
```

Fresh run artifacts go to `outputs/`; the historical outputs used in the notebook are preserved under `results/` and `data/`.

## Current research picture

The work progressively ruled out several naive mechanisms without proving global regularity. In particular:

1. The exact vorticity-magnitude equation charges directional bending through `-ν|ω||∇ξ|²`.
2. Straight near-self-contact has leading Biot–Savart cancellations: the strongest induced velocity is transverse to the gap and the leading longitudinal stretching vanishes at closest approach.
3. Curvature breaks this cancellation at a weaker scale, so critical self-stretching requires curvature to grow with the shrinking gap.
4. A local pair interaction that actually closes a near-aligned gap is anti-stretching in the reduced filament asymptotic; amplification must therefore be supplied nonlocally.
5. Closed multi-segment relays can temporarily outsource stretching internally, so “a closed vortex can never self-amplify” is false.
6. In the tested relays, contraction fails before runaway amplification; adding finite-core dynamics produces a positive relative-core floor for bounded renormalized geometry at finite circulation Reynolds number.
7. The local coherent-core inequality sharpens the remaining escape: while the relative core thickness `y=a²/δ²` is decreasing, the product `A_δ Re_δ` must grow at least like `1/y`; the two apparent escape variables are therefore not independent.
8. In the resolved relay, stretching at the local shrinking ruler is weaker than stretching available elsewhere on the loop. The dangerous mechanism is consequently an internally outsourced, multiscale strain transfer rather than a purely local self-collapse.
9. The remaining full-PDE route is a Type-II/unbounded-critical-amplitude cascade, repeated creation of a smaller ruler, or loss of coherent-tube geometry.

See [FINDINGS.md](FINDINGS.md) for the qualified version of every item.

## Important correction preserved in the history

An early local-reach diagnostic in the `checkpoint_74` family was later found to return before correctly excluding neighboring points around the full filament and was also used in an under-resolved case. The claimed resolved subscale generated from that diagnostic was retracted. Checkpoints `78–83` repair the reach calculation and rerun the relay at better resolution. Both the flawed historical run and the corrected work are retained for auditability.

## Scope

These programs are reduced models, asymptotic checks, and numerical experiments. They are not DNS of the full three-dimensional Navier–Stokes PDE and should not be represented as such. Their purpose is to attack candidate singular mechanisms, expose incorrect intuitions quickly, and formulate sharper analytic targets.

## Latest incremental checkpoint: 84–86

The newest run derives the necessary coherent-core gate

\[
A_\delta Re_\delta\,\frac{a^2}{\delta^2}\ge c_\nu
\]

whenever the relative core thickness is actually decreasing. A remote pusher at distance `d` therefore needs, schematically, `Re_source ≳ (d/a)^2`; if it avoids that amplitude growth by moving to `d=O(a)`, then `a` has become the new renormalization scale. See `docs/checkpoints/checkpoint_84_86_STATUS.md`.
