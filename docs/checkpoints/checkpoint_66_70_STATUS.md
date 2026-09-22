# Navier–Stokes Cornering Run — Checkpoints 66–70 Status

**Status:** no global proof. The finite-core comparable-scale closed relay has been substantially narrowed/conditionally eliminated.

## Completed this run

1. Coupled the prior four-arc closed Biot–Savart relay to viscous transverse-core evolution `b'=-sigma b+4nu` and source-dependent core regularization.
2. Swept circulation Reynolds numbers `infinity, 10000, 4000, 1000, 100`.
3. Derived the exact comparable-scale ratio equation for `y=(a/R)^2`:

   `dy/dtau = 2nu/(c_g Gamma) + (1-c_s/(2c_g)) y`.

4. Derived the positive fixed relative core thickness when stretching beats geometry:

   `y*=4nu/[(c_s-2c_g)Gamma]`.

5. Derived a conditional no-slenderness lemma: with bounded dimensionless self-strain coefficient `C`, a shrinking coherent core must satisfy

   `(a/R)^2 > (c_nu/C)(nu/Gamma)`.

6. Checked the scaling escape: ordinary Navier–Stokes parabolic scaling leaves circulation `Gamma` invariant, so `Gamma/nu` does not grow just because the candidate shrinks.

## Verdict

**Eliminated within the tested coherent-core assumptions:** a fixed-shape or bounded-geometry closed relay that remains filamentary (`a/R -> 0`) while collapsing at finite circulation Reynolds number.

**Not eliminated:** a genuinely non-self-similar/Type-II point concentration that drives its dimensionless geometry coefficient to infinity, creates new subscales/branches, or abandons coherent vortex-tube structure through strong 3-D deformation/reconnection.

This is consistent with the literature result of Hormoz & Brenner (JFM 707, 2012), who found an antagonism between interacting-filament centerline collapse and the core evolution needed to sustain singular stretching.
