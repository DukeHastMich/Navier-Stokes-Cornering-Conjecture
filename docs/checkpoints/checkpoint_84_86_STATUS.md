# Checkpoints 84–86 — Escape-variable gate

**Status:** conditional coherent-core analysis plus reduced regularized-filament diagnostics. **Not a proof of Navier–Stokes regularity.**

## 84 — Collapse the two escape variables into one gate

Starting from the local-scale coherent-core comparison

\[
\frac{dy}{ds}\ge \frac{c_\nu}{Re_\delta}-A_\delta y,
\qquad y=\frac{a^2}{\delta^2},
\]

with

\[
Re_\delta=\frac{\Gamma_\delta}{\nu},
\qquad
A_\delta=\frac{(\sigma-2\gamma)\delta^2}{\Gamma_\delta},
\qquad
\gamma=-\frac{\dot\delta}{\delta},
\]

there is a simple necessary condition whenever the relative core thickness is actually nonincreasing:

\[
\boxed{A_\delta Re_\delta y\ge c_\nu.}
\]

Equivalently,

\[
\boxed{A_\delta Re_\delta\ge \frac{c_\nu}{y}}
\]

or

\[
\boxed{\frac{(\sigma-2\gamma)a^2}{\nu}\ge c_\nu.}
\]

Therefore the earlier `Re_delta -> infinity` and `A_delta -> infinity` doors are not independent. If `a/delta -> 0` while the relative core continues shrinking, their **product** must diverge at least as `1/y`.

For the illustrative `c_nu=4` model, driving `y` through `10^-1, 10^-2, ..., 10^-6` requires `A_delta Re_delta` of at least `40, 400, ..., 4e6`.

## 85 — Remote pusher scaling

If a separate coherent source a distance `d` away supplies at most

\[
\sigma\lesssim C\frac{\Gamma_s}{d^2},
\]

then the same core gate implies

\[
\boxed{Re_s=\frac{\Gamma_s}{\nu}\gtrsim \frac{c_\nu}{C}\left(\frac d a\right)^2.}
\]

So a source that remains at the outer geometric scale `d ~ delta` while `a/delta -> 0` must acquire `Re_s ~ 1/y`. If instead the source approaches to `d=O(a)`, it has created a new active ruler at the core scale; that is a **renormalization escape**, not an independent large-`A` mechanism.

This turns the surviving coherent-tube picture into a dichotomy:

1. the scale-critical amplitude/circulation grows without bound; or
2. a new smaller interaction scale forms and the analysis must be renormalized there.

In a coherent single-scale blob with `U_delta ~ Gamma_delta/delta`, the local `L^3` size scales like `U_delta delta ~ Gamma_delta`. Thus `Re_delta -> infinity` is the reduced-model analogue of unbounded critical velocity amplitude. This is consistent with Seregin's theorem that a genuine finite-time 3-D Navier–Stokes blowup must satisfy

\[
\|u(t)\|_{L^3(\mathbb R^3)}\to\infty
\quad\text{as }t\uparrow T.
\]

Reference: G. Seregin, *A Certain Necessary Condition of Potential Blow up for Navier-Stokes Equations*, Comm. Math. Phys. 312 (2012), 833–845, DOI `10.1007/s00220-011-1391-x`, arXiv:1104.3615.

## 86 — Resolved relay diagnostic

The reach-safe closed relay from checkpoints 80–82 was instrumented with a local-scale gate. The physical local shrink rate was reconstructed from the normalized trajectory through

\[
\widehat\gamma= -\left(\rho+\frac{d}{ds}\log\delta_Z\right).
\]

Three variants of the available axial stretching were compared while the relay was still globally contracting and its physical local reach was shrinking:

- stretching exactly at the point/pair defining the local ruler;
- the best stretching within two local reach lengths;
- the best stretching anywhere on the closed loop.

The exact-controller stretching is generally insufficient to beat the local geometric shrink. Allowing nearby or global stretching improves the gate, which is direct evidence of **internal outsourcing** rather than self-local amplification.

Across the resolution/core sweep:

| N | regularization/core | relay failure `s` | median required `Re` using best stretch within `2 delta` |
|---:|---:|---:|---:|
| 256 | 0.05 | 0.4425 | ~4511 |
| 320 | 0.04 | 0.4275 | ~5850 |
| 384 | 0.03 | 0.3675 | ~5462 |

These numbers depend on the reduced core coefficient `c_nu=4`, the regularized Biot–Savart model, and the reach diagnostic. They are **not physical Reynolds-number predictions**. Their useful feature is qualitative: the contraction does not discover a growing scale-free local stretching advantage as resolution/core is refined over this range.

The global maximum stretching can be substantially better than the stretching at the local ruler, again reinforcing that the dangerous mechanism must import strain from another part of the geometry. This is the same nonlocal loophole identified analytically earlier.

## Current research boundary

The bounded-geometry finite-core relay is not the remaining hard case. The surviving coherent route must repeatedly do one of the following:

- increase a scale-critical circulation/amplitude so that the effective `Re_delta` diverges;
- create a new smaller active ruler and repeat the renormalization;
- or leave the coherent-vortex-tube class.

This aligns the project with the known Type-II / unbounded-critical-norm boundary of the full PDE rather than closing the Millennium problem. A recent Type-II analysis using Euler rescaling is G. Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468 (2026).
