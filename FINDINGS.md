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

## 8. What remains

The current escape routes for a hypothetical singularity are substantially narrower but still real. A full solution could:

- make a scale-critical effective circulation Reynolds number unbounded;
- make the normalized strain advantage unbounded;
- continually create new subscales so that no bounded renormalized coherent state exists;
- lose coherent vortex-tube structure through sheets, cancellation, reconnection, or other geometry;
- exploit genuinely nonlocal interactions not captured by the reduced core/filament models.

Accordingly, this repository does **not** establish the Millennium Prize result. Its present analytic target is to determine whether a true finite-energy unforced Navier–Stokes solution can sustain an infinite sequence of renormalization escapes in which the dimensionless quantities required to beat diffusion repeatedly become unbounded.

## 9. Retractions / failed proof routes intentionally retained

Several attractive arguments were explicitly rejected during the run:

- “infinite stages require infinite time” — false because a Zeno sequence can converge in finite time;
- “scale alone makes viscosity win” — false at Navier–Stokes critical scaling;
- “curvature at the target pays for all remote stretching pointwise” — false because the source curvature may live elsewhere;
- “stretching always straightens a vortex pointwise” — false by an explicit local jet;
- “a closed system cannot pass stretching around internally” — false in the four-arc relay model;
- an early `checkpoint_74` shrinking-reach claim — retracted after finding a reach-diagnostic bug and inadequate core resolution.

Preserving these failures is part of the research record.
