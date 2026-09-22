# Checkpoint 78–83 Status — Corrected Reach, Resolved Relay, Local-Scale Gate

## Critical correction to checkpoints 71–74

A bug was found in the original local-reach diagnostic used in checkpoint 74: the `reach()` function returned from inside the outer neighbor-exclusion loop. It therefore excluded adjacent nodes correctly only around one vertex before taking the global minimum. Reported very small half-self-separations from that diagnostic (including the ~0.004 value previously highlighted) are not valid evidence of a newly generated physical subscale.

In addition, the `eps=0.01, N=80` Z-space run was strongly under-resolved relative to its regularization core: the arclength node spacing was much larger than `eps`. Checkpoints 71–74 remain useful exploratory geometry tests, but their quantitative small-reach claims are superseded.

## Corrected convergence check

The reach routine was fixed so that the arclength-neighbor exclusion is applied to every node before the global nonlocal separation is computed. Re-running the old `eps=0.01` trajectory at N=80, 120, and 160 showed strong resolution dependence, confirming that the thin-core run was not converged.

## Reach-safe relay search

A deterministic random search over low Fourier modes found many closed four-arc shapes with all four cyclic stretching links initially positive and simultaneous global contraction while having much larger geometric reach than the old shape.

One selected candidate has, after refinement,

- reach ~0.10,
- positive cyclic stretching on all four links,
- global contraction,
- and can be simulated with core regularization comparable to or larger than the node spacing.

## Better-resolved dynamics

For the selected candidate:

- N=256, core=0.05: relay/contraction failure at s=0.450, with reach ~0.142 > core.
- N=320, core=0.04: failure at s=0.435, with reach ~0.161 > core.
- N=384, core=0.03: failure at s=0.375, with reach ~0.163 > core.

Thus the relay loses simultaneous contraction + cyclic stretching *before* core overlap in every tested better-resolved case. Smaller tested core does not uncover a longer-lived collapsing relay.

The N=256 run can later generate tiny geometric separation, but only long after global contraction has failed; by the time the first core/reach overlap occurs (`s≈1.695`) the relevant cyclic relay links have already changed sign, and the geometry is expanding. Those later folds are not evidence of a singular collapsing cascade.

## Local-scale gate

Let `delta(t)` be the actual active geometric scale (e.g. local reach), `b=a^2` a coherent transverse core width, and assume a local strain-diffusion inequality/model

    b_dot >= -sigma b + c_nu nu.

Set

    y = b/delta^2,
    gamma = -delta_dot/delta.

Then

    y_dot >= c_nu nu/delta^2 + (2 gamma - sigma)y.

Using local nonlinear time `ds/dt = Gamma_delta/delta^2` gives

    dy/ds >= c_nu/Re_delta - A_delta y,

where

    Re_delta = Gamma_delta/nu,
    A_delta = (sigma - 2 gamma) delta^2 / Gamma_delta.

Therefore if both `Re_delta` and `A_delta` stay bounded above along an infinite renormalized cascade, `y=a^2/delta^2` cannot tend to zero. A coherent finite-core singular cascade must force at least one of the following:

1. `Re_delta -> infinity` (unbounded scale-critical circulation/amplitude), or
2. `A_delta -> infinity` (unbounded normalized strain advantage over geometric collapse), or
3. loss of the coherent-core reduction itself (reconnection, sign cancellation, sheet/point geometry, etc.).

This is the cleanest current “next-variable” statement. Bounded renormalized geometry is not enough for the singularity; some dimensionless quantity must genuinely diverge.

## Current verdict

The earlier apparent “shrinking ruler” escape in the toy relay was partly a diagnostic/resolution artifact and has been retracted. In the corrected, better-resolved relay tests, the closed internal stretching cycle loses collapse before finite-core contact.

This still does not prove Navier–Stokes regularity. The surviving mathematical adversary is a Type-II/local-critical mechanism that drives `Re_delta` or `A_delta` unbounded (or ceases to resemble a coherent tube) while remaining an unforced finite-energy solution.
