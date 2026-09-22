# Checkpoint 87–90 status — flux inheritance, Type-II merger window, and backward circulation

**Status:** no global-regularity proof. This run found a genuine limitation of the current geometric/core-budget program: an abstract circulation-amplifying Type-II cascade can satisfy every reduced budget derived so far.

## 87 — Same-tube renormalization does not increase circulation Reynolds number

At any fixed time, for a coherent vortex tube whose side surface is tangent to vorticity,

\[
\nabla\cdot\omega=0
\]

implies equal vorticity flux through every cross-section. Hence the tube strength

\[
\Gamma=\int_S \omega\cdot n\,dS
\]

is independent of which cross-section is chosen. This is kinematic and does not require inviscid time evolution.

A divergence-free axisymmetric toy field with varying tube radius was constructed and numerically integrated; the cross-sectional flux stayed at `Gamma=1` to about `1e-10` while centerline vorticity changed by more than a factor of two.

**Consequence:** simply discovering a smaller ruler *inside the same coherent instantaneous tube* cannot manufacture a larger `Re_Gamma=Gamma/nu`. To make the critical circulation amplitude grow between generations, the dynamics must change the tube strength in time, aggregate flux from other structures, or leave the coherent-tube description.

## 88 — An abstract Type-II circulation-amplifying escape window exists

To stress-test the remaining escape, assume an adversarial generation law

\[
\Gamma_n=m^n\Gamma_0,
\qquad
\delta_n=q^n\delta_0,
\qquad m>1,
\quad 0<q<1.
\]

Using the bounded-geometry core floor `y_n=(a_n/delta_n)^2 ~ 1/Re_n`, one gets

\[
\frac{a_n}{\delta_n}\sim m^{-n/2},
\qquad
\tau_n\sim\frac{\delta_n^2}{\Gamma_n},
\qquad
E_n\sim \Gamma_n^2\delta_n.
\]

The generation ratios are

\[
\frac{\tau_{n+1}}{\tau_n}=\frac{q^2}{m},
\qquad
\frac{E_{n+1}}{E_n}\sim m^2q.
\]

Thus the reduced model has a nonempty formal window

\[
\boxed{q<m^{-2}}
\]

in which `Gamma_n -> infinity`, `a_n/delta_n -> 0`, the Zeno-time sum converges, and the model per-generation dissipation/energy proxy is summable. A slender-filament logarithmic energy factor does not close this window because a polynomial-in-`n` logarithm is dominated by the exponentially decaying factor `(m^2 q)^n`.

For example, `m=2, q=0.20` gives stage-energy ratio `0.8`, time ratio `0.02`, circulation doubling each generation, and relative core thickness reduced by `sqrt(2)` each generation.

This is **not a Navier–Stokes construction**. It is a counterexample to the hope that the current scale/energy/core bookkeeping alone must eventually contradict itself.

## 89 — Walking a small current loop backward forces huge stochastic area distortion

Constantin–Iyer's statistical Kelvin theorem for smooth Navier–Stokes solutions gives, for a closed current loop `C`,

\[
\Gamma_t(C)
=
\mathbb E\,\Gamma_0(A_t(C)),
\]

where `A_t` is the stochastic back-to-label map.

If `C_delta` spans a current surface of area `O(delta^2)` and `M_0=||omega_0||_infty`, Stokes' theorem plus the area formula imply schematically

\[
|\Gamma_t(C_\delta)|
\le
M_0\,C\delta^2\,\mathbb E K_2,
\]

where `K_2` is the two-dimensional area-stretch factor of the back-to-label map on the spanning surface. Therefore

\[
\boxed{
\mathbb E K_2
\gtrsim
\frac{|\Gamma_t(C_\delta)|}{M_0\delta^2}
}.
\]

For a critical-amplitude law `Gamma_delta ~ delta^{-p}`, the required mean backward area stretch scales at least like

\[
\delta^{-(2+p)}.
\]

This gives a precise version of “walk the singular object backward”: a small high-circulation loop must come from stochastic preimages with enormous area distortion. Under a uniform deterministic strain-integral bound `J`, area distortion satisfies a bound of the form `K_2 <= exp(2J)`, producing the necessary floor

\[
J\gtrsim\tfrac12\log K_{2,\mathrm{required}}.
\]

In the genuinely stochastic formula, without extra moment assumptions, the honest conclusion is instead a required exponential moment of the pathwise strain history.

References:

- P. Constantin and G. Iyer, *A stochastic Lagrangian representation of the three-dimensional incompressible Navier–Stokes equations*, Comm. Pure Appl. Math. 61 (2008), 330–345, DOI `10.1002/cpa.20192`.
- The deterministic circulation identity is summarized explicitly in later literature as `∮_C u_t·dx = E[∮_{A_t(C)}u_0·dx]`.

## 90 — The backward-area gate still leaves a Type-II window

For an `m`-fold circulation increase and scale ratio `q`, the stochastic-Kelvin area bookkeeping requires per generation

\[
K_{2,n+1}/K_{2,n}\gtrsim \frac{m}{q^2}.
\]

A uniform strain impulse `I` per generation would therefore need

\[
\boxed{
I\ge \frac12\log\frac{m}{q^2}
= -\log q + \frac12\log m.
}
\]

Combining this with the finite-budget condition `m^2 q<1` leaves a nonempty sampled window once the normalized strain impulse is large enough. For `m=2, q=0.20`, for example,

\[
I_{\min}\approx1.956,
\qquad
m^2q=0.8,
\qquad
q^2/m=0.02.
\]

So even the backward-circulation reconstruction requirement is algebraically compatible with the reduced Type-II cascade.

## Current boundary

The present program has now reached a sharper wall:

> A same coherent tube cannot increase `Re_Gamma` merely by changing ruler, but a hypothetical solution could evade that by dynamically amplifying/aggregating circulation while shrinking the active scale faster than `Gamma^{-2}`. Such a cascade can fit the current core, energy, dissipation, Zeno-time, and stochastic-backward-area budgets simultaneously at the level of scaling algebra.

This is precisely unbounded-critical-amplitude / Type-II territory. Seregin's rigorous theorem that a genuine finite-time blowup must have `||u(t)||_L3 -> infinity` is consistent with this conclusion rather than contradictory to it.

**Next useful move:** stop adding purely algebraic scale budgets. A further advance requires a genuinely Navier–Stokes-specific estimate controlling repeated circulation amplification or stochastic area distortion, or a theorem showing that the normalized strain impulse cannot remain sufficiently large through the infinite cascade.
