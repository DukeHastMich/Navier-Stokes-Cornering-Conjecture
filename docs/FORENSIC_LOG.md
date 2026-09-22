# Forensic Session Log — Navier–Stokes “Failure to Corner” Run

**Date:** 2026-09-21
**Topic:** Unforced 3D Navier–Stokes global regularity; geometric “cannot corner fast enough” intuition; recursive self-containing/ouroboros vortex thought experiment.

## User hypothesis progression

- Viscosity should prevent a fluid field from forming a true singular corner.
- A Gabriel’s-horn-like concentration was proposed as the intuitive pathology to test.
- External/remote strain was identified as a loophole; user noted that this begins to resemble the forced problem locally.
- User proposed a self-interacting vortex to close the forcing loop.
- Geometry was refined repeatedly: not parallel shrinking rings or a planar spiral, but a single pipe/vortex tube feeding back into its own open center — “snake eating itself.”
- Objective clarified: use the most dangerous self-interaction geometry as an adversarial test and try to prove it still cannot reach singularity.

## CHECKPOINT A — exact identities

Derived/used:

- vorticity equation: `D_t ω = Sω + νΔω`
- magnitude/direction decomposition: `ω = Ω ξ`
- exact magnitude equation: `D_t Ω = αΩ + νΔΩ − νΩ|∇ξ|²`, `α=ξ·Sξ`
- enstrophy identity and decomposition `|∇ω|² = |∇Ω|² + Ω²|∇ξ|²`

Interpretation: viscosity directly penalizes directional bending as well as magnitude sharpening.

## CHECKPOINT B — literature anchors

Verified current/primary literature supporting geometric depletion and vortex-line straightening:

- Constantin–Fefferman (1993), DOI 10.1512/iumj.1993.42.42034: sufficient coherence of vorticity direction in intense-vorticity regions prevents blowup.
- Constantin–Procaccia–Segel (1995), DOI 10.1103/PhysRevE.51.3207: stretching tends to straighten vortex lines; derived curvature/torsion equations; well-aligned tubes deplete self-stretching.
- Grujić and related work: localization and weaker directional coherence criteria.
- Bedrossian–Germain–Harrop-Griffiths (2023), DOI 10.1002/cpa.22091: well-posedness for vortex filament data, including arbitrary circulation in important settings.
- Enciso–Lucà–Peralta-Salas (2017), DOI 10.1016/j.aim.2017.01.025: smooth Navier–Stokes solutions can undergo vortex reconnection/topology changes; topology cannot be assumed frozen.

## CHECKPOINT C — straight-filament cancellation

For a straight filament along z,

`u = Γ/(2π(x²+y²)) (-y, x, 0)`.

At closest point `(d,0,0)`, induced velocity has no separation-normal component. Exact symmetric strain matrix:

`S = -Γ/(2πd²) [[0,1,0],[1,0,0],[0,0,0]]`.

Any target tangent orthogonal to the separation normal has `tᵀSt=0`.

Conclusion: leading near-contact singular velocity does not close the gap and leading `1/d²` straight-filament strain does not longitudinally stretch at closest approach.

## CHECKPOINT D — curvature correction

Explicit source curve `X(s)=(0, κs²/2, s)` and target tangent `e_z`.

Symbolic expansion of the Biot–Savart strain to first order in κ produced integrand

`−3 Γ d κ s² / [4π(d²+s²)^(5/2)]`.

Using the exact integral `∫ s²/(d²+s²)^(5/2) ds = 2/(3d²)` over the real line gave

`δα = −Γκ/(2πd)`

for this orientation.

Conclusion: bending breaks the closest-point cancellation at `O(Γκ/d)`, not `O(Γ/d²)`.

## CHECKPOINT E — correction to an invalid step

An attempted pointwise absorption of source curvature into the target’s local viscous term was rejected. Curvature can exist at source y and stretch a locally straight target x. Therefore the needed estimate is nonlocal/two-point/global.

## CHECKPOINT F — scale tests

- self-induced strain ~ `C Γ/R²`
- diffusion rate ~ `ν/a²`
- ratio ~ `C (Γ/ν)(a/R)²`
- thin-filament local induction adds only logarithmic growth, giving `(Γ/ν)(a/R)² log(R/a) -> 0` as `a/R -> 0`

Conclusion: extreme thinning around a nonshrinking loop loses to viscosity.

For exact self-similar shrinkage with fixed `a/R`, nonlinear and viscous rates scale the same way; size alone does not decide.

Infinite stages can occur in finite mathematical time because `Σ q^(2n)` converges. Temporal division alone is not a proof.

## CHECKPOINT G — second-moment/enstrophy lower bound

For nonnegative cross-sectional vorticity f with mass M and second moment width `b=(∫r²f)/(∫f)`, variational minimization gives

`∫f² >= 4M²/(9πb)`.

This quantifies the enstrophy cost of concentrating a coherent one-sign vortex core.

## CHECKPOINT H — affine-core contraction toll

Model equation `b' = -σb + 4ν`.

Eliminate σ and define action `J=∫bσ²dt = ∫(4ν-b')²/b dt`.

Use `(4ν-b')² >= -16ν b'` to obtain

`J >= 16ν ln(b0/b1)`.

Thus every fixed fractional core contraction has a scale-independent minimum strain action in this model.

An anisotropic 2D covariance optimization gave the affine lower bound

`|S|² >= (3/8)(b'-4ν)²/b²`.

Conditional consequence: if each complete recursive lap retains a length bounded below by `L*>0`, and coherent-core assumptions let this local action be charged to global dissipation, each lap has a nonzero energy toll `~ν²L*`; finite energy permits only finitely many laps.

## CHECKPOINT I — surviving loopholes

The argument is not a global proof because a real Navier–Stokes blowup candidate may:

- shrink the entire loop/hole so `L_n -> 0` and the toll sum converges;
- lose coherent one-sign tube structure;
- use strongly anisotropic/sparse cross-sections;
- exploit reconnection;
- transfer curvature cost in one location into stretching benefit at another;
- use non-self-similar/Type-II concentration.

## CHECKPOINT J — strongest current formulation

Working conjecture:

> In finite-energy unforced 3D Navier–Stokes flow, any multiscale self-interaction capable of critical vorticity amplification must generate directional complexity at comparable scales; geometric depletion of the Biot–Savart kernel plus viscous directional diffusion prevents that complexity from retaining sufficient stretching efficiency through an infinite scale hierarchy.

Desired missing estimate:

`∫ αΩ² <= (1-δ)ν∫(|∇Ω|²+Ω²|∇ξ|²) + subcritical/time-integrable remainder`

without assuming coherence as an external hypothesis.

## Status

**No fake proof claimed.**

Result of this session: the user’s intuition survives several meaningful adversarial checks and aligns with established geometric-depletion theory, but the unconditional nonlocal coercive estimate remains open. The fixed-macroscopic-open-center coherent ouroboros class is conditionally obstructed by a scale-independent dissipation toll.

## Artifacts

- `Navier-Stokes_Cornering_Conjecture_RESEARCH_NOTE_2026-09-21.md`
- this forensic log

## CHECKPOINT K — direct commutator attack

Used the exact Constantin directional kernel with the inequality

`Omega(x+h) |xi(x+h)-xi(x)| <= 2 |omega(x+h)-omega(x)|`.

After a near/far split at radius r, Hajlasz/maximal-function control of the near difference and Cauchy-Schwarz control of the far field give

`T_near <= C r W^(1/2) N^(5/2)`

`T_far  <= C r^(-3/2) W^3`

with `W=||omega||_2`, `N=||grad omega||_2`.

Optimizing at `r=W/N` gives

`|T| <= C W^(3/2) N^(3/2)`.

Young then gives the classical supercritical enstrophy ODE `Y' <= C nu^(-3) Y^3`, `Y=W^2`. Conclusion: the naive nonlocal commutator route does not secretly solve the problem; without additional direction coherence it falls back to the standard estimate.

## CHECKPOINT L — static coercive target falsified by scaling

Tested the hoped-for instantaneous inequality `T <= c nu N^2 + F(energy)`.

For energy-preserving concentrations `u_lambda(x)=lambda^(3/2) phi(lambda x)`:

- kinetic energy is fixed,
- `T_lambda = lambda^(9/2) T_0`,
- `N_lambda^2 = lambda^4 N_0^2`.

Therefore `T_lambda/(nu N_lambda^2) ~ lambda^(1/2) -> infinity` for any base field with positive instantaneous enstrophy production.

Conclusion: no universal instantaneous absorption inequality with an energy-only remainder can be the missing proof. The user's phrase “cannot corner fast enough” must be interpreted dynamically, not statically.

## CHECKPOINT M — critical half-Hölder threshold recovered

Assuming `|delta xi| <= H |h|^(1/2)`, HLS gives `alpha <= C H I_(1/2)(Omega)` and therefore

`|T| <= C H W^2 N`.

After Young:

`Y' <= C nu^(-1) H^2 Y^2`.

The energy identity supplies `int_0^T Y dt < infinity`, so bounded/time-controlled H turns this into Gronwall closure. This identifies the exact missing gain: one half spatial power of directional coherence.

## CHECKPOINT N — line curvature gives the half power exactly

For arclength s along a vortex line,

`|xi(s2)-xi(s1)| <= |s2-s1|^(1/2) (int kappa^2 ds)^(1/2)`.

On short segments with small total turning, arclength and Euclidean chord length are comparable, so a uniform linewise `L^2` curvature budget yields local Euclidean `1/2`-Holder direction coherence along the line.

This is the cleanest precise translation so far of “cannot corner fast enough.”

## CHECKPOINT O — exact stretching/straightening curvature skeleton

For the inviscid/stretching part, with `c=(xi·grad)xi`, direct commutator algebra gives

`D_t c = (xi·grad S)xi + S c - (xi·grad alpha)xi - 2 alpha c`.

Therefore

`1/2 D_t kappa^2 = c·(xi·grad S)xi + c·S c - 2 alpha kappa^2`.

If xi is aligned with the most extensive strain eigenvector, the local strain terms are net straightening; curvature must be regenerated by the strain-gradient source `(xi·grad S)xi`.

For a material vortex-line segment in the inviscid skeleton,

`d/dt int kappa^2 ds <= 2 int kappa |grad S| ds - int alpha kappa^2 ds`

schematically in the aligned stretching regime.

Since `grad S` is a Calderon-Zygmund transform of `grad omega`, the dynamic curvature route is still plausible, but converting spatial `L^2` control into uniform linewise curvature control remains unresolved.

## Current status after continuation

No proof claimed. One proposed static proof route has been decisively ruled out by concentration scaling. The surviving route is dynamic: establish that the strain-gradient field cannot regenerate line/tube curvature rapidly enough to destroy the critical 1/2-Holder coherence before stretching/viscosity straightens it.


## CHECKPOINT P — literature cross-check

Established literature was checked against the new target. The critical half-Holder threshold for vorticity-direction coherence is known to imply regularity; Constantin–Procaccia–Segel report dynamic straightening of vortex lines by stretching; Deng–Hou–Yu use vortex-line curvature/length in localized Euler non-blowup criteria; and high-Re DNS literature reports self-attenuation of local stretching in extreme-vorticity regions with dangerous production shifted toward nonlocal strain. These are supporting anchors, not a proof.

## CHECKPOINT Q — exact viscous direction PDE

Derived the full vorticity-direction equation

`xi_t + u·grad xi = F_tan + nu Delta xi + 2nu grad(log Omega)·grad xi + nu |grad xi|^2 xi`

with `F_tan = P_(xi^perp) S xi`.

Noted the divergence form

`Delta xi + 2 grad(log Omega)·grad xi = Omega^(-2) div(Omega^2 grad xi)`.

Moving the cross-diffusion to the transport side gives intrinsic drift `-2nu grad(log Omega)`, always down the vorticity-magnitude gradient. For `Omega = Phi r^(-2)`, the leading drift is the outward field `+4nu x/r^2`.

## CHECKPOINT R — hemisphere barrier

For `theta = 1 - xi·e = |xi-e|^2/2` and

`L = partial_t + (u - 2nu grad log Omega)·grad - nu Delta`,

derived

`L theta = -F_tan·e - nu |grad xi|^2 (1-theta)`.

On a hemisphere (`theta <= 1`) the harmonic-map term is nonpositive. Thus new hemisphere-sized direction defects cannot be manufactured internally from coherent data without tangential strain, incoming irregular boundary data, or loss of the hemisphere/topological regime.

## CHECKPOINT S — finite global budget for direction-rotating strain

Because `|F_tan| <= |S|` and the unforced energy identity gives

`1/2 ||u(t)||_2^2 + 2nu int ||S||_2^2 dt = 1/2 ||u0||_2^2`,

obtained the exact budget

`int int |F_tan|^2 dx dt <= ||u0||_2^2/(4nu)`.

## CHECKPOINT T — codimension cost

For an order-one turn on scale r over diffusive time `tau ~ r^2/nu`, a forcing rate `~nu/r^2` acting on an active set with k macroscopic directions of size L has spacetime L2 cost

`C_k(r) ~ nu L^k r^(1-k)`.

Therefore:
- point-like event: `~nu r` (summable over geometric scales);
- fixed-length filament: `~nu L` (scale-independent per event);
- fixed-area sheet: `~nu L^2/r` (diverges as scale shrinks).

This supplies a more robust explanation of the fixed-open-center ouroboros obstruction, but does not eliminate point concentration.

## CHECKPOINT U — energy cannot force the critical inflow barrier at a point

To beat the outward critical drift `4nu/r`, physical inward relative velocity must be `~nu/r`, requiring strain `~nu/r^2`. In a point ball of volume `r^3`, over time `r^2/nu`, the L2 strain cost is `~nu r`, which is summable. Thus finite energy alone cannot imply the recent critical-core inward-flow condition. In a fixed-length tube the same cost becomes `~nu L` per scale.

## CHECKPOINT V — Landau point-force signature

Cross-checked Šverák's classification of nonzero stationary (-1)-homogeneous 3D Navier-Stokes solutions: they are Landau solutions. Distributionally on all of R3, Landau solutions carry a Dirac point force `b delta_0`.

Interpretation: the canonical stationary critical `u~1/r` point core has the mathematical signature of a point momentum source. This does not rule out dynamical blowup because a singular limit could generate a defect measure, but it rules out treating a stationary critical core as an ordinary globally unforced smooth continuation.

## CHECKPOINT W — self-similar escape also constrained

Reviewed nonexistence results for exact/asymptotically backward self-similar Navier-Stokes blowup under broad stated integrability/convergence hypotheses. General non-self-similar/Type-II and sufficiently general DSS scenarios remain.

## CHECKPOINT X — 2026 Grujic work lands on same obstruction

Two current preprints independently derive/use the same structure: unidirectional Biot-Savart cancellation, logarithmic local-mean-oscillation depletion, the exact HMHF-like direction equation, outward `4nu x/r^2` cross-diffusion at a critical point profile, and hemisphere control. They still require structural hypotheses on inward transport/core history/tangential strain; no unconditional regularity theorem is claimed.

## CHECKPOINT Y — sharp current “cornering” diagnostic

Along a vortex line, an order-one turn on segment length r requires

`r int_segment kappa^2 ds >= c > 0`.

Thus a hypothetical singularity must sustain critical line-curvature concentration `int kappa^2 ds ~ 1/r` on arbitrarily small scales. If this scale-invariant curvature quantity tends to zero in intense-vorticity regions, half-Holder directional coherence follows along lines and the geometric-depletion route becomes available (subject to transverse coherence).

## Status after third continuation

No proof claimed. The fixed-open-center/macroscopic-filament mechanism is increasingly constrained. The remaining loophole is a shrinking, point-like, non-self-similar core that repeatedly supplies critical inward momentum flux and tangential strain while preventing even weak/logarithmic decay of vorticity-direction oscillations. Energy scaling alone does not eliminate that point-core cascade.

## CHECKPOINT Z1 — correction to tangential-strain budget argument

Derived the Bochner identity for `G=|grad xi|^2/2` under the exact direction drift `b=u-2nu grad log Omega`:

`L G = grad xi : grad F_tan - sum (partial_i b_j)(partial_j xi_k)(partial_i xi_k) + nu |grad xi|^4 - nu |grad^2 xi|^2`.

Conclusion: small-scale direction gradients can be generated by drift compression and HMHF gradient dynamics even without direct `F_tan` rotation. Therefore the prior codimension `F_tan` cost is conditional, not a universal per-corner toll.

For the critical radial drift `4nu x/r^2`, `grad b` has radial eigenvalue `-4nu/r^2` and two tangential eigenvalues `+4nu/r^2`; it screens outer data while still being capable of compressing radial direction gradients.

## CHECKPOINT Z2 — explicit curvature-producing local jet

Constructed and symbolically checked the divergence-free polynomial local velocity field

`u1=-s x/2 - Omega0 y/2 + M z^2/2`
`u2= Omega0 x/2 - s y/2 - M x y`
`u3= s z + M x z`.

Exact calculations:

- `div u = 0`
- `curl u = (0,0,Omega0-M y)`
- hence `xi=e_z` exactly in a small neighborhood where `Omega0-My>0`
- at origin `S=diag(-s/2,-s/2,s)`, `alpha=s`, `F_tan=0`
- `(xi.grad S)xi = M e_x` at origin.

Thus the local vortex direction is initially perfectly straight, but the curvature vector `c=(xi.grad)xi` satisfies initially `D_t c = M e_x`. Vorticity magnitude simultaneously obeys `D_t Omega=s Omega0` at the origin. The jet can be realized inside compactly supported smooth divergence-free finite-energy data by cutting off a vector potential, leaving the local derivatives unchanged.

## CHECKPOINT Z3 — critical scaling of local corner generation

With `s~nu/r^2`, `Omega0~nu/r^2`, `M~nu/r^3`, the local event has

- velocity `~nu/r`
- vorticity `~nu/r^2`
- strain-gradient `~nu/r^3`
- diffusive time `~r^2/nu`
- generated curvature `~1/r`
- energy `~nu^2 r`
- one-episode energy dissipation `~nu^2 r`.

Hence a geometric sequence of point-localized critical episodes has summable energy cost. Exact NS scaling gives the stronger statement that a single smooth local corner-generation event can be rescaled to arbitrarily small length, arbitrarily large curvature and arbitrarily small total kinetic energy.

This falsifies the strong local slogan “viscosity cannot corner fast enough.”

## CHECKPOINT Z4 — revised conjecture

The surviving statement is inter-scale rather than local:

`A smooth unforced NS flow can perform one critical cornering/stretching episode, but perhaps cannot self-reproduce such episodes through infinitely many shrinking scales in finite time.`

A positive proof now requires a renormalized scale-to-scale contraction/loss of Biot-Savart stretching efficiency. Fixed or periodic repetition in rescaled variables falls into self-similar/discretely-self-similar classes already constrained by known nonexistence results; a surviving cascade must continually change shape.

## CHECKPOINT Z5 — structural barrier cross-check

Tao's averaged Navier-Stokes blowup result was added as a sanity check: an averaged bilinear nonlinearity can preserve the usual energy cancellation and scaling yet blow up. Thus no argument based only on energy/scaling/generic bilinear estimates can settle true NS; the exact geometric structure of the real nonlinearity must enter.

## Status after fourth continuation

The analysis has reached a sharper boundary. Local critical cornering is demonstrably possible in true unforced smooth NS. What remains open is whether one solution can chain such events into an infinite point-localized non-self-similar cascade. The original intuition survives only in this “failure to sustain” form.

## CHECKPOINT Z6 — user closure insight tested

User observed that if the vortex "corners fast enough" it may close off and cancel at the point. This was tested carefully.

At any fixed smooth time with nonzero vorticity, vortex lines solve `gamma'=xi(gamma)`. Local ODE uniqueness means two vortex lines cannot cross transversely where `omega != 0`; a closed vortex line must return with the same tangent. Therefore an exact smooth closure has zero directional mismatch at the contact. In the Constantin stretching kernel the geometric factor then vanishes, so the bare `1/d^3` self-stretching singularity is depleted at coincidence.

A circular ring illustrates the distinction cleanly: at its geometric center `u_z(0)=Gamma/(2R)` but `du_z/dz(0)=0`; closure does not cancel translation, it cancels the first-order extensional strain at the symmetry center.

Fenchel + Cauchy gives for every smooth closed loop `int kappa^2 ds >= 4 pi^2/L`, so shrinking closure necessarily carries divergent line-curvature energy, though this alone does not contradict NS critical scaling.

## CHECKPOINT Z7 — exact closure is not enough for a proof

A singularity can attempt to synchronize gap collapse, vorticity growth, and loss of direction continuity at the same limiting time. If the gap is `d` and `K=||grad xi||`, leading straight-filament depletion implies critical self-stretching requires `K d = O(1)` or larger. A finite-angle mismatch across gap `d` makes the half-Holder seminorm grow at least like `d^{-1/2}`, precisely the regime that must evade known geometric-coherence criteria.

Thus the self-contact singularity, if any, must be a pre-contact loss of coherence, not a singularity generated by the completed smooth closure.

## CHECKPOINT Z8 — contact trichotomy

1. Smooth contact with `Omega>0`: vortex-line tangent matches and the leading geometric kernel cancels.
2. Contact through `Omega=0`: direction can become undefined and viscous reconnection/topology change can occur smoothly; Enciso-Lucà-Peralta-Salas provide rigorous examples of topology change without loss of regularity.
3. Singular contact: high vorticity and failure of directional coherence occur simultaneously as `d->0`; this is the only remaining self-contact blowup route.

## CHECKPOINT Z9 — gap kinematics and a counterwarning

For material trajectories `h=X-Y`, `d=|h|`, `n=h/d`,

`d'/d = int_0^1 n.S(Y+theta h).n dtheta`.

Finite-time material collision requires divergent accumulated compressive strain. Vortex lines are not material for viscous NS, so diffusion/reconnection can avoid material collision.

Also checked `S=diag(-2a,a,a)`: it compresses the normal gap while every transverse tangent direction is an eigenvector and therefore does not rotate. Thus incompressibility alone does NOT force approaching branches to align before contact. Alignment/cancellation is guaranteed only at an exact smooth nonzero-vorticity contact by uniqueness of the direction field.

## Status after fifth continuation

The user's closure intuition is valid as an endpoint obstruction: completed smooth self-closure cannot retain a finite-angle vortex corner and the leading Biot-Savart singular geometry cancels there. It does not yet rule out a singularity that occurs in the approach, with direction coherence breaking at the same time as the gap collapses. The remaining self-contact demon must therefore arrange simultaneous `d->0`, high-vorticity amplification, and failure of at least half-Holder directional coherence before viscosity/reconnection resolves the contact.

## CHECKPOINT Z10 — first-order general near-contact geometry

Generalized the curved-source calculation.  In coordinates with source tangent `t2=e_z`, separation normal `n=e_x`, source curve

`X(s)=(kn s^2/2, kb s^2/2, s)`,

and target tangent `t1=(0,sin(theta),cos(theta))`, symbolic expansion gives, after symmetric integration,

`alpha_(2->1) = Gamma kb (3 sin^2(theta)-2)/(4 pi d) + O(kappa^2)`.

The straight term and the first-order `kn` term integrate to zero.  Only the curvature component `kb = kappa.(t x n)` survives at first order.  The sign changes at `theta=asin(sqrt(2/3))=54.735610... degrees`.

The same curvature component gives finite-window normal velocity

`u.n = -(Gamma kb/(4 pi)) Q(L/d)`,

`Q(z)=asinh(z)-z/sqrt(1+z^2)>0`.

Therefore for sufficiently aligned branches (`theta<54.7 deg`), the curvature sign that drives the target toward the source gives negative longitudinal stretching at the target.

## CHECKPOINT Z11 — aligned pair closure-depletion law

For two nearly parallel same-sign branches with global `b=t x n` and `ki=kappai.b`, the local first-order model gives

`d_dot = Gamma Q(L/d)(k1-k2)/(4 pi)`

and

`alpha1+alpha2 = Gamma(k1-k2)/(2 pi d)`.

Hence

`alpha1+alpha2 = 2 d_dot/[d Q(L/d)]`.

Thus local mutual gap closure (`d_dot<0`) implies negative pair-summed longitudinal stretching.  Exact smooth closure also drives `k1-k2 -> 0`, killing the leading local approach and stretching together.

Ignoring remote and viscous terms, the local pair contribution obeys

`d/dt log(Omega1 Omega2) = 2 d_dot/[d Q] < 0`.

For `d << L`, this integrates asymptotically to a product depletion like `Omega1 Omega2 ~ const/[log(C/d)]^2`.

This does not prevent one branch from growing while the other shrinks more strongly.

## CHECKPOINT Z12 — magnitude asymmetry requires vortex-line divergence geometry

From `div omega=0`, `omega=Omega xi`, along a vortex line

`d_s log Omega = -div xi`.

Hence

`Omega(s2)/Omega(s1)=exp(-int div xi ds)`.

A strategy where one near-contact branch becomes arbitrarily stronger than its mate therefore requires unbounded integrated `div xi` along the connecting coherent vortex-line segment, unless coherence is destroyed by reconnection/zero vorticity.  Around a smooth closed nonzero-vorticity line, `oint div xi ds=0` exactly.

This matches the geometric quantities appearing in the Deng-Hou-Yu localized Euler nonblowup criteria.

## CHECKPOINT Z13 — far-field pusher dissipation lower bound

For strain generated only by vorticity farther than radius R,

`|S_>R(x,t)| <= C R^(-3/2) ||omega(t)||_2`.

Over interval length tau,

`int |S_>R| dt <= C R^(-3/2) tau^(1/2) (int ||omega||_2^2 dt)^(1/2)`.

Therefore an order-one accumulated remote stretching impulse costs energy dissipation at least

`E_diss >= c nu R^3/tau`.

For a parabolic scale-d episode `tau ~ d^2/nu`,

`E_diss >= c nu^2 R^3/d^2`.

A fixed macroscopic pusher is impossible as d->0.  For geometric d_n and `R_n ~ d_n^alpha`, finite total dissipation requires at least `alpha>2/3` to evade this estimate.  The strain source must follow the target down the scale hierarchy.

## CHECKPOINT Z14 — CKN sanity check

Caffarelli-Kohn-Nirenberg epsilon regularity uses scale-invariant local dissipation of the form `(1/r) int_{Q_r}|grad u|^2`.  This confirms why the repeatedly obtained point-scale physical dissipation cost `~nu^2 r` is critical and summable across geometric radii: it is exactly the scale at which partial regularity theory does not automatically rule out a singular point.

## Status after sixth continuation

The literal near-aligned self-closing pair is more strongly depleted than previously established: in the local first-order Biot-Savart asymptotic, gap-closing mutual motion has negative pair-summed longitudinal stretching.  A singular cascade therefore needs positive amplification imported from other geometry.  Global energy forces that amplifier geometry to descend toward zero scale as well; a fixed coarse-scale source cannot drive arbitrarily small critical events.

The remaining candidate is an increasingly compact multibranch cluster, not a self-sufficient two-branch ouroboros closure.

Verification artifacts: `checkpoint_52_pair_contact_verify.py`, `checkpoint_52_pair_contact_verify.txt`.

## CHECKPOINT Z15 — closed multi-segment relay test

User requested the strongest direct test of a closed system "vortex chasing its own tail" with multiple internally outsourcing segments.

### Three-segment closure

For a three-edge single closed polygon, edge vectors satisfy `q1+q2+q3=0`, so the geometry is planar. In the point-element Biot–Savart longitudinal-stretch formula the relevant scalar triple product therefore vanishes. A genuinely 3-D single-loop relay requires at least four edges/arcs.

### Smooth four-arc closed filament

Constructed one smooth nonplanar closed Fourier filament, divided it into four material arcs, and evolved it with a regularized full nonlocal Biot–Savart filament kernel. Searched for a state with all four cyclic arc-to-arc stretch contributions positive while global radius of gyration contracts.

Found such a state. Initial cyclic rates:

`[0.04430088, 0.04022682, 0.06687026, 0.05891911]`

with `d(Rg^2)/dt = -0.14597584`.

Therefore a strict claim that a closed system cannot transiently outsource positive stretching around a cycle is false.

The same state was integrated at `N=80`, core `a=0.15`, `dt=0.01`. All four cyclic links remained positive while contraction persisted until `t≈1.21`; then `d(Rg^2)/dt` crossed positive while all four cyclic stretch rates were still positive. Over the valid interval `L/Rg` rose by ~20.4%; integrated cyclic gains were only about `[1.0403, 1.0667, 1.0957, 1.0680]`.

Interpretation: the relay exists, but in this adversarial low-mode example it self-detunes into geometric complexity/expansion before accumulating large gain.

Artifacts:
- `checkpoint_60_closed_relay_test.py`
- `checkpoint_60_closed_relay_test.txt`
- `checkpoint_60_closed_relay_trace.csv`

## CHECKPOINT Z16 — literature adversarial check

Pelz (Phys. Rev. E 55, 1997) found a locally self-similar finite-time collapse in a high-symmetry vortex-filament model using six closed vortex contours. Kimura studied related 3-D straight-filament self-similar collapse. Thus centerline-only closed internal collapse is possible in reduced filament models and cannot be dismissed by topology/sign arguments alone.

Hormoz & Brenner (JFM 707, 2012) then analyzed finite-core self-consistency and argued that interacting filament collapse cannot maintain singular stretching: centerline/separation geometry collapses faster than the physical vortex core shrinks, so the filament approximation fails; their self-similar argument is stated to generalize to multiple filaments and they also develop a non-self-similar extension. This strongly supports the refined `failure-to-sustain` mechanism but is not an unconditional Navier-Stokes theorem.

## CHECKPOINT Z17 — impulse constraint

Hydrodynamic impulse is conserved for localized unforced viscous flow. A critical scale-r point core contributes only `I_r ~ nu r^2 -> 0`; therefore a concentrating core cannot keep a finite fraction of nonzero global impulse. Outer flow must retain it, while earlier remote-strain estimates show a fixed coarse outer pusher cannot drive arbitrarily small critical events. The terminal active cluster is therefore pushed toward a low-impulse/multipolar structure with its strain sources descending alongside the core.

## Status after seventh continuation

The multi-segment closed-system loophole is real transiently. The project cannot claim "internal outsourcing is impossible." The stronger surviving statement is that the relay may be unable to sustain itself through infinitely many shrinking scales while a finite viscous core remains self-consistent. The next adversarial target is a scale-changing multipolar relay, not a fixed finite loop.

## CHECKPOINT K — Finite-core relay run (2026-09-22)

User requested a status-checkpointed continuation of the finite-core attack.

### Coupled four-arc test

Augmented the prior closed four-arc regularized Biot–Savart relay with arcwise core widths `b_j=a_j^2` obeying

`b_j' = -sigma_j b_j + 4 nu`,

where `sigma_j` is the arc-averaged total longitudinal stretch. Each source arc uses its instantaneous `sqrt(b_j)` as its regularization radius. This is explicitly a reduced coherent-core model, not Navier–Stokes DNS.

Sweep: `Re_Gamma = infinity, 10000, 4000, 1000, 100` with initial `a/Rg=0.15`.

Observed: cyclic positive stretching plus global contraction remains transient for all runs. At `Re_Gamma=4000`, minimum `Rg^2≈0.91847` at `t≈1.115`, with `a/Rg≈(0.1458,0.1647,0.1531,0.1439)`. At `Re_Gamma=100`, relative core thickness grows beyond `0.25` before contraction stalls.

Artifacts: `checkpoint_66_finite_core_relay.py`, `.txt`, and per-Re trace CSVs.

### Exact ratio model

For comparable-scale collapse

`R^2dot=-2 c_g Gamma`, `sigma=c_s Gamma/R^2`, `bdot=-sigma b+4nu`, `y=b/R^2`, `tau=-log(R^2/R0^2)`:

`dy/dtau = 2nu/(c_g Gamma) + (1-c_s/(2c_g)) y`.

If `c_s<=2c_g`, `y` grows. If `c_s>2c_g`, `y` tends the positive floor

`y*=4nu/[(c_s-2c_g)Gamma]`.

Thus at finite `Gamma/nu`, a comparable-scale viscous relay cannot have `a/R -> 0`.

### Conditional no-slenderness lemma

If a coherent core satisfies `bdot >= -sigma b + c_nu nu` and self-generated strain is bounded by `sigma <= C Gamma/R^2` with bounded dimensionless `C`, then any shrinking core obeys

`(a/R)^2 > (c_nu/C)(nu/Gamma)`.

Escape requires `C->infinity`, `Gamma/nu->infinity`, loss of coherent-core structure, or loss of contraction. Ordinary Navier–Stokes scaling preserves circulation and hence `Gamma/nu`; shrinking alone does not supply the second escape.

### Current verdict

The fixed-shape / bounded-geometry finite-core closed relay is conditionally eliminated as an asymptotically slender terminal singularity mechanism. The remaining candidate is Type-II/non-self-similar: unbounded dimensionless geometry, proliferating subscales/branches, reconnection, or loss of the coherent-core description.

No global regularity proof claimed.

## CHECKPOINT K — Z-space / temporal structure run (71–77)

- Derived normalized shape dynamics for a scale-homogeneous closed filament: `Y_s = V(Y)-mean(V)-rho Y`, with `d log R/ds = rho`.
- Interpreted fixed points as continuous self-similarity, periodic log-time orbits as discrete self-similarity, bounded recurrent states as compact renormalized dynamics, and unbounded states as requiring a new diverging dimensionless variable.
- Ran the optimized four-arc relay in normalized Z-space to `s=30` at relative regularization eps=0.15. It did not converge or show credible recurrence; rho became positive and stayed positive in the latter half. Normalized length grew from ~10.34 to ~40–50.
- Repeated with thinner relative cores eps=0.01–0.035. First loss of global contraction occurred robustly near s~0.675 before coherent-core overlap for the thinnest cases.
- Extended eps=0.01 to s=5. Global contraction stayed mostly lost, while local geometric reach developed intermittent much smaller scales (down to ~0.004 in Rg=1 units). This shows the toy orbit escapes by generating a smaller local scale rather than by finding a global collapsing cycle.
- Derived generalized coherent-core ratio equation in scale time: `y_s + (sigma_hat+2 rho)y = c_nu/Re_Gamma`. If the normalized coefficient is bounded above, comparison gives a positive lower bound on y=a^2/R^2. Therefore no bounded fixed/periodic/quasiperiodic/chaotic coherent-tube Z-state can make a/R->0 at finite Re_Gamma; escape requires unbounded normalized strain or loss of the coherent-core model.
- Connected to full Navier–Stokes endpoint theory: bounded L^infinity_t L^3_x implies regularity (Escauriaza-Seregin-Sverak). Therefore a genuine singularity must escape every bounded renormalized state controlling the critical L3 norm; periodicity is not required to rule out bounded Z dynamics.
- Revised next target: renormalize on local reach/separation delta(t), not global Rg, and identify which critical scale-invariant quantity must diverge there.

Status: no proof. Stronger conclusion: **bounded/repeatable renormalized mechanisms are not the remaining problem; any surviving blowup must be unbounded in a critical normalized variable and continually generate new subscales.**

## CHECKPOINTS 78–83 — 2026-09-22 corrected local-scale run

### Correction discovered
A code audit found an indentation/early-return bug in the checkpoint-74 `reach()` diagnostic. Neighbor exclusion was applied completely only around the first vertex before the minimum pair distance was evaluated. Therefore the previously highlighted very small local-reach values from that file are not trustworthy. The `eps=0.01, N=80` run was also under-resolved relative to its core. Prior small-reach interpretation was explicitly retracted rather than preserved as a conclusion.

### Corrected convergence test
A repaired reach routine, excluding arclength neighbors around every vertex, was run at N=80/120/160. The old thin-core trajectory showed strong resolution dependence, confirming lack of convergence.

### Reach-safe relay search
A deterministic search over low Fourier-mode closed curves produced hundreds of initial states with four positive cyclic stretching links and simultaneous global contraction. A candidate with reach about 0.10 was selected so that a numerically resolved finite core could fit inside the geometry.

### Better-resolved relay
For N=256, core=0.05, the candidate began with rho=-0.0152742, all cyclic rates positive (minimum about 0.0289842), reach=0.100843, and spacing=0.0409143. The relay/global-contraction condition failed at s=0.450, while reach had increased to ~0.142195 and remained well above core. Core/reach overlap occurred only much later, after the relay had already ceased collapsing.

### Core/resolution sweep
N=256/core=.05 -> failure s=.450; N=320/core=.04 -> .435; N=384/core=.03 -> .375. In all cases reach at failure was much larger than core. No tested thinner-core refinement revealed a sustained collapsing relay.

### Local-scale gate derivation
For local geometric scale delta and core width b=a^2, from b_dot >= -sigma b + c_nu nu and y=b/delta^2:

`y_dot >= c_nu nu/delta^2 + (2 gamma - sigma)y`, `gamma=-delta_dot/delta`.

With local scale-time `ds/dt=Gamma_delta/delta^2`, this becomes

`dy/ds >= c_nu/Re_delta - A_delta y`,

`Re_delta=Gamma_delta/nu`, `A_delta=(sigma-2 gamma)delta^2/Gamma_delta`.

If both Re_delta and A_delta remain bounded above through an infinite coherent cascade, y cannot tend to zero. Remaining coherent-tube escape requires Re_delta -> infinity or A_delta -> infinity. Otherwise the coherent-tube reduction must fail.

### Status
No global regularity proof. Corrected numerical evidence is stronger than the superseded thin-core reach claim: the better-resolved closed relay loses collapse before core contact. The next target is an unbounded Type-II critical variable, not periodicity.

### New artifacts
- `checkpoint_78_reach_convergence.py/.txt` and N-resolution CSVs
- `checkpoint_79_initial_geometry_scan.csv`
- `checkpoint_80_geometry_search.py/.txt` + candidate coefficients
- `checkpoint_81_resolved_zrelay.py/.txt/.csv`
- `checkpoint_82_resolved_core_sweep.csv/.txt`
- `checkpoint_78_83_STATUS.md`

## CHECKPOINTS 84–86 — escape-variable reduction (2026-09-22)

### Analytic gate
Starting from `y_s >= c_nu/Re_delta - A_delta y`, observed that whenever the relative core ratio `y=a^2/delta^2` is nonincreasing, a necessary condition is

`A_delta Re_delta y >= c_nu`.

Therefore `A_delta` and `Re_delta` are not independent escape variables. If `y -> 0` while continuing to decrease, their product must diverge at least like `1/y`. Equivalent physical form:

`(sigma - 2 gamma) a^2 / nu >= c_nu`.

### Remote pusher
For schematic source strain `sigma <= C Gamma_s/d^2`, the core gate yields

`Re_s >= (c_nu/C)(d/a)^2`.

Thus a pusher that remains at the outer scale while `a/delta -> 0` needs diverging scale-critical circulation. If it approaches to `d=O(a)`, it has generated a new active scale and the renormalization must restart there.

### Critical norm connection
Under a coherent single-scale heuristic `U_delta ~ Gamma_delta/delta`, local `L3` size is `~Gamma_delta`. This was explicitly marked as heuristic. Literature check: Seregin 2012 rigorously proves that a finite-time 3-D Navier-Stokes blowup requires `||u(t)||_L3 -> infinity` (CMP 312, DOI 10.1007/s00220-011-1391-x; arXiv:1104.3615). Recent Type-II anchor: Seregin arXiv:2606.29468 (2026).

### Numerical gate instrumentation
Added `checkpoint_84_escape_gate.py` and a resolution/core sweep `checkpoint_86_escape_gate_sweep.py` on the corrected reach-safe relay. Reconstructed physical local reach shrink in normalized time and compared stretching available:
- exactly at the point/pair defining reach,
- within two reach lengths,
- globally on the loop.

The local controller typically has a poorer strain balance; allowing nonlocal stretching substantially improves the gate. This directly exhibits the internal-outsourcing loophole rather than removing it.

For N/core `(256,.05)`, `(320,.04)`, `(384,.03)`, relay failure occurred at approximately `s=.4425,.4275,.3675`. In the illustrative `c_nu=4` core overlay, the median Reynolds number required by the best stretch within `2 delta`, restricted to times of physical local shrink before relay failure, was about `4511, 5850, 5462`.

These values are model diagnostics only, not physical threshold predictions. The distance from the active ruler to the global maximum stretching point was not converged across resolution and is not retained as a theorem-like conclusion.

### Status
No proof claimed. The remaining coherent mechanism has been reduced to either unbounded critical amplitude/circulation, repeated creation of a smaller ruler, or loss of coherent-tube geometry. This is essentially the Type-II/unbounded-critical-norm boundary of the open PDE problem.

Artifacts:
- `src/checkpoint_84_escape_gate.py`
- `src/checkpoint_85_escape_scaling.py`
- `src/checkpoint_86_escape_gate_sweep.py`
- corresponding CSV/text outputs
- `docs/checkpoints/checkpoint_84_86_STATUS.md`

## CHECKPOINTS 87–90 — same-tube flux, abstract Type-II escape, stochastic Kelvin backtracking

### Same-tube flux inheritance
Used the exact kinematic fact `div omega=0`: an instantaneous coherent vortex tube has the same vorticity flux/circulation through every cross-section. Built a divergence-free axisymmetric flux-function example with varying radius; numerical cross-sectional flux remained `1` to ~`1e-10`.

Consequence: choosing a smaller ruler inside the same coherent instantaneous tube does not by itself increase `Re_Gamma=Gamma/nu`. Critical-amplitude growth between generations must come from time-dependent tube-strength change, aggregation of other flux, or failure of coherent-tube identity.

### Abstract Type-II adversary
Stress-tested the remaining budgets with `Gamma_n=m^n`, `delta_n=q^n`, and bounded-geometry core floor `y_n~1/Re_n`. Derived:
- relative core ratio `a_n/delta_n ~ m^{-n/2}`;
- nonlinear time ratio `q^2/m`;
- model stage energy/dissipation ratio `m^2 q`.

Found a nonempty formal finite-budget window `q<1/m^2`. Example `m=2,q=.20`: Gamma doubles, relative core thins by `sqrt(2)`, time ratio `.02`, stage-cost ratio `.8`. This is not an NSE construction; it demonstrates that existing scale/core/energy budgets do not themselves contradict an unbounded Type-II cascade.

### Stochastic Kelvin backtracking
Literature check verified Constantin–Iyer statistical Kelvin formula `circulation_t(C)=E[circulation_0(A_t(C))]`. Combining it with Stokes and the area formula yields the necessary schematic gate `E[K2] >= Gamma_delta/(||omega_0||_inf * C delta^2)` for the stochastic back-to-label 2-area distortion.

For `Gamma_delta~delta^{-p}`, required mean area distortion grows like `delta^{-(2+p)}`. For an `m`-fold circulation increase and scale ratio `q`, per-generation area amplification must be at least `m/q^2`, corresponding under a uniform strain bound to `I >= .5 log(m/q^2)`.

### Combined consistency sweep
Combined finite model dissipation, finite Zeno time, and backward-area impulse. A nonempty formal window remains for finite order-one-to-few normalized strain impulse. Example `m=2,q=.20` requires `I>=1.956` while retaining cost ratio `.8` and time ratio `.02`.

### Status correction / strategic boundary
No proof claimed. The run identified an honest limitation of the current program: algebraic budget gates alone can be satisfied by a circulation-amplifying Type-II scaling. Further progress needs a new PDE-specific estimate controlling repeated circulation amplification, back-to-label area distortion, or normalized strain impulse. Continuing to stack only dimensional inequalities would reparameterize rather than solve the known Type-II difficulty.

Artifacts:
- `src/checkpoint_87_vortex_flux_inheritance.py`
- `src/checkpoint_88_typeII_merger_cascade.py`
- `src/checkpoint_89_stochastic_kelvin_gate.py`
- `src/checkpoint_90_cascade_consistency.py`
- corresponding text/CSV outputs
- `docs/checkpoints/checkpoint_87_90_STATUS.md`
