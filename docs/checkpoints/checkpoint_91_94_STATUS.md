# Checkpoints 91–94 — circulation jugular run

**Status:** conditional narrowing only; no global Navier–Stokes regularity proof.

## 91. Same-tube circulation does not grow under ordinary coherent stretching

For the aligned parallel-tube reduction

\[
\omega=\zeta(x_\perp,t)e_z,
\qquad
u=(v_\perp(x_\perp,t),\sigma(t)z),
\qquad
\nabla_\perp\cdot v_\perp=-\sigma,
\]

the axial vorticity equation can be written exactly as

\[
\partial_t\zeta+\nabla_\perp\cdot(v_\perp\zeta)=\nu\Delta_\perp\zeta.
\]

Hence, for sufficiently decaying fields,

\[
\Gamma(t)=\int_{\mathbb R^2}\zeta\,dA
\]

obeys

\[
\boxed{\frac{d\Gamma}{dt}=0.}
\]

The Gaussian/Burgers-type special case has

\[
\dot b=-\sigma(t)b+4\nu
\]

for the mean-square core radius while `Gamma` remains fixed. The numerical check used strongly time-dependent strain; peak vorticity changed by more than an order of magnitude while numerical circulation remained constant to about `3.4e-7` relative quadrature error.

**Interpretation:** ordinary coherent stretching can raise `omega` by shrinking the cross-section, but it does not supply the `Gamma_{n+1}>Gamma_n` assumption used in the checkpoint-88 Type-II toy cascade.

## 92. Nested one-sign cores cannot hide a circulation increase

For aligned one-sign cross-sectional vorticity,

\[
\Gamma(R)=2\pi\int_0^R\zeta(r)r\,dr,
\qquad
\Gamma'(R)=2\pi R\zeta(R)\ge0.
\]

Therefore a smaller nested cross-section at one instant cannot contain more same-signed circulation than a larger one.

For a material radial boundary in the same coherent reduction,

\[
\frac{d\Gamma_R}{dt}=2\pi\nu R\,\partial_r\zeta(R,t).
\]

If the core decreases monotonically outward, `partial_r zeta <= 0`, viscosity makes the enclosed circulation **decrease**, not increase.

Thus same-lineage circulation amplification requires at least one of:

- recruitment of flux from outside the previous core;
- a non-monotone/sign-changing boundary layer;
- reconnection / tube redefinition;
- loss of coherent-tube geometry.

## 93. Viscous Kelvin law creates a gradient trap

For a material loop `C(t)`, the ordinary viscous Kelvin identity is

\[
\frac{d\Gamma}{dt}
=\nu\oint_{C(t)}\Delta u\cdot dx
=-\nu\oint_{C(t)}(\nabla\times\omega)\cdot dx.
\]

Assume a loop of length `O(delta)` increases its circulation by an order-one fraction during one parent nonlinear time

\[
\tau_{nl}\sim\frac{\delta^2}{\Gamma}.
\]

Then at some time in that interval one needs

\[
\boxed{
\|\nabla\omega\|_{C}
\gtrsim
\frac{\Gamma^2}{\nu\delta^3}.
}
\]

Relative to the natural parent vorticity scale

\[
\Omega_\delta\sim\frac{\Gamma}{\delta^2},
\]

this defines a gradient ruler satisfying

\[
\boxed{
\frac{\ell_{grad}}{\delta}
\lesssim
\frac1{Re_\Gamma},
\qquad
Re_\Gamma=\frac{\Gamma}{\nu}.
}
\]

The viscous time on that ruler is shorter than the parent nonlinear time by the same factor,

\[
\frac{\tau_\nu(\ell_{grad})}{\tau_{nl}}
\lesssim
\frac1{Re_\Gamma}.
\]

If the new ruler initially inherits only the parent vorticity amplitude, its local circulation Reynolds number is

\[
Re_{\ell}\sim\frac1{Re_\Gamma},
\]

so it is **strongly diffusive**, not a new high-Re vortex.

To promote this subscale to a next-generation vortex with

\[
Re_{next}=mRe_\Gamma
\]

requires a vorticity-amplitude increase of order

\[
\boxed{mRe_\Gamma^2.}
\]

Examples for `m=2`:

- `Re=10`: boost ~`2e2`;
- `Re=100`: boost ~`2e4`;
- `Re=1000`: boost ~`2e6`;
- `Re=10000`: boost ~`2e8`.

**Interpretation:** circulation amplification is not a free parameter. At high Reynolds number it first demands a still-smaller, faster-diffusing vorticity-gradient layer. Turning that layer into the next high-Re generation requires an enormous additional amplitude escalation.

## 94. If amplification is done by mergers, the flux must come from somewhere

If a lineage grows by signed-flux recruitment,

\[
\Gamma_{n+1}=m\Gamma_n,
\]

then the net recruited circulation at stage `n` is

\[
\Delta\Gamma_n=(m-1)\Gamma_n,
\]

and telescoping gives

\[
\sum_{k=0}^{N-1}\Delta\Gamma_k
=
\Gamma_N-\Gamma_0.
\]

Therefore `Gamma_N -> infinity` requires an unbounded **net signed-flux reservoir**. Splitting and re-merging the same flux cannot multiply the signed total.

A conditional packing lemma also rules out one simple way to preload that reservoir. If the initial vorticity is `C^1`, distinct donor tubes are geometrically comparable and isolated from one another by low-vorticity gaps of comparable width, then bounded `||grad omega_0||_inf` forces the peak vorticity of a donor of radius `r` to be `O(r)`. Its circulation is then `O(r^3)`. Pairwise-disjoint comparable neighborhoods in bounded volume have finite `sum r^3`, hence finite total recruitable circulation.

This is **conditional**. It does not cover a dense cluster, sheet, sign-changing region, or a sequence of reconnections where the notion of distinct isolated tubes breaks down.

That distinction matters because rigorous Navier–Stokes constructions show that arbitrarily complicated **finite** vortex-reconnection cascades can occur in smooth global solutions. Therefore reconnection itself cannot be assigned a universal fixed dissipation toll.

## Current branch structure

The checkpoint-88 formal Type-II corridor has now split into two much more specific mechanisms:

1. **same-lineage viscous circulation growth:** must pass the Kelvin gradient trap, creating `ell/delta ~ 1/Re` layers that diffuse `Re` times faster than the parent nonlinear clock;
2. **merger/recruitment growth:** must import unbounded net signed flux, and cannot obtain it from a finite collection of isolated comparable donor tubes.

What remains genuinely open is a dense, non-isolated, multiscale cluster in which coherent tube identity repeatedly fails and new high-Re structure is manufactured inside increasingly thin gradient layers.

That is a narrower target than the checkpoint-90 abstract `Gamma_n=m^n` cascade, but it is not yet contradictory.
