# Failure to Corner
## A checkpointed research note on geometric regularization, self-interaction, and the 3D unforced Navier–Stokes problem

**Date:** 2026-09-21
**Status:** NOT A PROOF OF GLOBAL REGULARITY. This file records a serious attempt to turn the informal intuition “a viscous vortex cannot corner fast enough to reach a singularity” into precise mathematical statements, stress-test them, and identify the surviving gap.

---

## Executive status

The working conjecture began as:

> A finite-energy, unforced 3D viscous flow cannot drive a smooth vortex geometry through an infinite sequence of progressively sharper turns quickly enough to produce a finite-time singularity, because either (i) the vorticity direction remains coherent and vortex stretching is geometrically depleted, or (ii) the direction bends rapidly and viscosity penalizes that bending.

That intuition is **not proved**. However, several parts survive exact calculation:

1. The vorticity-magnitude equation contains an exact directional-dissipation term \(-\nu |\omega||\nabla \xi|^2\).
2. The exact Biot–Savart stretching kernel is geometrically depleted when vorticity directions align.
3. Two locally straight vortex segments at closest approach have a leading \(1/d\) induced velocity that is transverse to their separation and a leading \(1/d^2\) strain that gives **zero longitudinal stretching** at the closest point.
4. Curvature breaks that cancellation only at the weaker scale \(O(\Gamma\kappa/d)\) in an explicit local calculation.
5. A thin vortex whose core shrinks much faster than its radius loses to viscosity: the self-induction/diffusion ratio scales like \((a/R)^2\log(R/a)\to0\).
6. Exact backward self-similar collapse of the simplest Leray type is already excluded in broad finite-energy/integrability classes.
7. A fixed-macroscopic-open-center recursive vortex-tube model admits a **scale-independent dissipation toll per fixed fractional core contraction**. Under coherent-core assumptions, infinitely many such complete laps are incompatible with finite energy.
8. The remaining loophole is genuinely nonlocal and multiscale: curved regions can strain remote, locally straight regions, so a pointwise “curvature cost beats stretching” estimate is false. A full proof would need a global/two-point coercive estimate tying nonlocal Biot–Savart stretching back to the viscous cost of generating the required directional geometry.

The strongest honest conclusion is therefore:

> The “cannot corner fast enough” idea is mathematically aligned with known geometric-depletion mechanisms, and it kills several natural self-collapse scenarios, but it has not yet been promoted to an unconditional a priori estimate for arbitrary smooth finite-energy 3D Navier–Stokes solutions.

---

# CHECKPOINT 0 — Exact equations and what must blow up

For the unforced incompressible Navier–Stokes equations on \(\mathbb R^3\),

\[
\partial_t u+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,
\qquad \nabla\cdot u=0,
\]

let

\[
\omega=\nabla\times u,
\qquad
S=\frac12(\nabla u+\nabla u^T).
\]

Then

\[
D_t\omega=S\omega+\nu\Delta\omega,
\qquad D_t=\partial_t+u\cdot\nabla.
\]

Write

\[
\omega=\Omega\xi,
\qquad \Omega=|\omega|,
\qquad |\xi|=1.
\]

On the set \(\Omega>0\), the exact magnitude equation is

\[
\boxed{
D_t\Omega
=
\alpha\Omega+\nu\Delta\Omega-\nu\Omega|\nabla\xi|^2,
}
\]

with

\[
\alpha=\xi\cdot S\xi.
\]

This gives the first precise version of “cornering costs viscosity”:

\[
\boxed{-\nu\Omega|\nabla\xi|^2}
\]

is an exact sink in the vorticity-magnitude equation.

The enstrophy identity is

\[
\frac12\frac{d}{dt}\|\omega\|_2^2
+
\nu\|\nabla\omega\|_2^2
=
\int \alpha\Omega^2\,dx,
\]

and because \(\xi\cdot\partial_j\xi=0\),

\[
\boxed{
|\nabla\omega|^2
=|\nabla\Omega|^2+\Omega^2|\nabla\xi|^2.
}
\]

Thus viscosity separately charges both magnitude sharpening and directional bending.

A continuation criterion of Beale–Kato–Majda type says a finite-time loss of smoothness requires loss of sufficiently strong vorticity control; in particular, if \(\int_0^T\|\omega(t)\|_\infty dt<\infty\), the smooth solution continues.

### Callout

The goal is therefore not to show “real fluids have molecules.” The mathematical target is to prevent \(\Omega\), its critical norms, or derivatives of \(u\) from becoming singular inside the continuum PDE itself.

---

# CHECKPOINT 1 — Known geometric depletion already supports the intuition

The stretching factor \(\alpha=\xi\cdot S\xi\) has an exact singular-integral representation of the schematic form

\[
\alpha(x)
=
\frac{3}{4\pi}\operatorname{PV}
\int
D(\hat y,\xi(x+y),\xi(x))
\frac{\Omega(x+y)}{|y|^3}\,dy,
\]

where

\[
D(e_1,e_2,e_3)
=(e_1\cdot e_3)\det(e_1,e_2,e_3),
\]

and

\[
|D|\le |\sin\phi|
\]

with \(\phi\) the angle between the two vorticity directions.

This is the geometric-depletion mechanism developed by Constantin and Fefferman. Sufficient coherence of \(\xi\) in high-vorticity regions prevents singularity formation. Later work weakened the required directional regularity substantially, including critical/Hölder-type criteria.

Constantin, Procaccia, and Segel also derived curvature/torsion dynamics and found that stretching which amplifies vorticity tends to straighten vortex lines. That is extremely close in spirit to the working intuition:

> if the tube stays aligned, stretching depletes; if it bends strongly, viscosity sees the bend.

But this is a conditional regularity mechanism, not yet an automatic theorem applying to all solutions.

---

# CHECKPOINT 2 — Straight near-self-contact: the leading singular interaction cancels

Take an infinite straight vortex filament along the \(z\)-axis with circulation \(\Gamma\). Its velocity is

\[
u(x,y)=\frac{\Gamma}{2\pi(x^2+y^2)}(-y,x,0).
\]

At the point \((d,0,0)\),

\[
u=\left(0,\frac{\Gamma}{2\pi d},0\right).
\]

Let \(n=(1,0,0)\) denote the closest-separation direction. Then

\[
\boxed{u\cdot n=0.}
\]

So the leading \(1/d\) induced velocity is sideways; it does not close the gap.

The strain tensor at \((d,0,0)\) is

\[
S=-\frac{\Gamma}{2\pi d^2}
\begin{pmatrix}
0&1&0\\
1&0&0\\
0&0&0
\end{pmatrix}.
\]

At a closest pair of points on two smooth curves, the target tangent \(t\) is orthogonal to \(n\), so \(t=(0,a,b)\). Therefore

\[
\boxed{t^TSt=0.}
\]

Hence the leading \(1/d^2\) near-contact strain does not longitudinally stretch the locally straight target filament at the closest point.

### Callout

The most singular straight-filament interaction is geometrically the wrong kind of motion for producing the feared collapse.

---

# CHECKPOINT 3 — Bending breaks the cancellation, but only at \(O(\Gamma\kappa/d)\)

To test the first curvature correction explicitly, take a source filament

\[
X(s)=\left(0,\frac{\kappa s^2}{2},s\right),
\]

with target point \((d,0,0)\) and target tangent \(e_z\).

Expanding the Biot–Savart strain to first order in \(\kappa\) gives the axial stretching integrand

\[
-\frac{3\Gamma d\kappa s^2}
{4\pi(d^2+s^2)^{5/2}}.
\]

Using

\[
\int_{-\infty}^{\infty}
\frac{s^2}{(d^2+s^2)^{5/2}}\,ds
=
\frac{2}{3d^2},
\]

one obtains for this orientation

\[
\boxed{
\delta\alpha
\sim
-\frac{\Gamma\kappa}{2\pi d}.
}
\]

The sign and coefficient depend on geometry, and some orientations cancel even at first order, but the scaling is the important point:

\[
\boxed{
\alpha_{\rm bend}=O\!\left(\frac{\Gamma\kappa}{d}\right),
}
\]

not \(O(\Gamma/d^2)\).

Therefore the near-contact mechanism needs

\[
\kappa d=O(1)
\]

or worse to recover a critical \(1/d^2\)-type stretching rate.

In ordinary language:

> as the separation collapses, the vortex has to bend on essentially the same collapsing scale.

That is a precise mathematical version of “it has to corner as fast as it closes.”

---

# CHECKPOINT 4 — Important correction: the curvature bill is nonlocal

A tempting but incorrect step would be

\[
\alpha(x)
\lesssim
\frac{\Gamma\kappa(x)}{d}
\]

followed by absorption into the local viscous penalty

\[
-\nu\Omega(x)|\nabla\xi(x)|^2.
\]

This is not generally valid.

The curvature that breaks the Biot–Savart cancellation may live at the **source** point \(y\), while the stretched target point \(x\) is locally straight:

\[
\kappa(y)\gg0,
\qquad
\kappa(x)\approx0.
\]

Thus a curved region can pay the geometry bill in one place and generate stretching somewhere else.

### Surviving proof target

A successful argument must be global/two-point. It needs an estimate that makes the source geometry pay for the remote stretching it creates, schematically

\[
\int \Omega(x)^2
\int K(x,y)\,\mathcal G(\xi(x),\xi(y))\Omega(y)\,dy\,dx
\]

controlled by global viscous terms such as

\[
\nu\int\left(|\nabla\Omega|^2+\Omega^2|\nabla\xi|^2\right)dx
\]

plus a genuinely subcritical remainder.

This is the central unresolved operator estimate in this research line.

---

# CHECKPOINT 5 — Scale analysis of the ouroboros vortex

Let

\[
R=\text{loop scale},\qquad
 a=\text{core radius},\qquad
\Gamma=\text{circulation}.
\]

A characteristic self-induced strain has the form

\[
\sigma_{\rm self}\sim C_{\rm geom}\frac{\Gamma}{R^2}.
\]

Viscous core diffusion acts at rate

\[
\sigma_\nu\sim\frac{\nu}{a^2}.
\]

Thus

\[
\boxed{
\frac{\sigma_{\rm self}}{\sigma_\nu}
\sim
C_{\rm geom}\frac{\Gamma}{\nu}
\left(\frac aR\right)^2.
}
\]

For thin curved filaments, self-induction gains only a logarithmic factor, so

\[
\frac{\sigma_{\rm self}}{\sigma_\nu}
\sim
\frac{\Gamma}{\nu}
\left(\frac aR\right)^2
\log\frac Ra.
\]

Therefore

\[
\boxed{
\frac aR\to0
\quad\Longrightarrow\quad
\frac{\sigma_{\rm self}}{\sigma_\nu}\to0.
}
\]

An ever-thinner thread around a nonvanishing loop does not win by becoming thin. Viscosity eventually dominates the ordinary curvature-driven self-induction.

However, if \(a/R\) stays constant, both rates scale like \(R^{-2}\), and scale alone does not decide the contest.

---

# CHECKPOINT 6 — Zeno timing does not by itself prevent blowup

Suppose a self-similar sequence has

\[
R_n=q^nR_0,
\qquad 0<q<1,
\]

and nonlinear time scale

\[
\tau_n\sim \frac{R_n^2}{C\Gamma}.
\]

Then

\[
\sum_{n=0}^{\infty}\tau_n
\sim
\frac{R_0^2}{C\Gamma}
\sum q^{2n}
<\infty.
\]

Therefore “it would require infinitely many stages” is not a proof. A continuum PDE can fit an infinite scale cascade into finite time.

This explicitly kills the naive temporal-division objection by itself.

---

# CHECKPOINT 7 — Exact self-similar collapse is strongly constrained already

The natural Navier–Stokes scaling is

\[
R(t)\sim\sqrt{T-t}.
\]

This corresponds to Leray backward self-similarity. Nontrivial backward self-similar singular profiles have been ruled out in broad classes, beginning with Nečas–Růžička–Šverák in \(L^3\), with extensions by Tsai and later authors to wider integrability/local-energy/Morrey settings.

This does **not** prove regularity: a hypothetical blowup may be non-self-similar or Type II. But it means the simplest “same snake, same shape, just smaller” terminal collapse is already mathematically disfavored/excluded under important admissibility hypotheses.

---

# CHECKPOINT 8 — A useful exact stress test: violent direction variation can exist, but diffusion kills it

Any proof claiming viscosity automatically makes the vorticity direction spatially tame is too strong.

On a periodic domain, take a Beltrami field satisfying

\[
\nabla\times u_0=\lambda u_0.
\]

Then

\[
(u_0\cdot\nabla)u_0
=
\nabla\frac{|u_0|^2}{2}-u_0\times\omega_0
=
\nabla\frac{|u_0|^2}{2},
\]

so the nonlinearity is a pressure gradient. The Navier–Stokes solution is essentially

\[
u(t)=e^{-\nu\lambda^2t}u_0.
\]

The direction field can oscillate on the tiny scale \(1/\lambda\), yet its amplitude decays on the correspondingly tiny time scale \(1/(\nu\lambda^2)\).

This is a valuable exact example of the proposed dichotomy:

> sharp geometry is allowed, but it comes with rapid viscous death rather than blowup.

It also shows that one cannot hope for a universal pointwise direction-coherence bound independent of amplitude and time.

---

# CHECKPOINT 9 — A sharp cross-sectional moment inequality

For a nonnegative scalar cross-sectional vorticity profile \(f(y)\) on \(\mathbb R^2\), define

\[
M=\int f\,dy,
\qquad
I=\int |y|^2f\,dy,
\qquad
b=I/M.
\]

Among nonnegative \(f\) with fixed mass and second moment, minimizing \(\int f^2\) gives a truncated parabola. The resulting sharp scaling is

\[
\boxed{
\int_{\mathbb R^2}f^2\,dy
\ge
\frac{4M^2}{9\pi b}.
}
\]

For a coherent one-sign vortex tube with circulation \(\Gamma\) and transverse second-moment width \(b\), this gives an enstrophy lower bound per unit length

\[
\boxed{
Z_{\rm per\ length}
\gtrsim
\frac{\Gamma^2}{b}.
}
\]

Thus a concentrated core is intrinsically expensive in enstrophy.

What this does **not** provide by itself is a lower bound on how long the concentrated core must exist. A singularity could try to create successively thinner cores on successively shorter time intervals.

---

# CHECKPOINT 10 — Variational dissipation toll for an idealized viscous core

For a locally straight, coherently aligned vortex core in a linear transverse strain field, let \(b\) denote transverse second-moment width. The standard strain-diffusion balance has the form

\[
\boxed{
\dot b=-\sigma b+4\nu,
}
\]

where \(\sigma\) is axial stretching rate. This is consistent with the classical Burgers-vortex balance.

Eliminate \(\sigma\):

\[
\sigma=\frac{4\nu-\dot b}{b}.
\]

The cross-sectional strain-action density scales like

\[
J=\int b\sigma^2dt
=
\int\frac{(4\nu-\dot b)^2}{b}\,dt.
\]

Use the exact algebraic inequality

\[
(4\nu-\dot b)^2
\ge
-16\nu\dot b,
\]

because

\[
(4\nu-\dot b)^2+16\nu\dot b
=(4\nu+\dot b)^2\ge0.
\]

Therefore any net contraction from \(b_0\) to \(b_1<b_0\) satisfies

\[
\boxed{
J\ge16\nu\log\frac{b_0}{b_1}.
}
\]

Equality occurs for \(\dot b=-4\nu\): trying to contract faster raises the required strain cost; trying to contract slower lets viscosity act longer and also raises the cost.

This captures a useful optimization principle:

> there is a cheapest possible rate for squeezing a viscous vortex core, and even the cheapest fixed fractional squeeze has a scale-independent cost.

### Anisotropic affine extension

Let \(C\) be the positive semidefinite \(2\times2\) transverse covariance tensor, \(b=\operatorname{tr}C\), and \(A\) the symmetric transverse strain. In a block-diagonal incompressible affine model the full strain cost is

\[
Q(A)=|A|_F^2+(\operatorname{tr}A)^2.
\]

If

\[
c=\operatorname{tr}(AC)=\frac{\dot b-4\nu}{2},
\]

then duality of this quadratic form gives

\[
|c|^2
\le
\frac{2}{3}b^2Q(A),
\]

hence

\[
\boxed{
|S|^2\ge
\frac{3}{8}
\frac{(\dot b-4\nu)^2}{b^2}.
}
\]

This shows the scale-independent contraction toll is not merely an artifact of perfectly isotropic radial squeezing inside the affine-core model.

---

# CHECKPOINT 11 — Conditional “fixed open center” no-go theorem

Assume the recursive ouroboros remains a coherent tube and each complete pass:

1. has centerline length \(L_n\ge L_*>0\) (a genuinely macroscopic open center),
2. carries a coherent core whose active cross-sectional area remains comparable to its second-moment width \(b_n\),
3. contracts \(b_n\to b_{n+1}\le q^2b_n\) with one fixed \(0<q<1\),
4. is governed locally well enough by the strain-diffusion moment inequality above that the cross-sectional contraction cost can be integrated into the global \(\int|S|^2\) budget.

Then each completed pass costs at least

\[
\Delta E_n
\ge
c(q)\nu^2L_n
\ge
c(q)\nu^2L_*.
\]

The unforced energy identity supplies only finite total dissipation:

\[
\frac12\|u(t)\|_2^2
+
2\nu\int_0^t\int|S|^2\,dx\,ds
=
\frac12\|u_0\|_2^2.
\]

Therefore infinitely many such complete macroscopic-center recursions are impossible.

### Status of this result

This is a **conditional model theorem**, not a Millennium proof. The vulnerable step is promoting a locally coherent vortex core to a rigorously controlled cross-sectional moment evolution under arbitrary curved, non-axisymmetric Navier–Stokes dynamics. The PDE permits reconnection, changing tube topology, loss of one-sign cross-sectional vorticity, anisotropic concentration, and nonlocal strain.

Still, within the literal fixed-open-center “pipe eating itself” geometry, the argument identifies a real scale-independent dissipation toll rather than relying on hand-waving about molecular cutoffs.

---

# CHECKPOINT 12 — If the hole also shrinks, the energy contradiction disappears

If the complete loop length shrinks,

\[
L_n\to0,
\]

then the per-generation lower bound becomes

\[
\Delta E_n\gtrsim c\nu^2L_n.
\]

A geometric sequence \(L_n\sim q^nL_0\) has

\[
\sum_nL_n<\infty,
\]

so finite energy does not by itself rule out infinitely many shrinking generations.

This is the important distinction between:

- **macroscopic open center**: conditional energy-budget contradiction;
- **shrinking open center**: no contradiction from this argument.

The latter returns us to the genuinely scale-critical Navier–Stokes problem.

---

# CHECKPOINT 13 — Why a fixed coarse-scale “pusher” cannot drive arbitrarily fine scales

Let \(k\) denote a fine spatial frequency and let \(K\ll k\) denote the highest frequency in a putative coarse background strain. Bernstein plus the energy bound gives

\[
\|\nabla u_{\le K}\|_\infty
\lesssim
K^{5/2}\|u_0\|_2.
\]

Viscous damping at frequency \(k\) is \(\nu k^2\). If the coarse field is to compete with that damping,

\[
K^{5/2}\|u_0\|_2
\gtrsim
\nu k^2,
\]

so

\[
\boxed{
K\gtrsim
\left(\frac{\nu}{\|u_0\|_2}\right)^{2/5}
 k^{4/5}
}
\]

up to constants.

Thus a fixed large-scale background cannot continue acting like an external force for arbitrarily small scales. The strain-generating part of an unforced blowup must itself migrate to increasingly fine scales.

This does not prove regularity: a multiscale hierarchy can still satisfy such a relation. It does, however, eliminate the naive picture “one large outer ring drives an infinitely tiny inner singularity forever.”

---

# CHECKPOINT 14 — Why topology alone cannot save us

Viscosity destroys material vortex-line topology. Smooth 3D Navier–Stokes solutions can exhibit creation/destruction and reconnection of vortex lines and vortex tubes without loss of regularity.

Therefore no final proof may rely on the same identifiable “pipe” persisting forever as a material object.

A rigorous statement must ultimately be phrased in Eulerian quantities such as

\[
\Omega,\quad \xi,\quad S,
\]

or critical function-space norms, rather than purely topological persistence of a tube.

This is a major reason the intuitive ouroboros picture is useful as a stress test but insufficient as the final proof language.

---

# CHECKPOINT 15 — What has actually been killed

The calculations above rule out or strongly obstruct the following candidate mechanisms:

- **Straight near-self-contact alone:** leading singular velocity does not close the gap; leading singular strain does not longitudinally stretch at closest approach.
- **Ever-thinner fixed-radius filament:** diffusion eventually wins because \((a/R)^2\log(R/a)\to0\).
- **Pure scale argument:** neither side wins merely because the geometry shrinks; Navier–Stokes is scale-critical enough that both nonlinear and viscous rates can accelerate together.
- **Naive “infinite steps require infinite time”:** false; Zeno sums converge.
- **Exact fixed-shape Leray collapse in standard admissible classes:** excluded by known nonexistence theorems.
- **Fixed macroscopic open-center recursive coherent tube:** conditionally excluded by a scale-independent dissipation toll per completed fractional contraction.
- **Fixed coarse outer pusher driving arbitrarily fine inner scales:** incompatible with simple energy/Bernstein scaling; the pusher itself must descend the scale hierarchy.

---

# CHECKPOINT 16 — The surviving monster

A hypothetical unforced singularity must now be allowed to exploit most or all of the following simultaneously:

1. genuinely three-dimensional, non-axisymmetric geometry;
2. nonlocal strain transfer between different parts of the flow;
3. a shrinking hierarchy of strain-generating scales;
4. sufficiently irregular vorticity direction to evade known coherence criteria;
5. enough geometric organization to keep producing extensional strain rather than merely translation/rotation;
6. enough concentration to beat viscosity without becoming an excluded backward self-similar profile;
7. reconnection/topology change if useful;
8. a mechanism in which the viscous cost of generating directional complexity is paid in one region while the nonlinear stretching benefit appears elsewhere.

This is the real escape hatch.

---

# CHECKPOINT 17 — The operator inequality that would finish the geometric route

The desired theorem would look qualitatively like

\[
\boxed{
\int \alpha\Omega^2dx
\le
(1-\delta)\nu
\int\left(|\nabla\Omega|^2+\Omega^2|\nabla\xi|^2\right)dx
+
F(t),
}
\]

for some \(\delta>0\) and time-integrable/subcritical remainder \(F\), **without assuming vorticity-direction coherence as an external hypothesis**.

If such an estimate held for all smooth finite-energy unforced solutions, the enstrophy identity would close and finite-time blowup would be excluded.

Known Constantin–Fefferman-type theorems effectively obtain this sort of control **conditional on** geometric coherence. The missing leap is to derive enough coherence/depletion dynamically from the Navier–Stokes evolution itself.

Equivalent target formulation:

> prove that every high-vorticity region is forced into a dichotomy in which either direction coherence depletes Biot–Savart stretching, or directional irregularity incurs sufficient viscous cost to prevent critical concentration.

The nonlocality of the Biot–Savart operator is what prevents the obvious pointwise version from working.

---

# CHECKPOINT 18 — Best next operators / attack plan

## A. Two-point commutator estimate

Use the exact geometric kernel and rewrite directional differences as

\[
\xi(x+y)-\xi(x)
=
\int_0^1 (y\cdot\nabla)\xi(x+\theta y)\,d\theta.
\]

Try to estimate the vortex-stretching trilinear form by a weighted square function in \(\Omega|\nabla\xi|\), rather than a pointwise Lipschitz norm. The hope is to make the nonlocal source curvature pay through the global directional-dissipation integral.

The critical issue is the \(|y|^{-3}\) kernel: one power is canceled by the directional difference, leaving an order-one singular integral. The half-Hölder threshold in the literature warns that this is exactly a critical-scale problem.

## B. Dyadic near/far decomposition

Split Biot–Savart interactions into annuli \(|y|\sim2^{-j}\). On each shell compare:

- angular mismatch between vorticity directions,
- vorticity concentration,
- local directional dissipation,
- and strain transfer into smaller scales.

Seek a fixed fractional loss per scale, or prove that maintaining order-one stretching efficiency across infinitely many shells forces a divergent sum of viscous directional costs.

## C. Blow-up rescaling and ancient limits

Assume blowup and rescale around a maximum-vorticity sequence. Ask what the “cannot corner fast enough” hypothesis becomes in the ancient limiting solution. Known Liouville/nonexistence theorems already eliminate large classes of self-similar or direction-coherent ancient limits. The objective would be to prove that the remaining limit is forced into an effectively 2D/aligned state.

## D. Curvature evolution

Use the actual evolution equation for vortex-line curvature/torsion from Constantin–Procaccia–Segel and isolate the competition

\[
\text{curvature creation by nonlocal strain gradients}
\quad\text{vs.}\quad
\text{straightening by stretching + viscous alignment}.
\]

The desired conclusion would be a scale-integrated bound strong enough to prevent \(\kappa d\) from remaining \(O(1)\) through an infinite collapsing hierarchy.

## E. Numerical falsification before proof effort

Construct controlled Navier–Stokes initial data resembling the recursive ouroboros geometry and measure:

- closest self-separation \(d(t)\),
- curvature \(\kappa(t)\),
- product \(\kappa d\),
- peak vorticity,
- directional-dissipation \(\int\Omega^2|\nabla\xi|^2\),
- geometric stretching efficiency \(\int\alpha\Omega^2 / \int |S|\Omega^2\),
- and whether the structure straightens/reconnects before critical concentration.

A numerical counterexample to the conjectured geometric inequality would save enormous proof effort.

---

# CHECKPOINT 19 — Honest bottom line

No unconditional proof of global regularity has been obtained here.

The work has, however, converted the original informal claim

> “viscosity requires dimension; the fluid cannot corner instantaneously”

into the more defensible research conjecture:

> **Dynamic geometric-depletion conjecture.** In finite-energy unforced 3D Navier–Stokes flow, any multiscale self-interaction capable of driving critical vorticity amplification must generate directional complexity at comparable scales; the exact geometry of Biot–Savart stretching plus viscous directional diffusion prevents that complexity from remaining sufficiently efficient across an infinite scale hierarchy.

The strongest completed sub-result of this notebook is conditional:

> **Fixed-open-center coherent-tube no-go (model theorem).** A recursive coherent vortex tube that repeatedly makes complete laps of length bounded below and contracts its viscous core by a fixed fraction per lap pays a scale-independent dissipation toll per lap in the affine/core-moment model. Finite initial energy therefore permits only finitely many such laps.

The critical unresolved step is to remove the coherent-core/affine reduction and prove an analogous global coercive estimate for arbitrary nonlocal 3D Navier–Stokes geometry.

So the verdict at this checkpoint is:

**NOT PROVEN, NOT HOPELESS, AND THE INTUITION HAS SURVIVED SEVERAL NONTRIVIAL ATTEMPTS TO BREAK IT.**

---

# References / literature anchors

1. P. Constantin and C. Fefferman, *Direction of Vorticity and the Problem of Global Regularity for the Navier-Stokes Equations*, Indiana Univ. Math. J. 42 (1993), 775–789. DOI: 10.1512/iumj.1993.42.42034.
2. P. Constantin, I. Procaccia, D. Segel, *Creation and dynamics of vortex tubes in three-dimensional turbulence*, Phys. Rev. E 51 (1995), 3207–3222. DOI: 10.1103/PhysRevE.51.3207.
3. H. Beirão da Veiga and L. C. Berselli, *On the regularizing effect of the vorticity direction in incompressible viscous flows*, Differential and Integral Equations 15 (2002), 345–356.
4. Z. Grujić, *Localization and geometric depletion of vortex-stretching in the 3D NSE*, Comm. Math. Phys. 290 (2009), 861–870. DOI: 10.1007/s00220-008-0726-8.
5. Z. Grujić and R. Guberović, *Localization of analytic regularity criteria on the vorticity and balance between the vorticity magnitude and coherence of the vorticity direction in the 3D NSE*, Comm. Math. Phys. 298 (2010), 407–418. DOI: 10.1007/s00220-010-1000-4.
6. J. Nečas, M. Růžička, V. Šverák, nonexistence of nontrivial Leray backward self-similar 3D Navier–Stokes profiles in \(L^3\), Acta Math. 176 (1996), 283–294.
7. T.-P. Tsai, extensions of backward self-similar nonexistence to broader profile classes, Arch. Rational Mech. Anal. 143 (1998), 29–51.
8. J. Bedrossian, P. Germain, B. Harrop-Griffiths, *Vortex Filament Solutions of the Navier-Stokes Equations*, Comm. Pure Appl. Math. 76 (2023), 685–787. DOI: 10.1002/cpa.22091.
9. A. Enciso, R. Lucà, D. Peralta-Salas, *Vortex reconnection in the three dimensional Navier–Stokes equations*, Advances in Mathematics 309 (2017), 452–486. DOI: 10.1016/j.aim.2017.01.025.
10. Classical Burgers vortex balance: for uniform axisymmetric strain, the viscous core scale obeys \(r_c^2\sim \nu/\text{strain}\), illustrating the same strain–diffusion balance used in Checkpoint 10.

---

## Reproducibility notes

Two algebraic calculations were independently checked symbolically during this run:

- the straight-filament strain matrix at closest approach and the exact cancellation \(t^TSt=0\) for every target tangent orthogonal to the separation vector;
- the first-order curved-source correction yielding \(\delta\alpha=-\Gamma\kappa/(2\pi d)\) for the explicit parabolic source orientation used in Checkpoint 3.

No numerical simulation or computer-assisted theorem prover was used to claim any unproved global result.

---

# CHECKPOINT 20 — The first nonlocal commutator attack closes only to the classical supercritical bound

The next attack was to use the exact directional cancellation directly, with no externally assumed Hölder coherence.

From the Constantin geometric kernel,

\[
|D(\hat h,\xi(x+h),\xi(x))|
\lesssim |\xi(x+h)-\xi(x)|.
\]

Also,

\[
\Omega(x+h)|\xi(x+h)-\xi(x)|
\le
|\omega(x+h)-\omega(x)|+|\Omega(x+h)-\Omega(x)|
\le 2|\omega(x+h)-\omega(x)|.
\]

Hence, after splitting the singular integral at a radius \(r>0\), the near-field stretching factor is bounded schematically by

\[
|\alpha_{<r}(x)|
\lesssim
\int_{|h|<r}
\frac{|\omega(x+h)-\omega(x)|}{|h|^3}\,dh.
\]

For Sobolev functions one has the Hajlasz-type difference estimate

\[
|\omega(x+h)-\omega(x)|
\lesssim
|h|\big(M|\nabla\omega|(x)+M|\nabla\omega|(x+h)\big),
\]

where \(M\) is the Hardy–Littlewood maximal operator. Since

\[
\left\|\frac{\mathbf 1_{|h|<r}}{|h|^2}\right\|_{L^1_h}
\sim r,
\]

the \(L^2\) maximal theorem gives

\[
\boxed{
\|\alpha_{<r}\|_2
\lesssim r\|\nabla\omega\|_2.
}
\]

For the far field, discard the angle factor and use Cauchy–Schwarz:

\[
\boxed{
\|\alpha_{>r}\|_\infty
\lesssim r^{-3/2}\|\omega\|_2.
}
\]

Write

\[
W=\|\omega\|_2,
\qquad
N=\|\nabla\omega\|_2.
\]

Then

\[
|T_{<r}|
=
\left|\int \Omega^2\alpha_{<r}\,dx\right|
\le
\|\Omega\|_4^2\|\alpha_{<r}\|_2.
\]

Using

\[
\|\Omega\|_4
\lesssim
W^{1/4}N^{3/4},
\]

we obtain

\[
|T_{<r}|
\lesssim
rW^{1/2}N^{5/2}.
\]

The far field satisfies

\[
|T_{>r}|
\lesssim
r^{-3/2}W^3.
\]

Balancing the two terms gives

\[
r\sim \frac{W}{N}
\]

and therefore

\[
\boxed{
|T|
\lesssim
W^{3/2}N^{3/2}.
}
\]

Young's inequality then yields the classical estimate

\[
|T|
\le
\frac{\nu}{2}N^2
+
C\nu^{-3}W^6.
\]

If \(Y=W^2\), the resulting differential inequality has the form

\[
Y'\lesssim \nu^{-3}Y^3,
\]

which does **not** preclude finite-time blowup.

### Callout

This calculation is important because it shows that simply feeding the exact directional difference into a generic commutator/maximal-function estimate does **not** produce a hidden regularity theorem. Without additional dynamic information, the geometric cancellation collapses back to the standard supercritical enstrophy estimate.

The reason is structural: the singular kernel is exactly at the endpoint where one full first difference of \(\omega\) recovers only the classical derivative count. The missing gain is a genuine fractional directional coherence effect, not an algebraic oversight.

---

# CHECKPOINT 21 — Why the naive instantaneous coercive inequality cannot be true

Checkpoint 17 proposed the dream estimate

\[
\int \alpha\Omega^2dx
\le
(1-\delta)\nu\|\nabla\omega\|_2^2
+F(\text{energy-level data}).
\]

A concentration scaling shows that no such universal **instantaneous** inequality can hold if the remainder is controlled only by kinetic energy.

Choose any smooth compactly supported divergence-free field \(\phi\) with positive instantaneous vortex-stretching integral

\[
T_0=\int (S_\phi\omega_\phi)\cdot\omega_\phi\,dx>0.
\]

Define the energy-preserving concentration

\[
u_\lambda(x)=\lambda^{3/2}\phi(\lambda x).
\]

Then

\[
\|u_\lambda\|_2^2=\|\phi\|_2^2,
\]

while

\[
\omega_\lambda=\lambda^{5/2}\omega_\phi(\lambda x),
\qquad
S_\lambda=\lambda^{5/2}S_\phi(\lambda x).
\]

Therefore

\[
\boxed{
T_\lambda=\lambda^{9/2}T_0,
}
\]

whereas

\[
\boxed{
\|\nabla\omega_\lambda\|_2^2
=\lambda^4\|\nabla\omega_\phi\|_2^2.
}
\]

Consequently,

\[
\frac{T_\lambda}{\nu\|\nabla\omega_\lambda\|_2^2}
\sim
\lambda^{1/2}\to\infty.
\]

Kinetic energy has remained fixed throughout.

### Conclusion

There is no universal instantaneous estimate of the form

\[
T\le c\nu N^2+F(\|u\|_2)
\]

with fixed \(c\) and finite energy-only remainder \(F\) that can close the problem.

This is not bad news for the original intuition. It says the phrase **"cannot corner fast enough" must be genuinely dynamical**. Arbitrarily violent instantaneous configurations are allowed. What must fail, if regularity is true for the geometric reason being pursued here, is their ability to *persist and recursively regenerate themselves through time*.

This also explains why optimizing instantaneous enstrophy production is not equivalent to constructing a singularity: very large instantaneous production is compatible with subsequent rapid depletion.

---

# CHECKPOINT 22 — The half-Hölder exponent is exactly the missing gain

Assume temporarily that in the active high-vorticity region the direction satisfies the critical coherence estimate

\[
|\xi(x+h)-\xi(x)|
\le H|h|^{1/2}.
\]

Then the geometric kernel loses half a power of singularity:

\[
|\alpha(x)|
\lesssim
H\,I_{1/2}(\Omega)(x),
\]

where \(I_{1/2}\) is the Riesz potential of order \(1/2\).

Hardy–Littlewood–Sobolev gives

\[
\|I_{1/2}\Omega\|_3
\lesssim
\|\Omega\|_2=W.
\]

Therefore

\[
|T|
\lesssim
H\|\Omega\|_3^2W.
\]

Since

\[
\|\Omega\|_3^2
\lesssim
WN,
\]

we get

\[
\boxed{
|T|\lesssim H W^2N.
}
\]

Young's inequality yields

\[
|T|
\le
\frac{\nu}{2}N^2
+
C\nu^{-1}H^2W^4.
\]

Thus, with \(Y=W^2\),

\[
Y'
\lesssim
\nu^{-1}H^2Y^2.
\]

The key difference from Checkpoint 20 is that the kinetic-energy identity already gives

\[
\int_0^T Y(t)\,dt
=
\int_0^T\|\omega(t)\|_2^2dt
<\infty.
\]

Hence, if \(H\) is uniformly bounded (or satisfies the appropriate time-integrability condition), this becomes a Gronwall inequality with integrable coefficient \(H^2Y\), and enstrophy remains bounded.

This reproduces the significance of the classical \(1/2\)-Hölder vorticity-direction regularity threshold.

### Callout

The calculations now identify the exact amount of geometric gain missing from the unconditional commutator estimate:

\[
\boxed{\text{one half of a spatial power in the direction field.}}
\]

The working conjecture can therefore be sharpened:

> the Navier–Stokes dynamics themselves must prevent high-vorticity geometry from losing an effective \(1/2\)-Hölder directional coherence quickly enough to sustain blowup.

---

# CHECKPOINT 23 — “Cannot corner fast enough” has an exact one-dimensional Sobolev meaning

Let \(X(s)\) be a vortex line parameterized by arclength, so

\[
X_s=\xi,
\qquad
\kappa=|\xi_s|.
\]

For two points on the same vortex line,

\[
|\xi(s_2)-\xi(s_1)|
\le
\int_{s_1}^{s_2}\kappa(s)\,ds.
\]

Cauchy–Schwarz gives

\[
\boxed{
|\xi(s_2)-\xi(s_1)|
\le
|s_2-s_1|^{1/2}
\left(\int_{s_1}^{s_2}\kappa^2ds\right)^{1/2}.
}
\]

Thus a uniform \(L^2\) curvature budget along active vortex-line segments automatically gives the **critical one-half Hölder exponent in arclength**.

Moreover, on a sufficiently short segment for which the accumulated turning is small, arclength and chord length are comparable. If

\[
\int_{s_1}^{s_2}\kappa\,ds\le \theta_0<\frac{\pi}{2},
\]

then projection onto the initial tangent gives

\[
|X(s_2)-X(s_1)|
\ge
\cos\theta_0\,|s_2-s_1|.
\]

Hence locally

\[
\boxed{
|\xi(s_2)-\xi(s_1)|
\lesssim
K_{\rm line}^{1/2}
|X(s_2)-X(s_1)|^{1/2},
}
\]

where

\[
K_{\rm line}
=
\int\kappa^2ds.
\]

This is the cleanest mathematical translation obtained so far of the original phrase **“it cannot corner fast enough.”** Infinite order-one turns on successively shorter segments force the line-bending budget \(\int\kappa^2ds\) to diverge.

### The remaining gap

The Constantin–Fefferman/Berselli criteria concern nearby high-vorticity points in space, not merely pairs lying on one well-behaved vortex line. Therefore a proof still needs to show either:

1. uniform/appropriately integrable control of line-curvature energy in the intense-vorticity region **plus** enough transverse coherence to transfer the estimate between neighboring vortex lines; or
2. an Eulerian replacement of this line estimate that supplies the same half-derivative gain directly.

The first option is geometrically very close to the ouroboros intuition.

---

# CHECKPOINT 24 — Exact stretching/straightening skeleton for vortex-line curvature

The previous checkpoint suggests studying curvature dynamically rather than trying to prove a static inequality.

Ignore viscosity for one moment and retain the exact stretching/transport part of the vorticity equation. Then

\[
D_t\xi=S\xi-\alpha\xi,
\qquad
\alpha=\xi\cdot S\xi.
\]

Define the curvature vector

\[
c=(\xi\cdot\nabla)\xi,
\qquad \kappa=|c|.
\]

Using the commutator

\[
D_t\nabla f
=
\nabla D_tf-(\nabla u)^T\nabla f,
\]

a direct index calculation gives

\[
\boxed{
D_tc
=
(\xi\cdot\nabla S)\xi
+Sc
-(\xi\cdot\nabla\alpha)\xi
-2\alpha c.
}
\]

Since \(c\cdot\xi=0\), dotting with \(c\) yields

\[
\boxed{
\frac12D_t\kappa^2
=
c\cdot(\xi\cdot\nabla S)\xi
+c\cdot Sc
-2\alpha\kappa^2.
}
\]

This identity cleanly separates three effects:

- \(-2\alpha\kappa^2\): stretching along the vortex direction straightens the line;
- \(c\cdot Sc\): transverse strain can help or oppose that straightening;
- \(c\cdot(\xi\cdot\nabla S)\xi\): spatial variation of strain regenerates curvature.

If \(\xi\) is aligned with the most extensive eigenvector of \(S\), so \(\alpha=\lambda_1>0\), then for every normal direction \(n\perp\xi\),

\[
n\cdot Sn\le \lambda_2\le\lambda_1=\alpha.
\]

Consequently the non-gradient strain terms satisfy

\[
\kappa^2(n\cdot Sn-2\alpha)
\le
-\alpha\kappa^2.
\]

So, in the strongly stretching aligned regime, local stretching itself **cannot maintain curvature**. Curvature must continually be regenerated by the strain-gradient term

\[
\boxed{(\xi\cdot\nabla S)\xi.}
\]

This reproduces, at the level of an exact local identity for the inviscid/stretching skeleton, the straightening mechanism reported by Constantin–Procaccia–Segel.

For a material vortex-line segment in the inviscid skeleton, \(ds\) evolves according to

\[
D_t(ds)=\alpha\,ds.
\]

Hence its bending energy obeys

\[
\frac{d}{dt}\int\kappa^2ds
=
\int
\left[
2c\cdot(\xi\cdot\nabla S)\xi
+2c\cdot Sc
-3\alpha\kappa^2
\right]ds.
\]

Under top-eigenvector alignment this simplifies schematically to

\[
\boxed{
\frac{d}{dt}\int\kappa^2ds
\lesssim
2\int\kappa|\nabla S|\,ds
-
\int\alpha\kappa^2ds.
}
\]

So the geometric problem has moved one derivative outward:

> a blowup hierarchy must regenerate curvature through gradients of the nonlocal strain faster than stretching straightens it and viscosity smooths it.

Since \(S\) is a Calderón–Zygmund transform of \(\omega\),

\[
\|\nabla S\|_2\lesssim\|\nabla\omega\|_2.
\]

That is encouraging, but not enough by itself: converting this spatial \(L^2\) control into a **uniform linewise \(L^2\) curvature bound** is exactly where concentration onto thin vortex structures can defeat naive trace estimates.

### New proof target

The previous “instantaneous coercivity” target is too strong and is ruled out by Checkpoint 21. The more plausible dynamic target is now:

> prove that high-vorticity vortex-line segments cannot accumulate unbounded \(L^2\) curvature before the strain-gradient field needed to create that curvature pays a non-integrable Navier–Stokes dissipation cost.

If such a statement supplied a uniform critical \(1/2\)-Hölder constant in intense-vorticity regions, Checkpoint 22 would close the regularity argument.

---

# CHECKPOINT 25 — Status after the second operator run

This continuation produced one negative and two positive clarifications.

**Negative:** the hoped-for universal instantaneous estimate absorbing vortex stretching into viscous enstrophy dissipation plus an energy-only remainder is impossible by concentration scaling. The proof, if it exists, must use time evolution.

**Positive 1:** the direct two-point commutator calculation identifies the precise analytic barrier. Without extra geometric information it reproduces the classical \(Y'\lesssim Y^3\) estimate; a half spatial power of directional coherence improves this to the critical \(Y'\lesssim Y^2\) structure, which closes using the finite energy-dissipation integral \(\int Ydt\).

**Positive 2:** an \(L^2\) curvature budget along vortex lines gives exactly that half-Hölder exponent by one-dimensional Cauchy–Schwarz, and the exact curvature evolution shows that positive stretching tends to destroy rather than create curvature; the required curvature has to be continually regenerated by \(\nabla S\).

The surviving bottleneck is therefore sharper than before:

\[
\boxed{
\text{control the linewise / tubular accumulation of curvature generated by }\nabla S
\text{ at the critical }1/2\text{-Hölder scale.}
}
\]

No global proof is claimed. The static operator route has been exhausted to a clear scaling obstruction; the dynamic curvature route remains alive.


---

# CHECKPOINT 26 — Literature cross-check of the new dynamic target

The dynamic-curvature target is not isolated from established work:

- Beirão da Veiga–Berselli-type results show that critical \(1/2\)-Hölder coherence of the vorticity direction suffices for regularity; this matches exactly the half-power recovered in Checkpoint 22.
- Constantin–Procaccia–Segel explicitly found that vortex stretching tends to straighten vortex lines and that well-aligned vortex tubes exhibit depleted self-stretching; this matches the sign structure in Checkpoint 24.
- Deng–Hou–Yu developed local non-blowup criteria for 3D Euler in terms of vortex-line length, curvature, and divergence of the vorticity direction. Although Euler is a different equation and vortex lines are material there, their results confirm that line geometry and curvature are legitimate blowup-control variables rather than merely visualization language.
- High-Reynolds-number DNS reported by Buaria et al. (Nature Communications, 2020) found strong self-attenuation of extreme vorticity events: in the most intense-vorticity regions the local strain contribution to enstrophy production becomes strongly negative, while the net positive production is associated with more nonlocal strain. This is empirical rather than a theorem, but it mirrors the analytic obstruction isolated here: the dangerous mechanism is remote/nonlocal regeneration, not naive local self-stretching.

These cross-checks do not prove the conjecture, but they support the decision to abandon the static coercive route and focus on the time-dependent transfer

\[
\nabla S\longrightarrow \kappa\longrightarrow \text{directional coherence}\longrightarrow \alpha.
\]


---

# CHECKPOINT 27 — Exact viscous direction equation: the geometry is a weighted harmonic-map heat flow

The previous run isolated curvature generation by the strain gradient. A cleaner route is to return to the exact direction equation and keep *all* viscous terms.

Write

\[
\omega=\Omega\xi,\qquad \Omega=|\omega|,\qquad |\xi|=1,
\]

and

\[
F_{\tan}=P_{\xi^\perp}S\xi
=S\xi-(\xi\cdot S\xi)\xi.
\]

Expanding \(\Delta(\Omega\xi)\), projecting parallel and perpendicular to \(\xi\), and using

\[
\xi\cdot\Delta\xi=-|\nabla\xi|^2
\]

gives the exact equation, wherever \(\Omega>0\),

\[
\boxed{
\partial_t\xi+u\cdot\nabla\xi
=F_{\tan}
+\nu\Delta\xi
+2\nu(\nabla\ln\Omega\cdot\nabla)\xi
+\nu|\nabla\xi|^2\xi.
}
\]

The diffusion and cross-diffusion combine in divergence form:

\[
\boxed{
\Delta\xi+2\nabla\ln\Omega\cdot\nabla\xi
=\Omega^{-2}\nabla\cdot(\Omega^2\nabla\xi).
}
\]

Thus the direction field is not merely transported and diffused. It is a sphere-valued, weighted harmonic-map heat flow whose natural diffusion weight is precisely \(\Omega^2\).

Equivalently, moving the cross-diffusion into the transport field,

\[
\boxed{
\partial_t\xi+igl(u-2\nu\nabla\ln\Omega\bigr)\cdot\nabla\xi-
u\Delta\xi
=F_{\tan}+\nu|\nabla\xi|^2\xi.
}
\]

Two observations are exact:

1. The stretching scalar \(\alpha=\xi\cdot S\xi\), which amplifies \(\Omega\), does **not** directly rotate \(\xi\). The strain rotates the direction only through \(F_{\tan}\).
2. The cross-diffusion drift on the left is

\[
\boxed{-2\nu\nabla\ln\Omega.}
\]

This vector always points *down* the vorticity-magnitude gradient. In other words, the intrinsic viscous direction dynamics advects directional structure away from increasing \(\Omega\).

For a critical point profile

\[
\Omega(x,t)=\Phi(x,t)|x|^{-2},
\]

one has

\[
-2\nu\nabla\ln\Omega
=
4\nu\frac{x}{|x|^2}-2\nu\nabla\ln\Phi.
\]

The leading term is an outward radial drift of magnitude \(4\nu/r\). This is exactly the repulsive drift isolated in Grujić's September 2026 analysis of critical point singularities.

### Callout

The phrase "viscosity pushes the corner back out" has an exact PDE representative: the direction equation contains an intrinsic drift down the vorticity gradient, and for the critical \(r^{-2}\) concentration it is the explicit outward field \(4\nu x/r^2\).

---

# CHECKPOINT 28 — Hemisphere barrier: the intrinsic geometric nonlinearity cannot manufacture a new large turn by itself

Fix a constant unit vector \(e\), and define the directional deviation

\[
\theta=1-\xi\cdot e=\frac12|\xi-e|^2.
\]

Let

\[
\mathcal L
=
\partial_t+igl(u-2\nu\nabla\ln\Omega\bigr)\cdot\nabla-
u\Delta.
\]

Taking the inner product of the exact direction equation with \(-e\) gives

\[
\boxed{
\mathcal L\theta
=-F_{\tan}\cdot e
-\nu|\nabla\xi|^2(1-\theta).
}
\]

On the hemisphere centered at \(e\),

\[
\xi\cdot e\ge0
\quad\Longleftrightarrow\quad
\theta\le1,
\]

the harmonic-map term has the favorable sign:

\[
-\nu|\nabla\xi|^2(1-\theta)\le0.
\]

Hence

\[
\boxed{
\mathcal L\theta\le |F_{\tan}|
\qquad\text{while }\theta\le1.
}
\]

In particular, if \(F_{\tan}=0\) and the parabolic boundary data remain in a fixed hemisphere, the maximum principle prevents the intrinsic diffusion/HMHF dynamics from creating a new hemisphere-sized directional defect in the interior.

This is stronger than the earlier informal statement that viscosity "smooths the direction." It says that, while the direction remains in a hemisphere, the nonlinear sphere constraint is not a source of angular growth for this deviation functional.

### Consequence for the cornering picture

A new order-one turn in an intense-vorticity core must be supplied by at least one of:

- tangential strain \(F_{\tan}\),
- transport of already-irregular direction through the boundary,
- or a breakdown of the single-hemisphere description/topological bubbling.

The core cannot simply generate an arbitrary corner from a coherent state by local maximal stretching: when \(\xi\) is a strain eigenvector, even the maximal-stretching eigenvector, \(F_{\tan}=0\).

---

# CHECKPOINT 29 — Exact global budget for the only part of strain that rotates the vorticity direction

The tangential forcing satisfies pointwise

\[
|F_{\tan}|\le |S|.
\]

For an unforced finite-energy solution,

\[
\frac12\|u(t)\|_2^2
+2\nu\int_0^t\|S(s)\|_2^2\,ds
=
\frac12\|u_0\|_2^2.
\]

Therefore

\[
\boxed{
\int_0^T\int_{\mathbb R^3}|F_{\tan}|^2\,dx\,dt
\le
\frac{\|u_0\|_2^2}{4\nu}.
}
\]

This is an exact finite spacetime budget for **direction-rotating strain**.

It does not prove regularity because \(L^2_{t,x}\) is too weak to prevent concentration at a point. Nevertheless, it gives a useful geometric accounting rule: every mechanism that continually rebuilds order-one angular defects over a region of nonvanishing geometric extent must pay from a finite budget.

---

# CHECKPOINT 30 — Codimension accounting: why a macroscopic vortex tube is expensive but a point core is not

The previous statement can be quantified at the scaling level without using the Burgers-core reduction.

Suppose an order-one directional change is created on spatial scale \(r\) over its natural viscous time

\[
\tau_r\sim \frac{r^2}{\nu}.
\]

Producing an \(O(1)\) turn through tangential strain requires a forcing rate of order

\[
|F_{\tan}|\sim \frac1{\tau_r}\sim\frac{\nu}{r^2}.
\]

Assume the active set has \(k\) macroscopic directions of characteristic size \(L\) and \(3-k\) directions of thickness \(r\). Its volume is

\[
V_r\sim L^k r^{3-k}.
\]

The corresponding spacetime \(L^2\) cost is therefore

\[
\mathcal C_k(r)
\sim
\left(\frac{\nu}{r^2}\right)^2
\left(L^k r^{3-k}\right)
\left(\frac{r^2}{\nu}\right),
\]

or

\[
\boxed{
\mathcal C_k(r)
\sim
\nu L^k r^{1-k}.
}
\]

Thus:

\[
\boxed{
\begin{array}{c|c}
\text{geometry} & \text{cost per diffusive-scale order-one turn}\\
\hline
k=0\ \text{point-like} & \nu r\\
k=1\ \text{filament of fixed length }L & \nu L\\
k=2\ \text{sheet of fixed area }L^2 & \nu L^2/r
\end{array}
}
\]

This explains, using the exact \(F_{\tan}\) budget rather than the earlier affine-core model, why the user's literal fixed-open-center ouroboros is strongly obstructed.

A vortex tube making complete laps around a hole whose circumference stays bounded below has \(k=1\) and \(L\ge L_*>0\). Rebuilding an order-one directional turn on every successively smaller transverse scale has a scale-independent cost \(\gtrsim \nu L_*\). Infinitely many such episodes would require an infinite \(L^2_{t,x}\) tangential-strain budget.

By contrast, a genuinely point-localized event costs only \(O(\nu r)\). For a geometric scale sequence \(r_n=q^n r_0\),

\[
\sum_n \nu r_n<\infty.
\]

So the global energy budget **cannot** rule out an infinite point-scale cascade.

### Important status

The scaling estimate above becomes a rigorous lower bound only after specifying how much of the angular change must be generated internally by \(F_{\tan}\) rather than imported through the parabolic boundary. The hemisphere identity in Checkpoint 28 is the mechanism that could justify such a statement for an isolated coherent core, but a complete trace/barrier argument for arbitrary Navier–Stokes geometry has not been supplied here.

Still, the codimension distinction is robust and exposes a genuine wall:

> fixed-length filament recursion is energetically expensive at every scale; point concentration gets cheaper as the scale shrinks.

---

# CHECKPOINT 31 — Attempt to remove the critical-point inflow hypothesis using energy alone: FAILS by the same codimension scaling

For the critical profile \(\Omega\sim r^{-2}\), the viscous cross-diffusion contributes an outward drift of size

\[
\frac{4\nu}{r}.
\]

To defeat that barrier, the physical flow in a co-moving frame must provide inward relative velocity of the same order,

\[
|u_r|\gtrsim \frac{\nu}{r}.
\]

Across a region of size \(r\), this requires a strain scale

\[
|S|\sim \frac{\nu}{r^2}.
\]

For a point-like core of volume \(r^3\), the instantaneous \(L^2\) strain cost is

\[
\int_{B_r}|S|^2dx
\sim
\frac{\nu^2}{r},
\]

and over one diffusive time \(r^2/\nu\),

\[
\boxed{
\int_{t}^{t+r^2/\nu}\int_{B_r}|S|^2dx\,ds
\sim
\nu r.
}
\]

Again this is summable over a geometric cascade of radii.

Therefore the global finite-energy identity does **not** automatically imply the inward-flow condition required by the September 2026 critical-point barrier analysis. This closes off an attractive but invalid shortcut.

For a fixed-length filamentary core, replacing \(r^3\) by \(Lr^2\) changes the same estimate to \(\sim\nu L\) per scale, reproducing the fixed-open-center obstruction.

### Callout

The mathematics now cleanly distinguishes the two cases:

- **ouroboros with a macroscopic open center:** repeated critical inward transport/turning has a nonvanishing per-scale cost;
- **point-like shrinking core:** the cost decreases like \(r\), so energy alone leaves an escape hatch.

This is why the general Millennium problem does not collapse to the fixed-open-center argument.

---

# CHECKPOINT 32 — A striking exact analogue: stationary critical point cores carry the signature of a point force

A velocity field with the critical point scaling

\[
u(x)\sim |x|^{-1}
\]

is homogeneous of degree \(-1\). Landau found explicit stationary solutions with precisely this scaling. Šverák later classified smooth \((-1)\)-homogeneous stationary solutions on \(\mathbb R^3\setminus\{0\}\): the nonzero ones are Landau solutions.

The crucial fact for the present investigation is that a Landau solution, when interpreted distributionally on all of \(\mathbb R^3\), satisfies

\[
-\nu\Delta U+(U\cdot\nabla)U+\nabla P
=b\,\delta_0
\]

for a nonzero constant vector \(b\) (after normalization of parameters). The singular core therefore carries a radius-independent momentum-flux defect represented by a Dirac point force.

In particular, an exact nonzero stationary \((-1)\)-homogeneous point singularity is **not** a globally unforced stationary solution on \(\mathbb R^3\).

This is not a proof against dynamical blowup: a singular limit of smooth unforced solutions could, in principle, generate a defect measure through concentration of nonlinear momentum flux. But it is an unusually literal mathematical counterpart of the original intuition:

> the canonical stationary critical point core looks, distributionally, as though something at the singular point is supplying a force.

Therefore a hypothetical unforced blowup cannot simply settle into a stationary \(1/r\) core with no further bookkeeping. The surrounding flow must dynamically manufacture the required point momentum flux.

---

# CHECKPOINT 33 — The other simple critical limit is already excluded: backward self-similar collapse

The natural viscous collapse scale is

\[
|x|\sim\sqrt{\nu(T-t)},
\qquad
|u|\sim (T-t)^{-1/2}.
\]

Exact Leray backward self-similar singular profiles are known to be absent under broad finite-energy/integrability hypotheses (Nečas–Růžička–Šverák; Tsai), and several asymptotically self-similar variants have also been excluded under stated convergence/integrability assumptions (e.g. Chae and subsequent work).

So two of the simplest ways a critical point core could organize itself are already obstructed:

1. **quasi-stationary \(1/r\) critical core:** the canonical homogeneous profiles are Landau-type and possess a point-force defect;
2. **fixed-profile diffusive shrinker:** broad classes of backward self-similar profiles are non-existent.

This does not eliminate Type-II, genuinely non-self-similar, or all discretely self-similar scenarios. In fact, sufficiently general backward discretely self-similar solutions remain a delicate/open class, although important subclasses and scaling ranges have been ruled out.

### Consequence

Any remaining critical point singularity has to remain dynamically nontrivial *on its own shrinking diffusive time scale*. It cannot simply freeze into a stationary critical profile or approach one of the standard admissible Leray profiles.

---

# CHECKPOINT 34 — Connection to the September 2026 logarithmic-depletion program

Two very recent preprints by Zoran Grujić independently arrive at a structure strikingly close to the current route.

The first rewrites the stretching eigenvalue as a Calderón–Zygmund commutator using the exact unidirectional Biot–Savart cancellation. For a critical point profile \(\Omega\sim r^{-2}\), it shows that a very weak logarithmic decay of local mean oscillation of the vorticity direction,

\[
\xi\in \mathrm{bmo}_{1/|\log r|},
\]

is sufficient, under the paper's hypotheses, to break criticality and avert blowup.

The companion paper derives precisely the direction PDE of Checkpoint 27 and studies whether this logarithmic directional regularity can be propagated. Its main structural ingredients are:

- the outward \(4\nu x/r^2\) drift generated by the critical vorticity envelope;
- the hemisphere subsolution identity of Checkpoint 28;
- the fact that strain enters direction dynamics only through \(F_{\tan}=P_{\xi^\perp}S\xi\).

The paper still requires structural assumptions, notably control of inward radial fluid transport relative to the viscous drift and suitable control of tangential strain/core history. It explicitly notes that the inward-flow condition does not follow merely from divergence-freeness or the critical weak-\(L^3\) velocity bound.

This matters for the present run because it independently identifies the same final obstruction:

\[
\boxed{
\text{Can self-generated inward transport and tangential strain continually import/regenerate
 directional disorder faster than viscous cross-diffusion ejects/smooths it?}
}
\]

The recent work proves substantial conditional pieces of the answer, but not an unconditional global regularity theorem.

---

# CHECKPOINT 35 — Updated escape-hatch map

After the third operator run, a hypothetical unforced singularity must now evade all of the following obstructions simultaneously:

1. It cannot be a fixed-macroscopic-length recursive tube that must rebuild order-one turns at every transverse scale; the finite \(L^2_{t,x}\) budget of tangential strain gives a scale-independent cost in filament geometry.
2. It cannot rely on an ever-thinner ordinary filament around a fixed loop; core diffusion outruns the logarithmic self-induction gain.
3. It cannot obtain dangerous stretching from the leading straight near-contact interaction; the leading singular longitudinal stretching cancels.
4. It cannot remain directionally coherent in the classical high-vorticity sense; known geometric-depletion criteria then give regularity.
5. It cannot simply settle into a stationary homogeneous \(1/r\) point core without acquiring a Landau-type point-force defect.
6. It cannot be one of the broad standard classes of exact/asymptotically Leray self-similar collapse already excluded in the literature.
7. Energy alone does **not** eliminate a point-localized cascade, because the strain/turning/inflow cost per diffusive episode scales like \(\nu r\) and is summable as \(r\to0\).

The surviving scenario is correspondingly pathological:

> a shrinking, essentially point-localized, non-self-similar core in which the surrounding unforced flow repeatedly supplies critical inward momentum flux and tangential strain, while the direction field continually avoids enough logarithmic/half-Hölder coherence for geometric depletion to trigger, and does so on every shrinking diffusive time scale.

This is not empty by theorem. It is, however, far narrower than the original generic phrase "vortex self-interaction might blow up."

---

# CHECKPOINT 36 — New precise formulation of “cannot corner fast enough”

The most useful scale-invariant geometric diagnostic now appears to be line curvature.

Along an arclength-parametrized vortex line,

\[
\kappa=|\partial_s\xi|.
\]

For a segment of length \(r\), Cauchy–Schwarz gives

\[
|\xi(s+r)-\xi(s)|^2
\le
r\int_s^{s+r}\kappa^2(\sigma)\,d\sigma.
\]

Therefore a necessary condition for an order-one directional turn on arbitrarily small scales is

\[
\boxed{
\limsup_{r\downarrow0}
\left(
 r\int_s^{s+r}\kappa^2\,d\sigma
\right)>0.
}
\]

Equivalently, a would-be singularity must sustain the critical curvature concentration

\[
\int_s^{s+r}\kappa^2\,d\sigma
\gtrsim \frac1r
\]

along relevant intense-vorticity lines at arbitrarily small scales.

If instead

\[
\boxed{
 r\int_s^{s+r}\kappa^2\,d\sigma\longrightarrow0
}
\]

uniformly in the intense-vorticity region (together with enough transverse coherence to compare neighboring vortex lines), the direction becomes better than the critical half-Hölder threshold at small scales and the geometric-depletion route closes.

This gives the sharpest current mathematical translation of the user's intuition:

> **A singularity has to keep paying for curvature at the critical rate \(1/r\) all the way down. The unresolved theorem is whether an unforced viscous flow can dynamically sustain that critical line-curvature concentration while simultaneously overcoming the outward cross-diffusion of its own vorticity envelope.**

---

# CHECKPOINT 37 — Verdict after third run

No global proof has been obtained.

This run did, however, produce three useful upgrades:

- an exact finite-energy budget for the strain component that actually rotates the vorticity direction;
- a codimension calculation explaining why the literal macroscopic ouroboros is much harder to sustain than a point-localized critical core;
- and a direct connection between the remaining point-core loophole, Landau's point-force signature, and the newest logarithmic-depletion/direction-PDE work.

It also killed another tempting shortcut: finite kinetic energy alone cannot force the critical outward viscous drift to beat inward fluid transport at a point, because the required scale-by-scale strain expenditure is summable.

The project is therefore **not proved and not hopeless**. The next mathematically meaningful target is no longer a generic estimate on vortex stretching. It is one of the following equivalent-looking dynamic statements:

\[
\boxed{
\text{(A) automatic decay of local mean oscillations of }\xi\text{ in critical cores,}
}
\]

or

\[
\boxed{
\text{(B) impossibility of sustaining }r\int_{\text{vortex segment of length }r}\kappa^2ds\gtrsim1
\text{ across infinitely many shrinking diffusive scales.}
}
\]

Either result, if established with the correct high-vorticity localization and transverse control, would convert the original "failure to corner" intuition into a genuine regularity mechanism.

---

## Additional literature anchors added in the third run

11. Z. Grujić, *Logarithmic Depletion of Vortex Stretching and Singularity Evasion in the 3D Navier-Stokes Equations*, arXiv:2607.08866 (2026). Preprint.
12. Z. Grujić, *On Decay of the Local Mean Oscillations of the Vorticity Direction in Critical Navier-Stokes Flows*, arXiv:2609.05720v2 (2026). Preprint.
13. V. Šverák, *On Landau's Solutions of the Navier-Stokes Equations*, Journal of Mathematical Sciences 179 (2011), 208–228; arXiv:math/0604550.
14. D. Chae, *Nonexistence of asymptotically self-similar singularities in the Euler and the Navier-Stokes equations*, Math. Ann. 338 (2007), 435–449.
15. D. Chae, *Remarks on the asymptotically discretely self-similar solutions of the Navier-Stokes and the Euler equations*, Nonlinear Analysis 125 (2015), 251–259.
16. D. Chae and J. Wolf, *Removing discretely self-similar singularities for the 3D Navier-Stokes equations*, Comm. PDE 42 (2017), 1359–1374.
17. S. Hormoz and M. P. Brenner, *Absence of singular stretching of interacting vortex filaments*, J. Fluid Mech. 707 (2012), 191–204.

---

# CHECKPOINT 38 — Correction: tangential-strain budget does not by itself bound corner formation

The previous codimension estimate treated the tangential strain

\[
F_{\rm tan}=P_{\xi^\perp}S\xi
\]

as though every new small-scale turn had to be created by directly rotating \(\xi\) through \(F_{\rm tan}\). That is too restrictive.

Write the exact direction equation in drift-diffusion form

\[
\mathcal L\xi
=F_{\rm tan}+\nu|\nabla\xi|^2\xi,
\qquad
\mathcal L=\partial_t+b\cdot\nabla-\nu\Delta,
\qquad
b=u-2\nu\nabla\log\Omega.
\]

Let

\[
G=\frac12|\nabla\xi|^2.
\]

Differentiating the direction equation gives the exact Bochner-type identity

\[
\boxed{
\mathcal L G
=
\nabla\xi:\nabla F_{\rm tan}
-
\sum_{i,j,k}(\partial_i b_j)(\partial_j\xi_k)(\partial_i\xi_k)
+\nu|\nabla\xi|^4
-\nu|\nabla^2\xi|^2.
}
\]

Consequently direction gradients can be created or compressed even when \(F_{\rm tan}\) itself is small. Two mechanisms are visible:

1. compression by the effective drift gradient \(\nabla b\);
2. the positive \(\nu|\nabla\xi|^4\) term familiar from harmonic-map heat flow.

Thus the finite spacetime budget

\[
\int|F_{\rm tan}|^2<\infty
\]

is not, by itself, a finite budget for the number of cornering events.

For the critical radial cross-diffusion drift

\[
b_0=4\nu\frac{x}{|x|^2},
\]

\[
\nabla b_0
=4\nu\left(\frac{I}{r^2}-2\frac{x\otimes x}{r^4}\right).
\]

Its eigenvalues are

\[
-\frac{4\nu}{r^2}
\quad\text{in the radial direction},
\qquad
+\frac{4\nu}{r^2}
\quad\text{in the two tangential directions}.
\]

So, despite the fact that the drift transports information outward, the gradient equation contains radial compression capable of amplifying a pre-existing radial direction gradient. This does not contradict the hemisphere barrier for \(1-\xi\cdot e\); it shows only that gradient control is subtler than direct forcing control.

### Correction to the previous escape-hatch map

The scale-independent \(L^2\) cost of \(F_{\rm tan}\) remains a useful obstruction when genuinely new rotation must be supplied locally, but it is **not an unconditional per-turn toll**. A final proof has to control both direct direction forcing and compression of already existing direction structure.

---

# CHECKPOINT 39 — Explicit local Navier–Stokes jet that creates curvature from a straight vorticity direction

To test the strongest possible version of “stretching must straighten the vortex,” construct the following divergence-free polynomial velocity field near the origin:

\[
\boxed{
\begin{aligned}
u_1&=-\frac{s}{2}x-\frac{\Omega_0}{2}y+\frac{M}{2}z^2,\\
u_2&=\frac{\Omega_0}{2}x-\frac{s}{2}y-Mxy,\\
u_3&=sz+Mxz.
\end{aligned}}
\]

Direct differentiation gives

\[
\nabla\cdot u=0,
\]

and

\[
\boxed{
\omega=\nabla\times u=(0,0,\Omega_0-My).
}
\]

Hence, on a sufficiently small neighborhood where \(\Omega_0-My>0\),

\[
\boxed{\xi=e_z}
\]

**exactly**. The vorticity lines are initially straight there and all spatial derivatives of \(\xi\) vanish.

The strain tensor is

\[
S=
\begin{pmatrix}
-s/2 & -My/2 & Mz\\
-My/2 & -Mx-s/2 & 0\\
Mz & 0 & Mx+s
\end{pmatrix}.
\]

At the origin,

\[
S(0)=\operatorname{diag}(-s/2,-s/2,s),
\qquad
\alpha(0)=\xi\cdot S\xi=s,
\]

and therefore

\[
F_{\rm tan}(0)=0.
\]

Nevertheless,

\[
\boxed{
(\xi\cdot\nabla S)\xi\big|_{0}
=\partial_z S\,e_z\big|_0
=M e_x.
}
\]

Let

\[
c=(\xi\cdot\nabla)\xi
\]

be the vortex-line curvature vector. Initially \(c(0)=0\). Because \(\xi\) is constant on a neighborhood, all initial viscous direction terms vanish there. The exact curvature evolution therefore yields at the origin

\[
\boxed{
D_t c(0,0)=M e_x.
}
\]

At the same point the magnitude equation initially gives

\[
\boxed{
D_t\Omega(0,0)=s\Omega_0.
}
\]

Thus one may have, simultaneously:

- positive vorticity stretching \(s>0\);
- perfectly straight local vorticity direction at the initial instant;
- zero tangential strain at the point itself;
- and arbitrarily strong instantaneous creation of vortex-line curvature through the strain-gradient term, by choosing \(|M|\) large.

This is an explicit counterexample to any **pointwise** theorem asserting that strong stretching automatically makes local curvature monotonically decrease.

The polynomial field is only a local jet, not finite-energy data on all of \(\mathbb R^3\). That is not an obstacle: on a ball it has a vector potential, and multiplying that potential by a smooth cutoff equal to one on a smaller ball and then taking its curl produces a smooth compactly supported divergence-free field with exactly the same local jet. Hence the calculation is realizable by legitimate smooth finite-energy unforced Navier–Stokes initial data.

---

# CHECKPOINT 40 — Critical scaling of the curvature-producing jet

The preceding local construction can be placed exactly at the Navier–Stokes critical rate.

At a target length scale \(r\), choose schematically

\[
s\sim \frac{\nu}{r^2},
\qquad
\Omega_0\sim\frac{\nu}{r^2},
\qquad
M\sim\frac{\nu}{r^3}.
\]

Then inside a ball of radius comparable with \(r\),

\[
|u|\sim\frac{\nu}{r},
\qquad
|\omega|\sim\frac{\nu}{r^2},
\qquad
|\nabla S|\sim\frac{\nu}{r^3}.
\]

The natural viscous time is

\[
\tau_r\sim\frac{r^2}{\nu}.
\]

During one such time,

\[
|c|\sim M\tau_r\sim\frac1r,
\]

which is exactly the curvature required for an order-one directional change on length \(r\).

Meanwhile the stretching exponent over the same time is

\[
s\tau_r=O(1),
\]

so the same local event can produce an order-one multiplicative change in vorticity magnitude.

The kinetic energy contained in the critical ball scales only as

\[
E_r\sim |u|^2r^3\sim\nu^2 r,
\]

and its enstrophy as

\[
Z_r\sim|\omega|^2r^3\sim\frac{\nu^2}{r}.
\]

The corresponding kinetic-energy dissipation over one diffusive episode is

\[
\nu Z_r\tau_r\sim\nu^2r.
\]

Therefore for a geometric sequence \(r_n=q^n r_0\),

\[
\sum_n \nu^2 r_n<\infty.
\]

So finite energy is fully compatible with an arbitrarily long sequence of **point-localized critical cornering episodes** at successively smaller scales.

An even cleaner statement follows from exact Navier–Stokes scaling. Start from one compactly supported smooth realization of the local jet and its short-time smooth solution. If it develops a nonzero curvature \(c_*\) at some small dimensionless time \(t_*>0\), then

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2 t)
\]

is another smooth unforced solution with the same viscosity. At time \(t_*/\lambda^2\), its curvature is \(\lambda c_*\), while its kinetic energy is \(\lambda^{-1}\) times the original energy.

Hence:

\[
\boxed{
\text{arbitrarily sharp critical cornering can occur in arbitrarily small-energy smooth unforced flows.}
}
\]

What scaling does **not** construct is one single solution that repeats this event at \(\lambda\to\infty\) as \(t\uparrow T\).

---

# CHECKPOINT 41 — The original slogan must be weakened

The literal local statement

> “viscosity does not let a vortex corner fast enough”

is false.

The polynomial jet above shows that the true Navier–Stokes dynamics can create curvature at the critical rate \(1/r\) in the critical time \(r^2/\nu\), while stretching the vorticity at the same time. No external force is required.

The surviving version of the conjecture is therefore genuinely **inter-scale**:

> **Failure-to-sustain conjecture.** Although an unforced smooth Navier–Stokes flow can execute a critical cornering/stretching episode at any one scale, it cannot self-reproduce such an episode through an infinite sequence of shrinking scales in finite time while retaining enough Biot–Savart stretching efficiency to avoid geometric depletion and viscosity.

This distinction is important. The problem is not a speed limit at one scale. It is whether the exact Navier–Stokes nonlinearity can build a self-replicating critical cascade.

A proof must therefore establish some loss in the renormalization map from one active scale to the next, for example a contraction of a dimensionless quantity such as local Reynolds amplitude, directional oscillation, or stretching efficiency:

\[
\mathcal R_{n+1}\le(1-\delta)\mathcal R_n+\varepsilon_n,
\]

or

\[
\Theta_{n+1}\le(1-\delta)\Theta_n+\varepsilon_n,
\qquad \sum_n\varepsilon_n<\infty,
\]

for the relevant rescaled state variables. No such unconditional scale-to-scale contraction is presently known.

Exact fixed-point repetition in rescaled variables corresponds to backward self-similar behavior, and exact periodic repetition corresponds to a discretely self-similar scenario; broad classes of both are already excluded by known nonexistence results. Thus a surviving blowup cascade would have to keep changing its rescaled geometry rather than simply replaying one critical cornering event forever.

---

# CHECKPOINT 42 — Why energy/scaling estimates alone cannot finish the job

The obstruction exposed above is consistent with Tao's averaged Navier–Stokes blowup construction. Tao constructed an averaged version of the 3D Navier–Stokes bilinear term which retains the standard energy cancellation

\[
\langle \widetilde B(u,u),u\rangle=0
\]

and the relevant scaling structure, yet permits finite-time blowup. The lesson is that a positive result for true Navier–Stokes must use finer algebraic/geometric structure of the actual nonlinearity than the energy identity and generic harmonic-analysis bounds alone.

Our calculation reaches the same wall from the geometric side:

- energy allows point-critical episodes because their cost is \(O(r)\);
- the exact local Navier–Stokes jet allows critical curvature generation;
- straight-filament and coherent-direction cancellations still remove many naive geometries;
- therefore the only plausible remaining positive route is to prove a **scale-to-scale loss of efficiency specific to the true Biot–Savart/strain geometry**.

This is a stronger and more accurate endpoint than the original “viscosity cannot corner fast enough” claim.

---

# CHECKPOINT 43 — Current verdict after fourth run

The analysis has now falsified one strong version of the working intuition while preserving a narrower one.

**Falsified:** there is no universal local viscous speed limit preventing critical vortex-line corner formation. Smooth unforced Navier–Stokes data can create curvature at the required \(1/r\) rate over the required \(r^2/\nu\) time scale.

**Still alive:** one-scale critical cornering may be impossible to chain into an infinite self-generated finite-time cascade. All of the previously identified geometric cancellations, coherence criteria, outward critical cross-diffusion, self-similar nonexistence results, and fixed-macroscopic-tube costs remain relevant to this inter-scale question.

The next meaningful target is therefore not another local curvature inequality. It is a renormalized cascade theorem: show that every passage from scale \(r\) to a smaller scale \(qr\) loses a definite amount of dimensionless stretching/cornering efficiency unless the rescaled state approaches one of the already excluded coherent/self-similar regimes.

At present that theorem is not available. Establishing it would be genuinely new mathematics and is very close to the heart of the global regularity problem itself.

## Additional literature anchor added in the fourth run

18. T. Tao, *Finite time blowup for an averaged three-dimensional Navier-Stokes equation*, J. Amer. Math. Soc. 29 (2016), 601–674; arXiv:1402.0290. The averaged nonlinearity retains the energy cancellation but admits finite-time blowup, demonstrating that energy and scaling structure alone cannot settle the true equation.

---

# CHECKPOINT 44 — Exact smooth closure really does cancel the local singular geometry

The user's interruption suggested a sharper geometric point: if a vortex "corners fast enough" to close back on itself, perhaps the very act of closure forces the dangerous self-interaction to cancel at the contact point.

There is a precise sense in which this is correct.

Fix a time at which the vorticity field is smooth and nonzero in a neighborhood, and write

\[
\xi=\frac{\omega}{|\omega|}.
\]

A vortex line is an integral curve

\[
\gamma'(s)=\xi(\gamma(s)).
\]

Because \(\xi\) is locally Lipschitz, the ODE has unique integral curves. Therefore two vortex lines cannot cross transversely at a point where \(\omega\neq0\). If a vortex line closes, it is a periodic integral curve and returns with the same tangent direction. A finite-angle corner at an exact smooth closure is impossible.

This feeds directly into the Constantin geometric kernel. The vortex-stretching factor has the form

\[
\alpha(x)
=\frac{3}{4\pi}\,\mathrm{PV}\int
D(\hat h,\xi(x+h),\xi(x))
\frac{\Omega(x+h)}{|h|^3}\,dh.
\]

At coincidence, smooth closure gives

\[
\xi(x+h)\to\xi(x),
\]

so

\[
D(\hat h,\xi(x+h),\xi(x))\to0.
\]

If \(\xi\in C^1\), then

\[
|D|\lesssim |\xi(x+h)-\xi(x)|
\lesssim \|\nabla\xi\|_\infty |h|,
\]

so the nominal \(|h|^{-3}\) singular kernel loses one power at the contact. The exact contact point is therefore not a source of a bare \(|h|^{-3}\) self-stretching singularity.

The same geometric factor also vanishes for parallel or antiparallel directions because it is controlled by the sine of the angle. Thus even antiparallel osculation is depleted at leading order.

### Important interpretation

A self-contact blowup cannot simply rely on "the two pieces finally touch and the singular kernel explodes." If the direction field remains smooth through contact, the leading geometric interaction cancels precisely there.

---

# CHECKPOINT 45 — A closed circular ring demonstrates the distinction: velocity adds, strain cancels

For an ideal circular vortex ring of radius \(R\) and circulation \(\Gamma\), the velocity on its symmetry axis is

\[
 u_z(z)=\frac{\Gamma R^2}{2(R^2+z^2)^{3/2}}.
\]

At the geometric center,

\[
 u_z(0)=\frac{\Gamma}{2R},
\]

so the contributions of the loop do **not** cancel in velocity. They add to a finite translational velocity.

But

\[
\frac{du_z}{dz}(0)=0.
\]

By axisymmetry and incompressibility, the first velocity gradient at the center vanishes. Thus the ring center sees translation but no extensional strain.

This is the physically relevant form of the user's cancellation intuition:

> closure need not cancel motion, but a sufficiently symmetric closure can cancel the **strain** that would amplify vorticity.

Likewise, the ideal circular ring's self-induced motion is translation along its axis rather than longitudinal stretching of the ring.

This cannot be generalized to every noncircular closed loop; noncircular rings can deform under their nonlocal self-interaction. But it provides an exact example in which complete closure reorganizes the self-field into transport rather than singular amplification.

---

# CHECKPOINT 46 — Every closed loop has a mandatory curvature bill

For every smooth closed space curve of length \(L\), Fenchel's theorem gives

\[
\int_\gamma \kappa\,ds\ge2\pi.
\]

Cauchy-Schwarz then gives

\[
\left(\int_\gamma\kappa\,ds\right)^2
\le
L\int_\gamma\kappa^2\,ds,
\]

and hence

\[
\boxed{
\int_\gamma\kappa^2\,ds\ge\frac{4\pi^2}{L}.
}
\]

Therefore a family of genuinely closed vortex lines whose lengths shrink to zero must carry divergent \(L^2\) curvature:

\[
L\to0
\quad\Longrightarrow\quad
\int\kappa^2ds\to\infty.
\]

This is another exact version of "closing requires cornering."

It is **not** by itself a regularity proof. The previous local-jet calculation showed that critical curvature \(\kappa\sim1/L\) can be generated on the diffusive time \(L^2/\nu\), and the energy cost of a point-localized critical event is summable across geometrically shrinking scales. Thus Fenchel's theorem identifies a compulsory geometric burden, but does not show that Navier-Stokes cannot pay it.

---

# CHECKPOINT 47 — Why exact cancellation at closure still does not finish the proof

The dangerous loophole is that cancellation is guaranteed only if the direction field remains regular **through** the contact.

A singularity can attempt to synchronize three events:

\[
 d(t)\to0,
\qquad
 \Omega(t)\to\infty,
\qquad
 \text{modulus of continuity of }\xi\text{ degenerates},
\qquad t\uparrow T.
\]

Then there is never a regular instant at which one may simply set \(d=0\) and invoke smooth tangent matching. The loss of directional regularity can occur at the same limiting time as the contact.

The straight near-contact cancellation makes the necessary rate explicit. If two intense-vorticity branches are separated by \(d\), and

\[
K(t)=\|\nabla\xi(t)\|_\infty
\]

in the relevant region, then directional mismatch satisfies schematically

\[
|\Delta\xi|\lesssim Kd.
\]

The leading straight-filament \(1/d^2\) interaction is depleted by this mismatch, giving at worst a curvature-corrected scale

\[
\alpha_{\rm pair}
\sim
\frac{\Gamma}{d^2}(Kd)
=
\frac{\Gamma K}{d}.
\]

To retain the full critical \(\Gamma/d^2\) efficiency, the candidate therefore requires

\[
\boxed{Kd\gtrsim1.}
\]

So as self-separation collapses, the direction gradient must diverge at least reciprocally with the gap.

At the level of the known half-Hölder geometric criterion, if

\[
|\xi(x)-\xi(y)|\lesssim H|x-y|^{1/2}
\]

with suitable control in the high-vorticity region, geometric regularity theory prevents blowup. Therefore a self-contact singularity must drive the corresponding half-Hölder seminorm to infinity; a finite-angle approach across gap \(d\) requires at least

\[
H\gtrsim d^{-1/2}.
\]

Thus the exact closure cancellation does not solve the problem, but it forces a singular self-contact mechanism to destroy direction coherence at the same time it closes the gap.

---

# CHECKPOINT 48 — Smooth closure, reconnection, or singular contact: a trichotomy

For a proposed self-contact event there are three qualitatively different endpoints.

### 1. Smooth contact with nonzero vorticity

If \(\Omega>0\) and \(\xi\) extends continuously/Lipschitzly to the contact, vortex-line uniqueness forces tangent matching. The leading geometric stretching kernel cancels at coincidence.

### 2. Contact through a zero-vorticity/reconnection region

If \(\Omega\to0\) in the contact region, \(\xi\) can become undefined without a vorticity blowup there. Viscous Navier-Stokes is known to permit creation, destruction, and reconnection of vortex structures while the velocity solution remains smooth. Thus topology can change without a singularity.

### 3. Singular contact

The only remaining self-contact blowup scenario is one in which high vorticity and loss of directional coherence occur simultaneously as \(d\to0\). The limiting direction field then fails to remain regular enough for the smooth-contact cancellation theorem to apply.

This is a significantly narrower target than "a vortex loop touches itself and blows up."

---

# CHECKPOINT 49 — Gap-closing kinematics show what the singular contact must pay

For two material trajectories \(X(t),Y(t)\), set

\[
h=X-Y,
\qquad d=|h|,
\qquad n=h/d.
\]

Then

\[
\frac12\frac{d}{dt}d^2
=h\cdot(u(X)-u(Y)).
\]

Using the fundamental theorem of calculus and the fact that the antisymmetric part of \(\nabla u\) drops out of a quadratic form,

\[
\boxed{
\frac{\dot d}{d}
=
\int_0^1 n\cdot S(Y+\theta h)n\,d\theta.
}
\]

Therefore finite-time collision of distinct material trajectories requires an unbounded accumulated compressive strain:

\[
\int^T -\left(\int_0^1n\cdot S n\,d\theta\right)dt=\infty.
\]

If \(\int_0^T\|S(t)\|_\infty dt<\infty\), material trajectories cannot collide.

This is not directly a vortex-line no-contact theorem in viscous flow, because vortex lines are not material objects when \(\nu>0\). Diffusion permits reconnection. It does show, however, that a literal material-tube collapse to a point already requires precisely the kind of divergent strain associated with loss of regularity.

---

# CHECKPOINT 50 — A warning: incompressibility does not force pre-contact alignment

One might hope that the compression required to close the gap automatically aligns the two approaching directions before contact. A simple strain tensor disproves that idea.

Take

\[
S=\operatorname{diag}(-2a,a,a),
\qquad a>0,
\]

with gap normal \(n=e_1\). Then

\[
n\cdot Sn=-2a,
\]

so the gap is compressed.

But every unit tangent in the transverse plane,

\[
t=(0,\cos\theta,\sin\theta),
\]

satisfies

\[
St=at,
\]

and hence its normalized direction evolution under the strain is

\[
P_{t^\perp}St=0.
\]

Thus the same incompressible strain can compress the separation while preserving **any** angle between two transverse directions.

So the statement

> "if it closes, strain must align it before it gets there"

is false on kinematic grounds alone.

The actual positive statement is subtler:

> if it reaches an exact contact while the vorticity direction is still smooth and nonzero, tangent uniqueness forces alignment at the contact and the leading geometric kernel cancels.

A hypothetical blowup can try to keep a finite directional mismatch all the way to \(t\uparrow T\), with the mismatch discontinuity appearing only at the singular limit.

---

# CHECKPOINT 51 — Revised self-contact target

The user's closure observation survives in the following precise form:

> **Smooth-closure depletion principle.** A completed smooth self-closure of a nonzero-vorticity line cannot contain a finite-angle corner; the direction is single-valued, and the leading singular Biot-Savart stretching geometry vanishes at coincidence. Therefore a self-contact-driven Navier-Stokes singularity must occur in the *approach to closure*, through simultaneous collapse of spatial separation and directional regularity, rather than being generated by the completed closure itself.

This gives a sharper necessary condition for a self-contact blowup sequence \((x_n,y_n,t_n)\):

\[
 d_n=|x_n-y_n|\to0,
\qquad
\Omega(x_n,t_n),\Omega(y_n,t_n)\to\infty,
\]

while

\[
\frac{|\xi(x_n,t_n)-\xi(y_n,t_n)|}{d_n^{1/2}}\to\infty
\]

(or otherwise violating the appropriate high-vorticity coherence hypothesis), and at the stronger Lipschitz level

\[
\|\nabla\xi(t_n)\|\,d_n\not\to0.
\]

If instead direction coherence survives to contact, the self-contact mechanism geometrically depletes itself; if vorticity vanishes in the contact region, viscous reconnection can resolve the topology smoothly.

This does not establish global regularity, but it turns the user's "it closes off and cancels" observation into a rigorous **endpoint obstruction** for the self-contact route.

## Additional literature anchors added in the fifth run

19. A. Enciso, R. Lucà, D. Peralta-Salas, *Vortex reconnection in the three dimensional Navier-Stokes equations*, Advances in Mathematics 309 (2017), 452–486. Smooth Navier-Stokes solutions can create/destroy/reconnect vortex structures without loss of regularity.
20. Fenchel's theorem for closed space curves: \(\int \kappa ds\ge2\pi\), yielding \(\int\kappa^2ds\ge4\pi^2/L\) by Cauchy-Schwarz.
21. Classical circular vortex-ring Biot-Savart formula: the ring has nonzero axial translation at its center but vanishing first axial derivative there; the symmetric closure cancels strain rather than velocity.

---

# CHECKPOINT 52 — General first-order near-contact expansion: which curvature actually matters?

The previous closest-approach calculation can be sharpened considerably.  Fix a local coordinate frame in which the source filament has tangent

\[
t_2=e_z,
\]

and the target point lies a distance \(d\) away in the normal direction

\[
n=e_x.
\]

Write the source centerline locally as

\[
X(s)=\left(\frac{\kappa_n s^2}{2},\frac{\kappa_b s^2}{2},s\right),
\]

where \(\kappa_n\) is the curvature component in the \((t_2,n)\)-plane and

\[
\kappa_b=\kappa\cdot(t_2\times n)
\]

is the curvature component in the binormal-to-separation direction.  Let the target tangent be

\[
t_1=(0,\sin\theta,\cos\theta),
\]

so \(\theta\) is the angle between the two locally straight tangents.

A direct symbolic expansion of the Biot–Savart filament integral gives the following facts for a symmetric local window about the source point.

For a perfectly straight source, the longitudinal stretching integrand is odd in \(s\), hence

\[
\int t_1\cdot S_0 t_1\,ds=0.
\]

The first-order contribution of \(\kappa_n\) is also odd and integrates to zero.  The first nonvanishing curvature correction is the \(\kappa_b\) term:

\[
\boxed{
\alpha_{2\to1}
=\frac{\Gamma\kappa_b}{4\pi d}
\bigl(3\sin^2\theta-2\bigr)
+O(\kappa^2)
}
\]

for the infinite symmetric-window leading asymptotic.

Thus the dangerous first curvature correction is not arbitrary curvature.  It is specifically the component

\[
\boxed{\kappa\cdot(t\times n)}
\]

that bends the source in the direction whose binormal motion can alter the gap.

The sign changes at

\[
\sin^2\theta=\frac23,
\qquad
\theta_c=\arcsin\sqrt{\frac23}
\approx54.7356^\circ.
\]

Therefore, once the two branches are more aligned than about \(54.7^\circ\), the sign of the curvature correction is opposite the sign that drives the target toward the source in the calculation below.

This is a more precise version of the qualitative phrase “closure turns off the stretching”: near an aligned closure, the curvature component that is capable of closing the gap is locally **anti-stretching**.

## Normal velocity generated by the same curvature component

For the same source curve, the first-order normal velocity at the target is

\[
\frac{\partial}{\partial\kappa_b}(u\cdot n)
=-\frac{\Gamma s^2}{8\pi(d^2+s^2)^{3/2}}
\]

at the integrand level.  Integrating over a symmetric finite local window \([-L,L]\) gives

\[
\boxed{
(u\cdot n)_{\kappa_b}
=-\frac{\Gamma\kappa_b}{4\pi}
Q\!\left(\frac{L}{d}\right),
}
\]

where

\[
Q(z)=\operatorname{arsinh}z-\frac{z}{\sqrt{1+z^2}}>0.
\]

For \(L\gg d\),

\[
Q(L/d)=\log\frac{2L}{d}-1+o(1).
\]

Hence \(\kappa_b>0\) drives the target toward the source in this orientation, while for \(|\theta|<\theta_c\) the same sign produces

\[
\alpha_{2\to1}<0.
\]

So, in the near-aligned regime,

\[
\boxed{
\text{the local curvature term that closes the gap compresses rather than stretches the target vorticity.}
}
\]

This statement is only a first-order local filament asymptotic.  It does not include the nonlocal remainder, finite-core effects, or arbitrary strongly curved geometry.

---

# CHECKPOINT 53 — Two-branch closure-depletion relation

Now take two nearly parallel pieces of the same-sign vortex structure.  Let \(n\) point from branch 2 toward branch 1, let their common leading tangent be \(t\), and define

\[
b=t\times n,
\qquad
k_i=\kappa_i\cdot b.
\]

Using the same first-order local-window approximation for the two mutual interactions gives

\[
\dot d_{\rm near}
=\frac{\Gamma}{4\pi}
Q(L/d)(k_1-k_2),
\]

while the sum of their mutual longitudinal stretching rates is

\[
\alpha_{1,\rm near}+\alpha_{2,\rm near}
=\frac{\Gamma}{2\pi d}(k_1-k_2).
\]

Therefore

\[
\boxed{
\alpha_{1,\rm near}+\alpha_{2,\rm near}
=\frac{2}{d\,Q(L/d)}\,\dot d_{\rm near}.
}
\]

Since \(Q>0\), a locally induced closing motion has

\[
\dot d_{\rm near}<0
\]

and therefore

\[
\boxed{
\alpha_{1,\rm near}+\alpha_{2,\rm near}<0.
}
\]

This is the cleanest mathematical version so far of the user's closure observation:

> **In the aligned two-filament asymptotic, the same first-order mutual geometry that closes the gap produces net pairwise longitudinal compression, not net stretching.**

The relation also reveals why exact smooth closure is especially depleted.  If the two local jets become identical as they merge, then

\[
k_1-k_2\to0,
\]

so both the relative closing velocity and the pair-summed longitudinal stretching vanish at leading local-induction order.

A finite-time approach that keeps \(|\dot d|\) at the critical size therefore requires a diverging curvature-jet mismatch rather than merely large common curvature.

---

# CHECKPOINT 54 — What the local closing pair does to vorticity amplitude

Ignoring for the moment viscosity and all nonlocal strain outside the local pair, the two vorticity magnitudes satisfy schematically

\[
\frac{d}{dt}\log(\Omega_1\Omega_2)
=\alpha_1+\alpha_2.
\]

Using the closure-depletion relation,

\[
\frac{d}{dt}\log(\Omega_1\Omega_2)
\simeq
\frac{2\dot d}{dQ(L/d)}.
\]

Thus, during local mutual gap closure,

\[
\frac{d}{dt}\log(\Omega_1\Omega_2)<0.
\]

For \(d\ll L\), where

\[
Q(L/d)\sim\log(2L/d)-1,
\]

integration gives the asymptotic local-pair behavior

\[
\boxed{
\Omega_1\Omega_2
\propto
\frac{1}{[\log(C/d)]^2}
}
\]

up to multiplicative constants and the neglected remote/diffusive terms.

This should **not** be read as a theorem that each individual branch loses vorticity.  One branch can be stretched while the other is compressed more strongly.  The robust statement of the local model is that their product, and for comparable magnitudes their pair enstrophy, is depleted by the closing interaction.

That gives a new escape requirement for a singularity: if one branch is to blow up while the closing pair has negative net local stretching, the growth must be supplied by nonlocal strain and/or by an increasingly extreme magnitude asymmetry between the two branches.

---

# CHECKPOINT 55 — Divergence-free vorticity makes magnitude asymmetry another geometric bill

The identity

\[
\nabla\cdot\omega=0,
\qquad
\omega=\Omega\xi,
\]

implies

\[
\xi\cdot\nabla\Omega+\Omega\nabla\cdot\xi=0.
\]

Along a vortex line parametrized by arclength \(s\),

\[
\boxed{
\frac{d}{ds}\log\Omega=-\nabla\cdot\xi.
}
\]

Consequently, between two points on the same vortex line,

\[
\boxed{
\frac{\Omega(s_2)}{\Omega(s_1)}
=\exp\!\left[-\int_{s_1}^{s_2}\nabla\cdot\xi\,ds\right].
}
\]

Thus a strategy in which one near-contact branch becomes arbitrarily stronger than its mate requires

\[
\left|\int\nabla\cdot\xi\,ds\right|\to\infty
\]

along the connecting vortex-line segment, unless the two points cease to belong to one coherent nonzero-vorticity line because of reconnection or vanishing vorticity.

For a smooth closed vortex line on which \(\Omega>0\), periodicity immediately gives

\[
\boxed{
\oint\nabla\cdot\xi\,ds=0.
}
\]

This is purely kinematic and holds independently of the Euler/Navier–Stokes evolution.  It does not forbid large positive and negative pieces that cancel around the loop, but it shows that extreme magnitude disparity along a closed tube must be accompanied by an extreme convergence/divergence geometry somewhere else on that same tube.

This is closely related to the localized vortex-line estimates of Deng–Hou–Yu, who use curvature and \(\nabla\cdot\xi\) along a high-vorticity vortex-line segment to derive nonblowup conditions for 3D Euler.  Their theorem is for Euler, so it is not itself a proof for viscous Navier–Stokes; the relevance here is that the exact same geometric quantities emerge independently from the closure calculation.

---

# CHECKPOINT 56 — Far-field strain has an explicit dissipation price

The closing pair cannot provide positive net local stretching once it is sufficiently aligned, so ask how expensive it is for a remote part of the flow to provide an order-one stretching impulse.

Let \(S_{>R}(x,t)\) denote the part of the Biot–Savart strain generated by vorticity farther than distance \(R\) from \(x\).  Since the strain kernel obeys

\[
|K(z)|\lesssim |z|^{-3},
\]

Cauchy–Schwarz gives

\[
|S_{>R}(x,t)|
\lesssim
\left(\int_{|z|>R}|z|^{-6}dz\right)^{1/2}
\|\omega(t)\|_2
\lesssim
R^{-3/2}\|\omega(t)\|_2.
\]

Along any path \(x(t)\) over a time interval \(I\) of length \(\tau\),

\[
\int_I|S_{>R}(x(t),t)|dt
\lesssim
R^{-3/2}\tau^{1/2}
\left(\int_I\|\omega(t)\|_2^2dt\right)^{1/2}.
\]

If the remote field must supply an accumulated order-one stretching impulse \(A_0>0\), then

\[
\boxed{
\nu\int_I\|\omega\|_2^2dt
\gtrsim
\nu A_0^2\frac{R^3}{\tau}.
}
\]

For a critical scale-\(d\) event lasting a parabolic time

\[
\tau\lesssim C\frac{d^2}{\nu},
\]

this becomes

\[
\boxed{
E_{\rm diss}(I)
\gtrsim
c(A_0,C)\,\nu^2\frac{R^3}{d^2}.
}
\]

This gives a rigorous scale-chase constraint.

- A fixed macroscopic pusher \(R\sim1\) cannot provide order-one stretching to arbitrarily small \(d\): the required dissipation diverges like \(d^{-2}\).
- If \(R=\Lambda d\), the cost is only \(\sim\nu^2\Lambda^3d\), which is summable over a geometric scale cascade.  So comparable-scale forcing is not excluded.
- More generally, if \(d_n\) decreases geometrically and \(R_n\sim d_n^\alpha\), then the per-stage lower bound scales as

\[
\nu^2 d_n^{3\alpha-2}.
\]

An infinite sequence is incompatible with finite dissipation when \(\alpha\le2/3\); to evade this particular estimate the source scale must itself collapse with

\[
\boxed{\alpha>\frac23.}
\]

Thus the “external” part of an unforced cascade cannot remain genuinely external.  It must follow the singular core down toward zero scale.

This is stronger and cleaner than the earlier Bernstein estimate, but it still does not prove regularity: \(R_n\) may shrink fast enough, and the point-scale dissipation cost can remain summable.

---

# CHECKPOINT 57 — Relation to known geometric nonblowup and partial-regularity theory

The present calculations line up with two established bodies of theory.

First, Deng–Hou–Yu proved localized geometric nonblowup criteria for 3D Euler using a vortex-line segment \(L_t\) through the high-vorticity region.  Their hypotheses involve the segment length \(L(t)\), curvature \(\kappa\), \(\nabla\cdot\xi\), and tangential/normal velocity components.  In one standard formulation, if

\[
M(t)L(t)\le C_0,
\qquad
L(t)\gtrsim(T-t)^B,
\]

with the velocity growth mild enough and the exponents satisfying the stated balance, blowup is excluded.  The important point for this project is not to import an Euler theorem into Navier–Stokes, but that the precise geometric escape quantities we keep deriving — curvature, directional divergence, shrinking vortex-line length, and nonlocal velocity — are already known to be the relevant ones in rigorous vortex-line nonblowup analysis.

Second, Caffarelli–Kohn–Nirenberg epsilon regularity says that a Navier–Stokes singular point must retain a nontrivial **scale-invariant** local dissipation density down arbitrarily small parabolic cylinders.  In one standard version, sufficiently small

\[
\frac1r\int_{Q_r}|\nabla u|^2dxdt
\]

implies regularity at the center.  This explains why the point-scale cost found repeatedly in this notebook,

\[
E_r\sim\nu^2 r,
\]

cannot by itself settle the problem: dividing by the scale \(r\) produces an order-one critical quantity.  The point demon is sitting exactly at the threshold where partial regularity theory says a singularity, if it exists, must live.

This is a useful negative check: the current scaling is not accidentally stronger than known theory.

---

# CHECKPOINT 58 — Updated self-contact escape diagram

The self-contact route has now been narrowed to the following alternatives.

### A. Smooth/aligned closure

If the two branches align as they approach and their local curvature jets become comparable, then:

\[
D\to0,
\qquad
k_1-k_2\to0,
\]

and the leading local mutual interaction loses both its gap-closing power and its longitudinal stretching power.  In the first-order aligned model, any remaining local closing motion has negative pair-summed stretching.

### B. One branch tries to amplify at the expense of the other

The local pair can transfer stretching from one branch to the other, but their product is depleted under gap closure.  To make one branch overwhelmingly stronger while retaining one coherent vortex line requires a divergent integrated \(\nabla\cdot\xi\) along the connecting segment.

### C. Remote strain rescues the amplification

A fixed coarse-scale pusher is impossible at arbitrarily small target scales by the far-field dissipation estimate.  The pusher must itself descend toward the singular scale; for a geometric target cascade, a power-law source distance \(R_n\sim d_n^\alpha\) must satisfy \(\alpha>2/3\) merely to evade the global energy budget.

### D. Finite-angle singular contact

The direction fails to align, so the solution must lose at least the known critical directional coherence while \(d\to0\).  Viscous reconnection can otherwise resolve the topology smoothly.

The surviving candidate is therefore not “a vortex bites its tail.”  It is an increasingly compact **cluster** of interacting vortex geometry in which the closing pair locally depletes itself and the needed positive stretching is continually imported from other geometry that is itself collapsing almost as fast.

That is a much more constrained mechanism.

---

# CHECKPOINT 59 — Current strongest derived statement

Within the first-order slender-filament, near-aligned closest-approach asymptotic, the following relation has been derived and symbolically verified:

\[
\boxed{
\dot d_{\rm near}<0
\quad\Longrightarrow\quad
\alpha_{1,\rm near}+\alpha_{2,\rm near}<0.
}
\]

More precisely,

\[
\boxed{
\alpha_{1,\rm near}+\alpha_{2,\rm near}
=\frac{2\dot d_{\rm near}}
{d\left[\operatorname{arsinh}(L/d)-L/\sqrt{L^2+d^2}\right]}.
}
\]

This is **not a Navier–Stokes regularity theorem**.  It is a local geometric depletion law for the specific self-contact asymptotic.  Its importance is conceptual: the branch interaction responsible for completing the closure is not simultaneously a net local amplifier of the two branch vorticities.

The remaining proof problem is consequently shifted again:

> Can a finite-energy unforced Navier–Stokes solution construct an infinite, point-localized, scale-descending network of *remote/comparable-scale* strain sources quickly enough to overcome the local closure depletion at every generation?

That is now the sharpest version of the “failure to sustain” conjecture obtained in this run.

## Additional references added in this continuation

22. J. Deng, T. Y. Hou, X. Yu, *Geometric Properties and Nonblowup of 3D Incompressible Euler Flow*, Comm. Partial Differential Equations 30 (2005), 225–243. DOI: 10.1081/PDE-200044488.
23. J. Deng, T. Y. Hou, X. Yu, *Improved Geometric Conditions for Non-Blowup of the 3D Incompressible Euler Equation*, Comm. Partial Differential Equations 31 (2006), 293–306. DOI: 10.1080/03605300500358152.
24. L. Caffarelli, R. Kohn, L. Nirenberg, *Partial regularity of suitable weak solutions of the Navier–Stokes equations*, Comm. Pure Appl. Math. 35 (1982), 771–831.
25. M. J. Shelley, D. I. Meiron, S. A. Orszag, *Dynamical aspects of vortex reconnection of perturbed anti-parallel vortex tubes*, J. Fluid Mech. 246 (1993), 613–652. DOI: 10.1017/S0022112093000291.

## Verification artifact

The first-order Biot–Savart expansion, the \(54.7356^\circ\) sign threshold, the finite-window normal-velocity coefficient, and the aligned-pair closure-depletion relation are reproduced in:

- `checkpoint_52_pair_contact_verify.py`
- `checkpoint_52_pair_contact_verify.txt`

---

# CHECKPOINT 60 — Closed relay test: three segments are too few for a genuine 3-D single-loop relay

A useful discrete Biot–Savart element model writes the velocity induced at target point \(x_i\) by a short source element \(q_j=\Gamma\,d\ell_j\) as

\[
 u_{j\to i}=\frac{1}{4\pi}\frac{q_j\times r_{ij}}{|r_{ij}|^3},
 \qquad r_{ij}=x_i-x_j.
\]

If \(t_i\) is the target tangent, its longitudinal stretching contribution is

\[
\boxed{
\alpha_{j\to i}
=-\frac{3}{4\pi}
\frac{(t_i\cdot r_{ij})\,t_i\cdot(q_j\times r_{ij})}
{|r_{ij}|^5}.
}
\]

For a single closed polygon made from only three straight vortex elements,

\[
q_1+q_2+q_3=0.
\]

Hence the three segment vectors are coplanar. Their midpoints and midpoint-separation vectors are in the same plane. Therefore the scalar triple product in every pairwise longitudinal-stretch term vanishes:

\[
 t_i\cdot(q_j\times r_{ij})=0.
\]

Thus the three-edge single-loop version of the cyclic-relay idea cannot realize genuinely three-dimensional mutual longitudinal stretching in this discrete model. Three arbitrary *unconnected* vortex elements can do so, but that is not yet the user's requested "one closed system chasing its own tail." A nonplanar single closed polygon requires at least four edges, and a smooth closed filament can of course contain arbitrarily many interacting arcs.

This is a geometric closure constraint, not a Navier–Stokes theorem.

# CHECKPOINT 61 — A smooth closed four-arc relay CAN exist transiently

To test the actual closed-system loophole rather than assume it away, a single smooth closed filament was represented by a low-order Fourier curve and divided into four material arcs \(A_0,A_1,A_2,A_3\). The curve was evolved by a regularized nonlocal Biot–Savart filament model

\[
\partial_t X(\theta)
=\frac{\Gamma}{4\pi}
\int
\frac{X_{\theta'}(\theta')\times[X(\theta)-X(\theta')]}
{(|X(\theta)-X(\theta')|^2+a^2)^{3/2}}\,d\theta'.
\]

The shape was searched adversarially for the conditions

\[
\overline\alpha_{A_3\to A_0}>0,\quad
\overline\alpha_{A_0\to A_1}>0,\quad
\overline\alpha_{A_1\to A_2}>0,\quad
\overline\alpha_{A_2\to A_3}>0
\]

while the global squared radius of gyration obeyed

\[
\frac{d}{dt}R_g^2<0.
\]

Such a state was found. At \(t=0\), with \(R_g=1\) and regularization core \(a=0.15\), the four cyclic arc-averaged stretch rates were

\[
(0.04430088,\ 0.04022682,\ 0.06687026,\ 0.05891911),
\]

while

\[
\frac{d}{dt}R_g^2=-0.14597584.
\]

Therefore the strong statement

> "a closed vortex cannot internally outsource stretching around a cycle at all"

is false even in a single-filament model. A closed four-link relay can exist for a finite interval.

This is an important adversarial correction: the remaining conjecture must concern **failure to sustain an infinite shrinking relay**, not impossibility of a transient relay.

# CHECKPOINT 62 — In the closed-loop test the relay self-detunes before large gain

The same optimized curve was integrated forward with \(N=80\) material points and fixed core \(a=0.15\). All four cyclic links remained positive while \(R_g^2\) continued to contract until approximately

\[
\boxed{t\simeq1.21.}
\]

At that time the cyclic stretch rates were still positive,

\[
(0.02679,\ 0.05909,\ 0.07744,\ 0.06301),
\]

but

\[
\frac{d}{dt}R_g^2
\]

had changed sign. In other words, **the cyclic stretch relay survived, but the collapsing state did not.**

The initial rms speed was approximately \(0.37516\), so the crude turnover time \(R_g/u_{\rm rms}\) was approximately \(2.6655\). Loss of contraction therefore occurred after only about \(0.45\) turnover times.

During that interval the dimensionless shape-complexity measure

\[
\chi=\frac{L}{R_g}
\]

rose from

\[
10.3422
\]

to approximately

\[
12.45,
\]

a growth of about \(20.4\%\). The accumulated cyclic logarithmic stretch gave only modest multiplicative gains,

\[
(1.0403,\ 1.0667,\ 1.0957,\ 1.0680),
\]

before global contraction stalled.

This is not evidence sufficient for a theorem, because a different shape or higher-dimensional internal relay may behave differently. It is nevertheless exactly the failure mode the geometric intuition predicts: the closed system can temporarily pass strain around the loop, but doing so deforms the geometry until the collective inward motion loses coherence.

The reproducible numerical test is saved as:

- `checkpoint_60_closed_relay_test.py`
- `checkpoint_60_closed_relay_test.txt`
- `checkpoint_60_closed_relay_trace.csv`

# CHECKPOINT 63 — Important literature stress test: centerline collapse can occur, but the core may fail to keep up

The closed-relay idea has a known adversarial precedent. Pelz constructed a high-symmetry vortex-filament model with six closed vortex contours whose centerline geometry approaches a locally self-similar finite-time collapse. Kimura later studied related straight-filament collapse models. Thus **closed internal Biot–Savart geometry by itself is capable of organizing a centerline collapse in reduced filament models**.

That prevents any honest argument of the form "closed self-interaction can never geometrically collapse."

However, Hormoz and Brenner (JFM 707, 2012) analyzed the missing finite-core consistency. Their central requirement is that the physical vortex-core radius remain asymptotically smaller than the geometric scales of filament separation and curvature. In their interacting-filament asymptotics, the centerline separation can collapse like \((T-t)^{1/2}\) while the core does not shrink fast enough to remain a filament. They identify an antagonism between the stretching rate required to shrink the core and the curvature/self-interaction dynamics required to maintain the collapsing filament geometry. Their paper states that the self-similar argument generalizes naturally to multiple interacting filaments and also develops a non-self-similar extension.

Their result is not a rigorous global Navier–Stokes regularity theorem, and it is principally an Euler/filament asymptotic analysis. But it lands extremely close to the refined working conjecture here:

> **A closed internal strain relay may collapse its centerline geometry, yet fail to maintain the transverse/core concentration required for singular vorticity.**

For Navier–Stokes, viscous spreading adds an additional core-expansion mechanism rather than removing this consistency problem.

# CHECKPOINT 64 — Conserved impulse further forces a concentrating core to become multipolar/locally self-contained

For sufficiently localized unforced flow on \(\mathbb R^3\), the hydrodynamic impulse

\[
I=\frac12\int x\times\omega\,dx
\]

is conserved; this remains true in the viscous case under the standard decay assumptions. For a thin closed filament,

\[
I\approx\frac{\Gamma}{2}\oint X\times dX,
\]

i.e. circulation times the oriented vector area.

Under Navier–Stokes critical point scaling, a core of radius \(r\) has the schematic scales

\[
|u|\sim \frac{\nu}{r},\qquad
|\omega|\sim\frac{\nu}{r^2},\qquad
\text{Vol}\sim r^3,
\]

so its impulse contribution scales only as

\[
\boxed{I_r\sim \nu r^2\to0.}
\]

Thus a singular point-scale core cannot carry a fixed nonzero fraction of the total impulse all the way down. Any nonzero global impulse must remain in larger-scale vorticity. Earlier energy/Biot–Savart estimates in this notebook show that a fixed coarse component cannot deliver order-one critical stretching to arbitrarily small scales without an increasingly prohibitive dissipation cost. Therefore an admissible terminal cascade is pushed toward a **locally low-impulse, multipolar cluster** whose active strain sources descend along with the core.

This does not eliminate such clusters; indeed high-symmetry filament candidates such as the Pelz dodecapole are precisely multipolar constructions. It does, however, remove another easy version of "one coherent ring shrinks itself to a point while retaining all of its large-scale dynamical identity."

# CHECKPOINT 65 — Updated verdict after the closed-relay experiment

The closed-system test changes the wording, but not the direction, of the project.

What is now false:

> A closed unforced vortex cannot internally generate a positive cyclic strain relay.

It can, transiently.

What survives:

> A coherent finite-core vortex system appears unable to **sustain** the relay through an infinite shrinking hierarchy while simultaneously keeping its core thinner than the collapsing geometric scales and maintaining the positive stretching required for vorticity blowup.

The most dangerous remaining candidate is therefore not a simple ouroboros and not even a fixed finite relay. It is a scale-changing multipolar network that repeatedly reorganizes before geometric depletion, core deformation, viscous spreading, or reconnection shuts down the current relay.

That is now the proper adversarial object for the next stage.

## References added at this checkpoint

26. R. B. Pelz, *Locally self-similar, finite-time collapse in a high-symmetry vortex filament model*, Phys. Rev. E 55 (1997), 1617. DOI: 10.1103/PhysRevE.55.1617.
27. Y. Kimura, *Self-similar collapse of a 3D straight vortex filament model*, Geophys. Astrophys. Fluid Dyn. 103 (2009), 135–142. DOI: 10.1080/03091920802357742.
28. S. Hormoz and M. P. Brenner, *Absence of singular stretching of interacting vortex filaments*, J. Fluid Mech. 707 (2012), 191–204. DOI: 10.1017/jfm.2012.270.
29. S. Hormoz, M. P. Brenner et al., *Non-Universal and Non-Singular Asymptotics of Interacting Vortex Filaments*, Procedia IUTAM 7 (2013), 97–106. DOI: 10.1016/j.piutam.2013.03.012.

# CHECKPOINT 66 — Finite-core augmentation of the closed four-arc relay

The next adversarial test couples the previously found closed four-arc Biot–Savart relay to a minimal viscous transverse-core model instead of holding the filament regularization radius fixed.

For material arc \(j\), let

\[
b_j=a_j^2
\]

be its transverse second-moment/core-radius scale and let \(\sigma_j\) be the arc-averaged **total** longitudinal stretching rate generated by the whole closed filament. The reduced core law is

\[
\boxed{\dot b_j=-\sigma_j b_j+4\nu.}
\]

Each source arc is then regularized in the Biot–Savart kernel using its instantaneous radius \(a_j=\sqrt{b_j}\), so the geometric motion and core evolution are coupled. This is still a coherent-core filament model, **not** a Navier–Stokes DNS and not a proof.

The circulation is normalized to \(\Gamma=1\), so \(Re_\Gamma=1/\nu\). Initial \(a/R_g=0.15\).

The sweep used

\[
Re_\Gamma=\infty,\ 10^4,\ 4000,\ 1000,\ 100.
\]

Results:

- In every run the previously found cyclic positive-strain relay again exists only transiently; global contraction stalls/reverses at finite time.
- At \(Re_\Gamma=4000\), the minimum \(R_g^2\) occurs at \(t\approx1.115\), with arcwise \(a/R_g\approx(0.1458,0.1647,0.1531,0.1439)\). Thus the finite cores remain nonzero and comparable to their starting relative thickness while the contraction dies.
- At \(Re_\Gamma=1000\), the minimum-scale ratios are roughly \((0.1570,0.1756,0.1642,0.1555)\).
- At \(Re_\Gamma=100\), viscous spreading is strong enough that \(\max(a/R_g)\) passes \(0.25\) well before the contraction stalls; at the minimum geometric size the ratios are approximately \((0.271,0.287,0.277,0.273)\).
- At very high \(Re_\Gamma\), some arcs become relatively thinner after the geometric contraction has already failed, because later positive stretching continues during re-expansion. This is not a collapsing singular relay.

The coupled experiment therefore does **not** produce a finite-core collapse. It reproduces the previous geometric failure and adds the expected viscous tendency for the transverse core to become increasingly important at lower circulation Reynolds number.

Reproducible outputs:

- `checkpoint_66_finite_core_relay.py`
- `checkpoint_66_finite_core_relay.txt`
- `checkpoint_66_trace_Re*.csv`

---

# CHECKPOINT 67 — Exact core-to-geometry ratio equation in the comparable-scale collapse model

The finite-core obstruction can be stated analytically.

Let \(R\) be the characteristic geometric collapse scale, \(b=a^2\) the core second-moment width, and \(\Gamma\) the circulation scale. Assume a comparable-scale closed relay has

\[
\frac{dR^2}{dt}=-2c_g\Gamma,
\]

and axial stretching

\[
\sigma=\frac{c_s\Gamma}{R^2},
\]

with dimensionless geometric coefficients \(c_g,c_s>0\). Couple this to

\[
\dot b=-\sigma b+4\nu.
\]

Set

\[
y=\frac{b}{R^2}=\left(\frac aR\right)^2,
\qquad
\tau=-\log\frac{R^2}{R_0^2}.
\]

Then direct differentiation gives

\[
\boxed{
\frac{dy}{d\tau}
=
\frac{2\nu}{c_g\Gamma}
+
\left(1-\frac{c_s}{2c_g}\right)y.
}
\]

Define

\[
\lambda=\frac{c_s}{2c_g}.
\]

Three cases follow exactly inside this model.

### Case 1: \(\lambda<1\)

The geometric scale collapses faster than stretching can narrow the core. Then \(y\) grows exponentially in logarithmic collapse time. The filament approximation is lost.

### Case 2: \(\lambda=1\)

\[
\frac{dy}{d\tau}=\frac{2\nu}{c_g\Gamma}>0,
\]

so \(y\) grows linearly. Again the core catches the geometric scale.

### Case 3: \(\lambda>1\)

Stretching is strong enough to narrow the core faster than geometric collapse would by itself, but viscosity creates a positive attracting fixed point

\[
\boxed{
y_*
=
\frac{4\nu}{(c_s-2c_g)\Gamma}>0.}
\]

Therefore

\[
\boxed{
\frac aR\longrightarrow
\sqrt{\frac{4\nu}{(c_s-2c_g)\Gamma}}
\neq0
}
\]

for finite \(\Gamma/\nu\).

This is the important result: **even when stretching wins strongly enough to keep narrowing the core, a comparable-scale self-similar viscous relay does not become asymptotically filamentary. It approaches a finite relative core thickness.**

An illustrative phase table and repeated-shrink calculation are saved in `checkpoint_67_core_ratio_phase.py/.txt`.

---

# CHECKPOINT 68 — Conditional finite-core no-slenderness lemma

The same obstruction can be stated without assuming an exact constant-rate self-similar solution.

Assume over a coherent collapsing episode that the core width obeys the moment inequality/model

\[
\dot b\ge -\sigma b+c_\nu\nu,
\qquad c_\nu>0,
\]

and that the self-generated axial strain has the comparable-scale bound

\[
\sigma\le C\frac{\Gamma}{R^2}
\]

with a scale-independent dimensionless geometry coefficient \(C<\infty\).

If the core is actually shrinking at some sufficiently late time, \(\dot b<0\), then necessarily

\[
\sigma b>c_\nu\nu.
\]

Combining the inequalities gives

\[
C\frac{\Gamma}{R^2}b>c_\nu\nu,
\]

hence

\[
\boxed{
\left(\frac aR\right)^2
=
\frac b{R^2}
>
\frac{c_\nu}{C}\frac{\nu}{\Gamma}.
}
\]

Thus a finite-circulation-Reynolds-number coherent relay with bounded dimensionless geometry cannot have

\[
a/R\to0
\]

while its core continues shrinking.

This is a **conditional finite-core lemma**, not a theorem for arbitrary Navier–Stokes solutions. The unproved PDE-level step is the existence of a sufficiently coherent transverse moment obeying the stated diffusion inequality through arbitrary 3-D deformation/reconnection.

---

# CHECKPOINT 69 — What a singular relay must do to evade the finite-core lemma

The conditional lemma leaves only a short list of exits.

A collapsing candidate must make at least one of the following fail:

1. **Bounded geometry coefficient:** \(C\to\infty\). This means a new smaller internal separation/curvature scale develops inside the nominal scale \(R\); the candidate is no longer a one-scale relay.
2. **Finite circulation Reynolds number:** \(\Gamma/\nu\to\infty\) along the cascade.
3. **Coherent-core description:** the structure ceases to possess a one-sign/coherent tube cross-section, for example through reconnection, severe anisotropy, cancellation, or a fully three-dimensional thick-core state.
4. **Persistent contraction:** the geometry stalls or re-expands, as happened in the explicit four-arc relay experiment.

The second exit is not supplied merely by Navier–Stokes scaling. Under

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\]

circulation is scale invariant:

\[
\oint u_\lambda\cdot dx
=
\oint u\cdot dy.
\]

Hence \(\Gamma/\nu\) is also invariant under ordinary parabolic rescaling. A self-similar cascade does not acquire increasing \(Re_\Gamma\) simply by getting smaller.

Therefore a finite-core singular candidate must either build an **increasingly singular dimensionless geometry** or reorganize circulation/branch structure in a genuinely non-self-similar fashion.

This pushes the remaining escape hatch away from a fixed closed relay and toward a hierarchy-within-a-hierarchy.

---

# CHECKPOINT 70 — Status: the finite-core self-similar relay is effectively slain; Type-II/multiscale escape remains

Combining the closed-relay experiment, the finite-core augmentation, and the ratio equation gives the strongest status yet.

A fixed-shape/comparable-scale closed internal relay may transiently outsource stretching around itself, but:

- its explicit four-arc realization loses geometric contraction before large amplification;
- adding viscous core dynamics does not rescue that collapse;
- in the idealized comparable-scale collapse equations, the core-to-geometry ratio either grows or approaches a positive viscosity-controlled floor;
- ordinary Navier–Stokes scaling cannot drive that floor to zero because \(\Gamma/\nu\) is scale invariant;
- this agrees in spirit with Hormoz–Brenner's conclusion that centerline collapse and core evolution are antagonistic in interacting-filament singularity scenarios.

Accordingly, the remaining adversary is **not** a self-similar finite-core ouroboros or fixed finite closed relay.

It must be a non-self-similar/Type-II multiscale object in which the dimensionless geometry coefficient itself grows without bound, or in which new branches/separations are continually created at scales below the nominal collapsing core.

That does not prove global regularity. It does, however, remove the specific finite-core comparable-scale relay as a credible terminal blowup mechanism within the assumptions tested here.

### Status callout

> **Slain at this checkpoint:** fixed-shape or bounded-geometry finite-core closed relays that require \(a/R\to0\) while collapsing at finite circulation Reynolds number.
>
> **Still alive:** genuinely non-self-similar multiscale point concentration with unbounded dimensionless geometry, changing branch count/topology, or loss of the coherent-core description.


---

# CHECKPOINT 71 — Renormalized Z-space: periodicity is the right question, but boundedness is even better

For a scale-homogeneous vortex-filament model with centerline position \(X(t)\), center \(C(t)\), and radius of gyration

\[
R^2(t)=\langle |X-C|^2\rangle,
\]

write

\[
Y=\frac{X-C}{R},\qquad \langle |Y|^2\rangle=1.
\]

When the physical core regularization scales with the geometry, \(a=\varepsilon R\), Biot–Savart velocity has the homogeneity

\[
V(RY;\varepsilon R)=R^{-1}V(Y;\varepsilon).
\]

Define logarithmic scale time by

\[
\frac{ds}{dt}=\frac{1}{R^2}
\]

(with circulation normalized to one in the toy model). Then the normalized shape satisfies the autonomous equation

\[
\boxed{
\partial_s Y=V(Y)-\overline V-\rho(Y)Y,
}
\]

where

\[
\rho(Y)=\langle Y\cdot(V-\overline V)\rangle,
\qquad
\frac{d\log R}{ds}=\rho(Y).
\]

This turns candidate singular behavior into dynamical-systems language:

- fixed \(Y_*\) with \(\rho(Y_*)<0\): continuous self-similar collapse;
- periodic \(Y(s+P)=Y(s)\) with negative mean \(\rho\): discrete self-similar collapse;
- bounded recurrent/nonperiodic orbit with negative mean \(\rho\): bounded Type-II-like renormalized dynamics;
- unbounded \(Y\)-state: some dimensionless geometric variable must diverge and becomes the next scale to chase.

This is the clean formal version of the proposed \(Z(s)\) interrogation.

---

# CHECKPOINT 72 — Explicit Z-space relay run: no fixed point or temporal cycle; contraction is lost

The four-arc closed relay from Checkpoint 60 was integrated directly in the normalized equation above with fixed relative regularization \(\varepsilon=0.15\), periodically reparameterizing the curve by arclength to control marker bunching.

Run parameters:

\[
N=80,\qquad \Delta s=0.005,\qquad s_{\max}=30.
\]

Results:

\[
\rho(0)=-0.07299,
\qquad
\rho(30)=+0.22727,
\]

and

\[
\langle \rho\rangle_{0\le s\le30}=+0.16223.
\]

The last half of the run had no negative-\(\rho\) samples. The cumulative scale exponent was

\[
\int_0^{30}\rho(s)\,ds\approx4.871>0,
\]

so this orbit is emphatically not a renormalized collapsing attractor.

The normalized length changed from

\[
L/R_g=10.34
\]

to values around \(40\)-\(50\). Rotation/cyclic-shift Procrustes checks on candidate recurrence times gave order-one shape distances, not near returns. A principal-component autocorrelation also failed to show a credible positive long-time period.

Thus the explicit closed relay does not settle to a fixed point or log-periodic orbit. It escapes by generating increasing normalized geometric complexity and loses net global contraction.

Files: `checkpoint_71_zspace_relay.py`, `checkpoint_71_zspace_trace.csv`, `checkpoint_71_zspace_results.txt`.

---

# CHECKPOINT 73 — Thin-core sweep: loss of global contraction is robust before core overlap

Because \(\varepsilon=0.15\) is too large to represent an embedded slender tube for the initial optimized curve, the normalized experiment was repeated at genuinely thinner relative regularizations

\[
\varepsilon=0.01,\ 0.02,\ 0.03,\ 0.035.
\]

Using an approximate geometric reach

\[
\operatorname{reach}(Y)
\approx
\min\left\{\kappa_{\max}^{-1},\frac12 d_{\min,\mathrm{nonlocal}}\right\},
\]

the first loss of global contraction, \(\rho\ge0\), occurred at essentially the same normalized time in every run:

\[
s\approx0.675\text{--}0.683.
\]

For \(\varepsilon=0.01\), the tube remained geometrically thinner than the estimated reach through that first loss of contraction. For \(\varepsilon=0.02\) and above, the first core/reach conflict occurred later than the first expansion transition.

Hence the initial failure of the collapsing relay is not simply an artifact of using a fat regularization core.

Files: `checkpoint_73_zspace_core_sweep.py/.csv/.txt`.

---

# CHECKPOINT 74 — The orbit escapes into a smaller local scale: global radius of gyration is not the terminal scale

The \(\varepsilon=0.01\) run was extended to \(s=5\). It again lost global contraction near

\[
s\approx0.675,
\]

but later developed intermittent very small geometric reach even while \(\rho>0\) most of the time.

Examples in \(R_g=1\) units:

\[
\operatorname{reach}\approx0.0167\quad(s=0.975),
\]

\[
\operatorname{reach}\approx0.00589\quad(s=1.62),
\]

and the minimum sampled reach was approximately

\[
0.00406.
\]

Thus the normalized orbit did not approach a global collapsing attractor; instead it generated **subscale self-approaches inside a globally noncollapsing configuration**.

This is exactly the Type-II/multiscale escape anticipated at Checkpoint 70. The next geometrically meaningful scale is therefore not \(R_g\) but a local reach/separation/curvature scale \(\delta\ll R_g\).

The low-reach events were irregular rather than temporally periodic in the sampled logarithmic time. Once \(\delta\) approached the imposed core radius, however, the centerline filament description ceased to represent an embedded physical tube, so later low-reach recurrences cannot be interpreted as coherent-vortex-tube dynamics without adding finite-core/reconnection physics.

Files: `checkpoint_74_zspace_eps001.py`, traces, shapes, and reach analysis.

---

# CHECKPOINT 75 — Compact-Z finite-core obstruction: periodicity is not actually required

The core-ratio equation from Checkpoints 66–69 generalizes cleanly along an arbitrary renormalized trajectory.

Let

\[
y=\frac{a^2}{R^2},
\]

let normalized axial strain satisfy

\[
\sigma=\frac{\Gamma}{R^2}\widehat\sigma(s),
\]

and use dimensionless scale time

\[
\frac{ds}{dt}=\frac{\Gamma}{R^2}.
\]

With the coherent-core moment model

\[
\dot a^2=-\sigma a^2+c_\nu\nu
\]

and

\[
\frac{dR^2}{dt}=2\Gamma\rho(s),
\]

one obtains the exact scalar relation within that model

\[
\boxed{
\frac{dy}{ds}
+
\beta(s)y
=
\frac{c_\nu}{Re_\Gamma},
\qquad
\beta(s)=\widehat\sigma(s)+2\rho(s),
\qquad
Re_\Gamma=\frac{\Gamma}{\nu}.
}
\]

Its integrating-factor solution is

\[
y(s)=e^{-B(s)}\left[
y(0)+\frac{c_\nu}{Re_\Gamma}
\int_0^s e^{B(\tau)}d\tau
\right],
\qquad
B(s)=\int_0^s\beta(\tau)d\tau.
\]

Now suppose the renormalized coherent-tube state remains in a compact region where

\[
\beta(s)\le B_{\max}<\infty.
\]

Then comparison gives

\[
\boxed{
y(s)\ge y(0)e^{-B_{\max}s}
+
\frac{c_\nu}{B_{\max}Re_\Gamma}
\left(1-e^{-B_{\max}s}\right)
}
\]

for \(B_{\max}>0\). Consequently

\[
\boxed{
\liminf_{s\to\infty}\frac{a^2}{R^2}
\ge
\frac{c_\nu}{B_{\max}Re_\Gamma}>0.
}
\]

If \(B_{\max}\le0\), diffusion makes \(y\) grow instead.

This is stronger than checking fixed points or periodic orbits individually:

> **Any bounded/compact renormalized coherent-tube dynamics — fixed, periodic, quasiperiodic, recurrent, or chaotic — cannot drive the relative core thickness to zero at finite circulation Reynolds number unless the normalized strain coefficient itself becomes unbounded.**

Thus temporal periodicity is not the decisive gate. Boundedness of the normalized state is enough for the finite-core obstruction.

The remaining coherent-tube escape must therefore satisfy

\[
\boxed{
\sup_s \widehat\sigma(s)=\infty
}
\]

or lose the coherent-core description / finite \(Re_\Gamma\).

---

# CHECKPOINT 76 — Full Navier–Stokes has an even stronger rigorous bounded-Z gate: the critical \(L^3\) norm

The previous checkpoint is conditional on the coherent-core moment reduction. Full 3-D Navier–Stokes supplies a rigorous scale-critical obstruction independent of that model.

Under Navier–Stokes scaling

\[
u_\lambda(x,t)=\lambda u(\lambda x,\lambda^2t),
\]

the spatial \(L^3\) norm is invariant:

\[
\|u_\lambda(t)\|_{L^3}=\|u(\lambda^2t)\|_{L^3}.
\]

Escauriaza–Seregin–Šverák proved endpoint regularity for solutions bounded in

\[
L^\infty_tL^3_x.
\]

Therefore a finite-time singularity cannot have a renormalized trajectory that remains bounded in a state space controlling the critical \(L^3\) norm. At minimum,

\[
\boxed{
\limsup_{t\uparrow T}\|u(t)\|_{L^3}=\infty.
}
\]

Thus any genuinely bounded self-similar, discretely self-similar, periodic-in-log-time, or compact recurrent renormalized profile lying in the relevant \(L^3\) class is excluded. Chae additionally proved nonexistence of locally asymptotically discretely self-similar Navier–Stokes blowup for time-periodic profiles in \(C^1_t(L^3_x\cap C^2_x)\).

This substantially clarifies the research strategy:

> **We do not need to wait for temporal periodicity. If the full renormalized state is bounded in a critical norm, existing Navier–Stokes regularity theory already kills the blowup. A surviving singularity must make a scale-invariant quantity itself diverge.**

This converts the question “does \(Z(s)\) become periodic?” into the stronger interrogation:

\[
\boxed{
\text{Which critical component of }Z(s)\text{ is forced to become unbounded?}
}
\]

The explicit toy relay answers geometrically: it escapes global-scale compactness by generating smaller reach/separation scales. Full Navier–Stokes says that a genuine blowup must ultimately also escape boundedness in a critical velocity norm such as \(L^3\).

---

# CHECKPOINT 77 — Revised target after the Z-space run

At this stage the candidate is no longer allowed to hide in any repeatable bounded mechanism.

A terminal blowup would have to exhibit all of the following:

1. no bounded fixed/periodic/recurrent renormalized profile in a critical regularity class;
2. divergence of a scale-invariant quantity, in particular critical velocity concentration;
3. continual creation of smaller geometric scales \(\delta/R\to0\) or an equivalent unbounded normalized strain coefficient;
4. finite-core dynamics that either cease to be coherent-tube dynamics or continually reorganize before core overlap/reconnection regularizes the centerline picture.

So the next variable is **not time-periodicity**. It is the unbounded critical concentration hidden inside the shrinking local scale.

The most natural next attack is to renormalize a second time on the local reach/separation scale \(\delta(t)\), rather than on global \(R_g(t)\), and ask whether the \(\delta\)-normalized local state can remain bounded. If it can, critical-norm/ancient-limit machinery becomes available. If it cannot, the next diverging normalized quantity is exposed.


---

# CHECKPOINT 78 — Correction: the first local-reach diagnostic was wrong

A code audit found an indentation error in the original checkpoint-74 `reach()` routine: it returned from inside the outer loop that was supposed to exclude neighboring nodes around *every* filament vertex. As a result, the global minimum distance still included near-neighbor pairs almost everywhere on the curve.

Consequences:

- the previously highlighted very small half-separation/reach values from checkpoint 74 are **not valid evidence** of a newly generated physical subscale;
- the statement that the `eps=0.01, N=80` run had clearly escaped global-scale failure by manufacturing a resolved local scale is retracted;
- the old thin-core run was also under-resolved, because node spacing was much larger than the regularization core.

The original files are retained for forensic reproducibility, but checkpoints 71–74 are now explicitly exploratory/superseded for quantitative reach claims.

# CHECKPOINT 79 — Corrected reach convergence test

The reach calculation was repaired by excluding an arclength-neighbor band around **all** nodes before evaluating the minimum nonlocal pair separation.

Re-running the old `eps=0.01` Z-space model at `N=80,120,160` showed strong resolution dependence in both the first expansion time and the first apparent core/reach encounter. This confirms that the old tiny-core trajectory was not numerically converged.

The correct lesson is therefore methodological: the local ruler must be resolved relative to both node spacing and regularization/core radius before a putative subscale escape is interpreted physically.

# CHECKPOINT 80 — Search for a reach-safe closed relay

To avoid building the next test on an already over-curved filament, a deterministic search over low Fourier-mode closed curves was performed. The objective required simultaneously:

- all four cyclic stretching links positive,
- global radius-of-gyration contraction,
- and substantially larger local geometric reach.

Many feasible shapes were found. A selected candidate retained, after refinement to higher resolution, approximately

\[
\rho<0,\qquad \min_i\alpha_{i-1\to i}>0,
\qquad \delta_{\rm reach}\approx 0.10.
\]

This supplied a cleaner initial condition for the relay test.

# CHECKPOINT 81 — Better-resolved Z-space relay

The selected candidate was evolved with

\[
N=256,\qquad a_{\rm reg}=0.05,
\]

so that initial node spacing was smaller than the core regularization and the core was initially inside the geometric reach.

Initial values were approximately

\[
\rho=-0.01527,
\]

with all four cyclic stretching rates positive and minimum cyclic rate about `0.02898`. Initial reach was

\[
\delta\approx0.10084,
\qquad a/\delta\approx0.496.
\]

The first loss of simultaneous

\[
\text{global contraction} + \text{all cyclic links positive}
\]

occurred at

\[
\boxed{s\approx0.450}.
\]

At that time the reach had **increased** to approximately

\[
\delta\approx0.1422>a=0.05.
\]

Thus the relay failed before any finite-core contact.

A later tiny separation occurs only after the system has already ceased being a collapsing relay. The first `core >= reach` event is around `s≈1.695`, at which point the global gauge is expanding and some cyclic links are negative. That later folding is not evidence for a singular collapsing cascade.

# CHECKPOINT 82 — Resolution/core sweep

The same reach-safe candidate was tested with progressively thinner cores and higher resolution:

\[
(N,a)=(256,0.05),\ (320,0.04),\ (384,0.03).
\]

The first relay/contraction failures occurred at approximately

\[
0.450,\quad0.435,\quad0.375,
\]

respectively.

At those failure times the geometric reach remained approximately

\[
0.142,\quad0.161,\quad0.163,
\]

all well above the corresponding core radii.

So within this tested family, making the core thinner does not reveal a persistent collapsing cyclic relay. The relay loses the required dynamical combination before finite-core overlap.

This is numerical evidence in a reduced regularized-filament model, not a Navier–Stokes theorem.

# CHECKPOINT 83 — The local-scale gate

The previous global-scale core-ratio argument can be repeated using the *actual active local scale* \(\delta(t)\), such as local reach.

Assume a coherent transverse core width

\[
b=a^2
\]

satisfies a strain-diffusion inequality/model

\[
\dot b\ge -\sigma b+c_\nu\nu,
\]

where \(\sigma\) is the relevant axial stretching rate and \(c_\nu>0\) is an order-one diffusion constant.

Define

\[
y=\frac{b}{\delta^2},
\qquad
\gamma=-\frac{\dot\delta}{\delta}.
\]

Then

\[
\boxed{
\dot y
\ge
\frac{c_\nu\nu}{\delta^2}
+(2\gamma-\sigma)y.
}
\]

Introduce local nonlinear scale-time through

\[
\frac{ds}{dt}=\frac{\Gamma_\delta}{\delta^2},
\]

and define

\[
Re_\delta=\frac{\Gamma_\delta}{\nu},
\qquad
A_\delta=\frac{(\sigma-2\gamma)\delta^2}{\Gamma_\delta}.
\]

Then

\[
\boxed{
\frac{dy}{ds}
\ge
\frac{c_\nu}{Re_\delta}
-A_\delta y.
}
\]

This exposes the next escape cleanly.

If, along an infinite coherent cascade,

\[
Re_\delta\le R_*<\infty,
\qquad
A_\delta\le A_*<\infty,
\]

then comparison with the forced linear ODE prevents

\[
y=\frac{a^2}{\delta^2}\to0.
\]

In particular, for positive \(A_*\), the asymptotic floor is of order

\[
\boxed{
y\gtrsim \frac{c_\nu}{A_*R_*}.}
\]

Thus a coherent finite-core singular cascade must make at least one dimensionless quantity escape every bounded renormalized state:

1. \(Re_\delta\to\infty\): unbounded local scale-critical circulation/amplitude;
2. \(A_\delta\to\infty\): unbounded normalized stretching advantage over the geometric collapse rate;
3. or the coherent-tube description itself fails through reconnection, cancellation, sheet/point concentration, etc.

This is a sharper statement than the earlier search for temporal periodicity. A bounded renormalized state—fixed, periodic, quasiperiodic, chaotic, or merely recurrent—is insufficient inside this coherent-core reduction. A genuine escape must be **unbounded in a scale-invariant variable**.

## Updated status

The corrected numerics no longer show the toy closed relay escaping by a resolved shrinking local ruler while still collapsing. The next adversarial target is therefore not another finite-dimensional periodic relay. It is a Type-II mechanism capable of driving \(Re_\delta\) or \(A_\delta\) to infinity, or abandoning coherent-vortex-tube geometry altogether.

# CHECKPOINT 84 — The two escape variables collapse to a product gate

Checkpoint 83 left two coherent-tube escape variables,

\[
Re_\delta=\frac{\Gamma_\delta}{\nu},
\qquad
A_\delta=\frac{(\sigma-2\gamma)\delta^2}{\Gamma_\delta},
\]

inside the local core comparison

\[
\frac{dy}{ds}\ge \frac{c_\nu}{Re_\delta}-A_\delta y,
\qquad
 y=\frac{a^2}{\delta^2}.
\]

They are not independent once the core is actually trying to become thinner relative to the active geometry. If

\[
\frac{dy}{ds}\le0,
\]

then necessarily

\[
0\ge \frac{c_\nu}{Re_\delta}-A_\delta y,
\]

hence

\[
\boxed{A_\delta Re_\delta y\ge c_\nu.}
\]

Equivalently,

\[
\boxed{A_\delta Re_\delta\ge\frac{c_\nu}{y}}
\]

and, after substituting the definitions,

\[
\boxed{\frac{(\sigma-2\gamma)a^2}{\nu}\ge c_\nu.}
\]

Thus if

\[
\frac a\delta\to0
\]

through intervals on which the relative core is nonincreasing, the product

\[
A_\delta Re_\delta
\]

must diverge at least as fast as

\[
\frac{\delta^2}{a^2}.
\]

This is a useful reduction. The coherent-core escape is not “large normalized strain *or* large circulation” in an unconstrained sense. The flow must generate enough **core-scale strain Reynolds number** to keep pace with diffusion.

For the illustrative second-moment coefficient `c_nu=4`, the minimum product required at

\[
y=10^{-1},10^{-2},\ldots,10^{-6}
\]

is

\[
40,400,4000,\ldots,4\times10^6.
\]

This is still a conditional core-model statement, not a full-PDE estimate.

# CHECKPOINT 85 — Remote pusher scaling and the new-ruler dichotomy

Suppose the positive axial strain needed by the target core is supplied by another coherent vortex structure a distance `d` away, with a Biot–Savart scaling bound of the schematic form

\[
\sigma_s\lesssim C\frac{\Gamma_s}{d^2}.
\]

Combining this with the core-scale requirement

\[
\frac{\sigma_s a^2}{\nu}\gtrsim c_\nu
\]

gives

\[
\boxed{
Re_s=\frac{\Gamma_s}{\nu}
\gtrsim
\frac{c_\nu}{C}\left(\frac d a\right)^2.
}
\]

Therefore a source which remains at the outer active scale

\[
d\sim\delta
\]

while

\[
a/\delta\to0
\]

must make its scale-critical circulation grow like

\[
Re_s\gtrsim \frac1y.
\]

The other option is to move the source inward until

\[
d=O(a).
\]

But then the source has entered the core scale. The old outer ruler `delta` is no longer the correct scale for the interaction; the analysis must be renormalized on the newly generated smaller ruler.

This converts the large-`A_delta` escape into a more geometric dichotomy:

1. **critical amplitude escape:** the circulation/amplitude grows without bound at the active scale; or
2. **renormalization escape:** a new smaller interaction scale is created, and the same question restarts there.

Under the coherent single-scale estimate

\[
U_\delta\sim\frac{\Gamma_\delta}{\delta},
\]

a blob occupying order `delta^3` has local critical size

\[
\|u\|_{L^3(B_\delta)}\sim U_\delta\delta\sim\Gamma_\delta.
\]

Thus unbounded `Re_delta` is the reduced-model version of unbounded scale-critical velocity amplitude. This is consistent with the rigorous full-PDE result of Seregin (2012): a genuine finite-time blowup must satisfy

\[
\lim_{t\uparrow T}\|u(t)\|_{L^3(\mathbb R^3)}=\infty.
\]

Reference: G. Seregin, *A Certain Necessary Condition of Potential Blow up for Navier-Stokes Equations*, Comm. Math. Phys. 312 (2012), 833–845, DOI `10.1007/s00220-011-1391-x`, arXiv:1104.3615.

This connection does not prove that `Re_delta` and the global `L^3` norm are equivalent for arbitrary multiscale flows. It identifies where the present geometric program meets a known necessary critical-norm escape.

# CHECKPOINT 86 — Instrumenting the resolved relay with the escape gate

The reach-safe relay from checkpoints 80–82 was instrumented more aggressively.

The physical local ruler is

\[
\delta_{\rm phys}=R\,\delta_Z,
\]

and in the normalized scale time the physical local shrink rate becomes

\[
\widehat\gamma
=
-\frac{d}{ds}\log\delta_{\rm phys}
=
-\left(\rho+\frac{d}{ds}\log\delta_Z\right).
\]

The diagnostic then evaluates

\[
A_\delta=(\widehat\sigma-2\widehat\gamma)\delta_Z^2
\]

under the filament normalization `Gamma=1`.

Three choices of available stretching were distinguished:

1. stretching exactly at the point or pair defining the reach;
2. the best stretching within two reach lengths of that local ruler;
3. the strongest stretching anywhere on the closed filament.

This separation matters because it directly tests the **outsourcing loophole**.

A resolution/core sweep gave:

\[
(N,a)=(256,.05),\ (320,.04),\ (384,.03).
\]

The relay/contraction failures remained near

\[
s\approx0.443,\quad0.428,\quad0.368.
\]

Restricting attention to pre-failure intervals in which the *physical local reach itself* was shrinking, the median finite Reynolds number required by the best stretching within `2 delta` was approximately

\[
4511,\quad5850,\quad5462,
\]

respectively, for the illustrative `c_nu=4` core model.

These are **not physical predictions**. The coefficient, core equation, regularized kernel, and reach definition are all part of the reduced model. The useful qualitative observation is different:

> The point/pair actually defining the shrinking local ruler generally has a worse strain balance than other parts of the loop. The dangerous positive stretching is imported from nearby or remote geometry rather than produced by the local closing mechanism itself.

At the coarser two resolutions the global maximum positive stretching typically lay many local reach lengths away from the active ruler; at the finest tested case the location statistics changed substantially. Therefore the distance statistic is not claimed to be numerically converged. The robust conclusion retained is only that allowing nonlocal stretching improves the gate, exactly as predicted by the earlier analytic loophole.

## Status after checkpoint 86

The project has now pushed the coherent-tube argument to a familiar hard boundary:

- bounded renormalized coherent geometry is insufficient for blowup;
- making the relative core vanish requires an unbounded scale-invariant core-strain product;
- a remote pusher either needs diverging critical circulation/amplitude or must descend to the core scale, creating a new ruler;
- the reduced relay continues to lose its collapsing cyclic state rather than discovering such an escape over the tested range.

What remains is recognizably Type-II territory: a cascade whose critical amplitude becomes unbounded, whose active scale repeatedly changes, or whose vortex-tube description fails. This is not a global-regularity proof.

A current literature anchor for the Type-II side is G. Seregin, *On potential Type II blowups for the Navier-Stokes equations*, arXiv:2606.29468 (2026), which studies potential Type-II scenarios using Euler rescaling and Liouville-type arguments.
