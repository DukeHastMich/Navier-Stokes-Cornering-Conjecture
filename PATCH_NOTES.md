# Checkpoint 95–98 update

This delta performs a final adversarial audit of the Kelvin-gradient/circulation route.

Key result: checkpoint 93's `delta/Re` layer is a valid inherited-amplitude estimate, but it is not a universal circulation-transfer layer. An exact heat-step diffusion calculation gives a competing layer with

- `h/delta ~ Re^-1/2`,
- vorticity jump `~Re^1/2` times the parent amplitude,
- local `Re_h ~ Re^1/2`.

Iterating this relation gives a short square-root hierarchy `Re, sqrt(Re), Re^(1/4), ...` that formally bridges the parent scale to the `delta/Re` ruler without creating a new divergent reduced energy/time budget.

The research program is therefore marked at a principled stopping boundary: the geometric cornering/finite-core arguments substantially constrain coherent self-collapse, but they do not eliminate the remaining unbounded critical Type-II regime. Closing that regime requires a genuinely new Navier–Stokes critical estimate.

This update **does not claim a proof of global regularity or a construction of blowup**.
