# Checkpoints 95–98 — diffusion-compatible Kelvin hierarchy and route boundary

**Status:** this run does **not** prove global regularity or construct a blowup. It closes the present *proof strategy* by finding a formal multiscale bridge that survives the reduced cornering/core/circulation budgets.

## 95. A diffusion-compatible Kelvin layer is thicker and stronger than the one-step `delta/Re` picture

Checkpoint 93 used the exact viscous Kelvin identity

\[
\frac{d\Gamma}{dt}
=-\nu\oint_{C(t)}(\nabla\times\omega)\cdot dx
\]

to show that order-one circulation change on a parent nonlinear time requires a vorticity gradient of order

\[
|\nabla\omega|\sim \frac{\Gamma^2}{\nu\delta^3}.
\]

If the vorticity jump across that gradient is artificially restricted to the parent amplitude

\[
\Omega_p\sim\frac{\Gamma}{\delta^2},
\]

then its thickness is indeed

\[
\ell\sim\frac{\delta}{Re_\Gamma}.
\]

That statement remains correct. The over-strong interpretation was to treat this as the only dynamically relevant layer.

A local 1-D heat-step calculation gives a more adversarial possibility. For a vorticity jump `A` diffusing across an interface, the exact integrated diffusive flux per unit tangential length is

\[
Q(\tau)=A\sqrt{\frac{\nu\tau}{\pi}}.
\]

If a boundary segment of length `L~delta` transfers `Delta Gamma~Gamma` during one parent nonlinear time

\[
\tau_p\sim\frac{\delta^2}{\Gamma},
\]

then the diffusion-compatible thickness and jump scale as

\[
\boxed{\frac{h}{\delta}\sim Re_\Gamma^{-1/2}},
\qquad
\boxed{\frac{A}{\Omega_p}\sim Re_\Gamma^{1/2}}.
\]

The circulation scale carried by such a layer is

\[
\Gamma_h\sim A h^2,
\]

hence

\[
\boxed{Re_h\sim Re_\Gamma^{1/2}}.
\]

So the layer capable of persisting for the whole parent nonlinear time is **not** necessarily a low-Re `1/Re` roadkill layer. It can be an intermediate, still-high-Re object.

This is a reduced diffusion model, not a full 3-D construction.

## 96. The direct `delta/Re` ruler can be resolved into a square-root Reynolds ladder

Iterate the diffusion-compatible scaling:

\[
R_{j+1}=\sqrt{R_j},
\qquad
\delta_{j+1}=\frac{\delta_j}{\sqrt{R_j}},
\qquad R_j=Re_j.
\]

Then

\[
\frac{\Omega_{j+1}}{\Omega_j}=\sqrt{R_j}=R_{j+1},
\]

and the exact closed forms are

\[
R_j=R_0^{2^{-j}},
\qquad
\delta_j
=\delta_0 R_0^{-(1-2^{-j})}.
\]

Therefore

\[
R_j\to1,
\qquad
\delta_j\to\frac{\delta_0}{R_0}.
\]

The number of intermediate levels needed to reach `Re=O(1)` is only `O(log log Re_0)`.

Examples from the script:

- `Re_0=10^4`: `10^4 -> 100 -> 10 -> 3.16 -> 1.78`;
- `Re_0=10^8`: `10^8 -> 10^4 -> 100 -> 10 -> 3.16 -> 1.78`;
- `Re_0=10^16`: six square-root reductions reach the same order-one terminal range.

This ladder does **not** prove that Navier–Stokes dynamically manufactures the required nested geometry. It proves something narrower and important for the research logic: the checkpoint-93 one-step promotion cost is not by itself a contradiction.

## 97. The helper ladder does not generate a new divergent critical budget

For a single-scale vortex estimate use

\[
E_j\sim \Gamma_j^2\delta_j,
\qquad
D_j\sim \nu\Gamma_j\delta_j,
\qquad
I_j\sim\Gamma_j\delta_j^2,
\qquad
\tau_j\sim\frac{\delta_j^2}{\Gamma_j}.
\]

Under the square-root recursion,

\[
\frac{E_{j+1}}{E_j}=R_j^{-3/2},
\qquad
\frac{D_{j+1}}{D_j}=R_j^{-1},
\qquad
\frac{\tau_{j+1}}{\tau_j}=R_j^{-1/2}.
\]

The computed sums are dominated by the outermost level. Thus the intermediate hierarchy creates no fresh divergence in these reduced energy, dissipation, impulse, or time proxies.

This is exactly the obstruction imposed by critical scaling: making the hierarchy more complicated does not automatically make it too expensive.

### Correction to checkpoint 93 interpretation

Checkpoint 93 remains correct as a conditional calculation **at inherited parent vorticity amplitude**. What is withdrawn is the stronger rhetorical inference that the `O(Re^2)` promotion of that thinnest layer is probably fatal. A dense Type-II mechanism can use intermediate diffusion-compatible layers as transient flux-transfer machinery without requiring the first `delta/Re` layer to become the next primary high-Re vortex in one jump.

## 98. The present cornering proof route has reached the known critical gap

The work still gives meaningful conditional results:

- leading straight self-contact interactions are geometrically depleted;
- near-aligned local closure is anti-stretching in the filament asymptotic;
- fixed/comparable coherent finite-core relays acquire a positive relative-core floor;
- bounded renormalized coherent states cannot keep `a/delta -> 0` at finite `Re`;
- a same-tube spatial change of ruler does not manufacture larger circulation.

But the remaining adversary is explicitly **unbounded in a scale-critical quantity**. That is exactly where established full-PDE regularity theory says a hypothetical singularity has to go.

Relevant known boundaries:

1. Seregin proved that a finite-time blowup requires

   \[
   \|u(t)\|_{L^3}\to\infty
   \]

   as the blowup time is approached (`arXiv:1104.3615`).

2. Tao quantified the critical `L^3` theory and obtained a necessary minimum growth rate along a sequence approaching a hypothetical blowup (`arXiv:1908.04958`).

3. Miller obtained scale-critical necessary/sufficient blowup criteria involving the positive part of the middle eigenvalue of the strain tensor (`arXiv:1710.05569`). He also exhibited a strain self-amplification model with finite-time blowup despite preserving important Navier–Stokes strain/enstrophy structure (`arXiv:1910.05415`).

4. Current Type-II work explicitly studies unbounded-rescaling scenarios beyond bounded self-similar compactness (`arXiv:2606.29468`).

These results do not prove that the square-root helper hierarchy exists. They show why our remaining target is not something another rearrangement of the same energy/core scaling is likely to eliminate.

## Research verdict after checkpoint 98

The original geometric intuition survives in a **qualified** form:

> A coherent vortex cannot simply close on itself and obtain singular amplification from the same local geometry doing the closing; several such mechanisms are depleted, anti-stretching, or finite-core inconsistent.

The stronger statement

> an unforced Navier–Stokes flow cannot blow up because it cannot internally sustain the required multiscale strain/circulation chain

has **not** been proved.

The dense Type-II escape can be organized at the level of reduced scaling without violating any budget derived here. Closing it requires a genuinely new full-PDE estimate controlling a scale-critical object such as critical velocity amplitude, positive middle strain, stochastic area distortion, or an equivalent quantity.

**Recommendation:** treat checkpoints 1–98 as a completed adversarial study of the “failure to corner” proof route. Resume only if a new estimate is found that acts at the critical Type-II level; otherwise further scale bookkeeping is expected to reproduce the same gap.
