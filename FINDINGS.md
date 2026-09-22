# Findings and current status

## 1. Exact PDE identities used

For `ω = Ω ξ`, `Ω = |ω|`, `|ξ| = 1`, and `S = (∇u + ∇uᵀ)/2`, the unforced incompressible Navier–Stokes vorticity equation gives

\[
D_t \Omega = (\xi\cdot S\xi)\Omega + \nu\Delta\Omega - \nu\Omega|\nabla\xi|^2.
\]

The enstrophy dissipation decomposes as

\[
|\nabla\omega|^2 = |\nabla\Omega|^2 + \Omega^2|\nabla\xi|^2.
\]

These exact identities motivate the geometric idea that sharp directional variation carries a viscous cost. They do **not** by themselves prove global regularity.

## 2. Near-contact geometric cancellation

For two locally straight vortex-filament pieces at closest approach, the leading `1/d` induced velocity is transverse to the separation and the leading `1/d²` strain produces zero longitudinal stretching at the closest point. An explicit first-curvature expansion in `checkpoint_52_pair_contact_verify.py` gives a correction of order

\[
O(\Gamma\kappa/d),
\]

rather than the naive `O(Γ/d²)` longitudinal stretching.

This supports the narrower statement that a candidate self-contact singularity must create curvature on the same shrinking scale as the gap.

## 3. Closure is not the amplifier in the reduced pair model

The first-order pair calculation found a regime of near-aligned branches in which the curvature component that drives gap closure gives negative net longitudinal stretching of the pair. Thus, in that local asymptotic model, the mechanism finishing the contact is anti-stretching; positive amplification has to be supplied elsewhere.

This is a reduced-filament statement, not a theorem for arbitrary Navier–Stokes fields.

## 4. A strong local “stretching always straightens” theorem is false

`checkpoint_39_local_jet_verify.py` constructs a divergence-free local velocity jet with initially straight vorticity direction that is stretched while a strain-gradient term instantaneously generates curvature. This invalidates a naive pointwise proof that vortex stretching must always straighten the direction quickly enough.

The surviving conjecture is dynamical and multiscale: individual critical cornering events are possible; the question is whether they can be reproduced through infinitely many shrinking scales.

## 5. Closed internal stretching relays exist temporarily

`checkpoint_60_closed_relay_test.py` searches a closed nonplanar four-arc filament model. It finds states with positive cyclic stretching transfer and simultaneous contraction. Therefore the statement “a closed unforced vortex cannot internally outsource stretching” is false in this reduced model.

In the tested trajectory, however, the geometry loses global contraction before runaway amplification. The normalized shape drifts rather than settling into a repeating collapsing relay.

## 6. Finite-core obstruction in bounded renormalized geometry

For a coherent core width `b=a²` with strain-diffusion model

\[
\dot b = -\sigma b + c_\nu\nu,
\]

and collapsing geometric scale `δ`, define

\[
y = a^2/\delta^2.
\]

Using a local scale-time based on effective circulation gives a comparison form

\[
\frac{dy}{ds}\gtrsim \frac{c_\nu}{Re_\delta} - A_\delta y,
\]

where `Re_δ = Γ_δ/ν` and `A_δ` is a dimensionless strain advantage over geometric contraction.

If both `Re_δ` and `A_δ` remain bounded, the model gives a positive lower bound on `a²/δ²`. Thus a coherent finite-viscosity core cannot become arbitrarily thin relative to its collapsing geometry while the renormalized state remains bounded.

This is a conditional coherent-core result, not a full-PDE theorem.

## 7. Corrected numerical relay behavior

Later high-resolution relay runs (`checkpoint_78` through `checkpoint_82`) corrected an earlier faulty reach diagnostic. In the repaired tests, the combination of global contraction plus all-positive cyclic stretching fails while the estimated local geometric reach is still comfortably larger than the chosen core size. The failure is therefore not explained solely by a core-overlap artifact in those runs.

The numerical experiments are reduced regularized-filament models, not direct numerical simulation of the full Navier–Stokes equations.

## 8. Escape variables collapse to a product gate

For the conditional local coherent-core inequality

\[
\frac{dy}{ds}\ge \frac{c_\nu}{Re_\delta}-A_\delta y,
\qquad y=\frac{a^2}{\delta^2},
\]

any interval on which `y` is nonincreasing must satisfy

\[
\boxed{A_\delta Re_\delta y\ge c_\nu.}
\]

Thus, if a coherent core is to become asymptotically thin relative to its active geometric scale, `A_delta` and `Re_delta` are not independent escape routes: their product must diverge at least like `1/y`.

If a separate coherent source at distance `d` supplies strain no larger than order `Gamma_s/d^2`, then the same gate gives the scaling requirement

\[
Re_s\gtrsim (d/a)^2
\]

up to geometry/order-one constants. A pusher that stays at the outer scale therefore needs unbounded scale-critical circulation as `a/delta -> 0`; a pusher that instead approaches to `d=O(a)` has created a new smaller active scale and forces another renormalization.

A resolved reduced-filament diagnostic (checkpoints 84–86) supports the same qualitative picture: the stretching available exactly at the shrinking local ruler is weaker than the stretching available elsewhere on the loop. Positive amplification is being outsourced nonlocally rather than generated by the local closing geometry itself. This remains reduced-model evidence, not a PDE theorem.

The `Re_delta -> infinity` branch is also consistent with known full-PDE critical-norm theory: Seregin (2012) proved that if a finite-time blowup occurs, `||u(t)||_L3` must tend to infinity. Under a coherent single-scale interpretation, `Gamma_delta ~ U_delta delta` is the corresponding scale-invariant amplitude. This analogy is not an equivalence for arbitrary flows.

## 9. What remains

The current escape routes for a hypothetical singularity are substantially narrower but still real. A full solution could:

- make the product of scale-critical circulation and normalized strain advantage diverge fast enough to satisfy the local core gate;
- in practice, drive the scale-critical circulation/amplitude unbounded, or continually create a new smaller ruler on which the normalized geometry must be reconsidered;
- continually create new subscales so that no bounded renormalized coherent state exists;
- lose coherent vortex-tube structure through sheets, cancellation, reconnection, or other geometry;
- exploit genuinely nonlocal interactions not captured by the reduced core/filament models.

Accordingly, this repository does **not** establish the Millennium Prize result. Its present analytic target is to determine whether a true finite-energy unforced Navier–Stokes solution can sustain an infinite sequence of renormalization escapes in which the dimensionless quantities required to beat diffusion repeatedly become unbounded.

## 10. Retractions / failed proof routes intentionally retained

Several attractive arguments were explicitly rejected during the run:

- “infinite stages require infinite time” — false because a Zeno sequence can converge in finite time;
- “scale alone makes viscosity win” — false at Navier–Stokes critical scaling;
- “curvature at the target pays for all remote stretching pointwise” — false because the source curvature may live elsewhere;
- “stretching always straightens a vortex pointwise” — false by an explicit local jet;
- “a closed system cannot pass stretching around internally” — false in the four-arc relay model;
- an early `checkpoint_74` shrinking-reach claim — retracted after finding a reach-diagnostic bug and inadequate core resolution.

Preserving these failures is part of the research record.

## 11. Same-tube scale changes do not create larger circulation

At any fixed time, `div omega=0` implies that the vorticity flux through every cross-section of one coherent vortex tube is the same. Therefore merely discovering a smaller geometric ruler inside the same instantaneous tube does not increase `Re_Gamma=Gamma/nu`.

A divergence-free axisymmetric flux-function example in checkpoint 87 numerically preserved unit cross-sectional flux to about `1e-10` while the tube radius varied substantially.

This does **not** imply that a tube's strength is constant in time under viscosity. It means only that spatial renormalization inside the same coherent tube cannot by itself generate the unbounded critical circulation required by the remaining escape route.

## 12. The present budget method admits a formal Type-II escape

Checkpoint 88 stress-tests the remaining mechanism using an abstract circulation-amplifying cascade

\[
\Gamma_n=m^n\Gamma_0,
\qquad
\delta_n=q^n\delta_0.
\]

With the bounded-geometry core floor `a_n^2/delta_n^2 ~ 1/Re_n`, the model gives

\[
\tau_{n+1}/\tau_n=q^2/m,
\qquad
E_{n+1}/E_n\sim m^2q.
\]

Hence there is a nonempty formal window `q<1/m^2` in which the circulation Reynolds number diverges and the relative core thickness vanishes, while the Zeno-time sum and the reduced per-generation energy/dissipation proxy both converge.

This is **not** a Navier–Stokes blowup construction. It is a failed-proof result: energy/core/time scaling alone does not eliminate the final Type-II possibility.

## 13. Stochastic Kelvin backtracking turns circulation growth into an area-distortion requirement

Constantin–Iyer's statistical Kelvin theorem gives

\[
\Gamma_t(C)=\mathbb E\,\Gamma_0(A_t(C)).
\]

For a current loop of scale `delta`, bounded initial vorticity and the area formula imply schematically

\[
\mathbb E K_2
\gtrsim
\frac{|\Gamma_t(C_\delta)|}{\|\omega_0\|_\infty\delta^2},
\]

where `K_2` is the two-dimensional area stretch of the stochastic back-to-label map. Thus a small loop carrying growing circulation must have stochastic preimages with rapidly growing area distortion.

For `Gamma_delta ~ delta^{-p}`, the required mean area stretch grows at least like `delta^{-(2+p)}`. This precisely formalizes the earlier idea of “walking the singularity backward,” but it does not yet produce a contradiction.

## 14. Current stopping point for this proof route

Combining the abstract Type-II cascade with the backward-area gate still leaves a nonempty formal parameter window. For example, `m=2,q=.20` has a reduced stage-cost ratio `.8`, Zeno-time ratio `.02`, and requires a normalized strain impulse of only about `1.956` per generation to meet the uniform backward-area bound.

Therefore the current line of attack has reached a genuine strategic boundary:

> another algebraic scale budget is unlikely to finish the problem. A further advance requires a Navier–Stokes-specific estimate limiting repeated circulation amplification, stochastic back-to-label area distortion, or the normalized strain impulse through an infinite Type-II cascade.

This conclusion is consistent with the rigorous requirement that any genuine finite-time blowup must have `||u(t)||_L3 -> infinity` and with current work on potential Type-II blowup scenarios.

## 15. Circulation amplification is not supplied by ordinary coherent stretching

In the aligned parallel-tube reduction, the vorticity equation takes the conservative form

\[
\partial_t\zeta+\nabla_\perp\cdot(v_\perp\zeta)=\nu\Delta_\perp\zeta,
\]

so the total cross-sectional circulation `Gamma=int zeta dA` is constant for decaying fields even while stretching changes the core radius and peak vorticity. Thus the checkpoint-88 assumption `Gamma_{n+1}=m Gamma_n` is **not** generated by ordinary stretching of one isolated coherent tube.

For a one-sign nested core, `Gamma'(R)=2 pi R zeta(R)>=0`; a smaller nested ruler cannot contain more same-signed circulation at the same instant. In the same coherent reduction, viscosity changes the circulation inside a material radial boundary according to `dGamma_R/dt=2 pi nu R partial_r zeta`. A monotone core therefore loses rather than gains enclosed circulation.

## 16. Kelvin gradient trap

The exact viscous Kelvin law shows that order-one circulation growth on the parent nonlinear time requires

\[
\|\nabla\omega\|\gtrsim\Gamma^2/(\nu\delta^3).
\]

With parent vorticity `Omega~Gamma/delta^2`, the required gradient scale satisfies

\[
\ell_{grad}/\delta\lesssim1/Re_\Gamma.
\]

Its viscous time is shorter than the parent nonlinear time by `~1/Re_Gamma`, and at inherited parent amplitude its own local circulation Reynolds number is only `~1/Re_Gamma`. Promoting this tiny layer into the next high-Re vortex with `Re_next=m Re_parent` requires an additional vorticity-amplitude multiplication `~m Re_parent^2`.

This does not prove impossibility, but it exposes a hidden nested-scale cost in the formal Type-II cascade.

## 17. Merger amplification requires a genuine flux reservoir

If `Gamma` grows by merging/recruiting signed vortex flux rather than by changing one material-loop circulation, the net recruitment telescopes:

\[
\sum \Delta\Gamma=\Gamma_N-\Gamma_0.
\]

Therefore unbounded circulation requires unbounded net signed-flux recruitment; splitting and reusing the same flux cannot multiply it.

Under additional coherent-tube assumptions (isolated donor tubes, comparable low-vorticity gaps, bounded eccentricity, and bounded initial vorticity gradient), a donor of radius `r` has `Gamma=O(r^3)`, so pairwise-disjoint donors in bounded volume have finite total recruitable circulation. The merger-only escape must then abandon isolated-tube geometry and move into a dense cluster/sheet/sign-changing/reconnection regime.

This restriction is conditional. Rigorous Navier-Stokes results allow arbitrarily complicated **finite** vortex reconnection cascades in smooth global solutions, so reconnection itself is not evidence of singularity and cannot be assigned a universal fixed energy toll.

## 18. Updated surviving adversary

The free `Gamma_n=m^n` Type-II toy cascade has been demoted from a plausible one-tube mechanism to a shorthand for a far more difficult process. A genuine realization must either:

- change the circulation of a material lineage through viscosity, which forces `delta/Re` vorticity-gradient layers that diffuse much faster than the parent nonlinear clock; or
- repeatedly recruit new signed flux through mergers/reconnection, requiring an unbounded reservoir and loss of isolated coherent-tube geometry.

The remaining object is therefore a dense, non-isolated, multiscale cluster that simultaneously changes topology, creates ever thinner gradient layers, and boosts vorticity strongly enough to keep those layers at high local Reynolds number.
