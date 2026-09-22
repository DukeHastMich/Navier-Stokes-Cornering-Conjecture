from pathlib import Path
import numpy as np

OUT = Path('outputs'); OUT.mkdir(parents=True, exist_ok=True)

# Checkpoint 95
# A 1-D heat-step model is used only as a local diffusion sanity check.
# Initial vorticity jump A across x=0:
#   zeta(x,t) = A/2 erfc(x/(2 sqrt(nu t)))  for the half-space receiving flux.
# The diffusive flux per unit tangential length through x=0 is
#   J(t) = A sqrt(nu)/(2 sqrt(pi t)),
# and the integrated transfer is
#   Q(tau) = A sqrt(nu tau/pi).
# For a loop/boundary segment of length L~delta, transferring DeltaGamma~theta Gamma
# over tau~c_tau delta^2/Gamma therefore needs
#   A/Omega_parent ~ theta sqrt(pi)/(c_L sqrt(c_tau)) sqrt(Re_Gamma),
# while the diffusion-compatible layer thickness is h/delta~sqrt(c_tau/Re_Gamma).
# The layer circulation scale A h^2 has Re_h~O(sqrt(Re_parent)), not O(1/Re_parent).

nu = 1.0
Gamma = 1.0
# convenient normalization: Re=Gamma/nu is varied by choosing Gamma=Re, nu=1 below
Res = np.logspace(1, 8, 71)
theta = 1.0
cL = 1.0
ctau = 1.0
rows = []
for Re in Res:
    nu = 1.0
    Gamma = Re * nu
    delta = 1.0
    tau = ctau * delta**2 / Gamma
    L = cL * delta
    h = np.sqrt(nu * tau)
    # Exact heat-step integrated transfer Q=A sqrt(nu tau/pi); DeltaGamma=L Q.
    A = theta * Gamma * np.sqrt(np.pi) / (L * np.sqrt(nu * tau))
    Omega_parent = Gamma / delta**2
    amplitude_ratio = A / Omega_parent
    Gamma_layer = A * h**2
    Re_layer = Gamma_layer / nu
    # Check the exact transfer formula recovers theta*Gamma.
    recovered = L * A * np.sqrt(nu * tau / np.pi)
    rows.append((Re, tau, h/delta, amplitude_ratio, Re_layer,
                 Re_layer/np.sqrt(Re), recovered/Gamma))

arr = np.array(rows)
np.savetxt(OUT/'checkpoint_95_diffusive_kelvin_layer.csv', arr, delimiter=',',
           header='Re_parent,tau_parent,h_over_delta,jump_over_parent_omega,Re_layer,Re_layer_over_sqrtRe,recovered_DeltaGamma_over_Gamma', comments='')

lines = [
    'Checkpoint 95 - diffusion-compatible Kelvin layer',
    '',
    'Heat-step sanity model: Q(tau)=A sqrt(nu tau/pi) per unit boundary length.',
    'For DeltaGamma~Gamma, L~delta, tau~delta^2/Gamma:',
    '  h/delta ~ Re^{-1/2}',
    '  DeltaOmega/Omega_parent ~ sqrt(pi) Re^{1/2}  (for unit order constants)',
    '  Re_layer ~ sqrt(pi) Re^{1/2}.',
    '',
    'This is an adversarial correction to an over-strong reading of checkpoint 93.',
    'The ell~delta/Re layer is what follows if the vorticity jump is artificially limited to the parent amplitude.',
    'If the layer is allowed to carry the larger diffusion-compatible jump needed to persist over one parent nonlinear time,',
    'its thickness is delta/sqrt(Re) and its own circulation Reynolds number is O(sqrt(Re)), not O(1/Re).',
    'Thus the Kelvin gradient trap does not by itself make the transfer layer viscous roadkill.',
    ''
]
for Re in [10, 100, 1e4, 1e8]:
    row = arr[np.argmin(abs(arr[:,0]-Re))]
    lines.append(f'Re={row[0]:.0f}: h/delta={row[2]:.4g}, jump/Omega={row[3]:.4g}, Re_layer={row[4]:.4g}, transfer/Gamma={row[6]:.12f}')

(OUT/'checkpoint_95_diffusive_kelvin_layer.txt').write_text('\n'.join(lines))
print('\n'.join(lines))
