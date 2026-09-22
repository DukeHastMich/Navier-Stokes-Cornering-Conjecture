from pathlib import Path
import numpy as np

OUT = Path('outputs')
OUT.mkdir(parents=True, exist_ok=True)

# Kinematic divergence-free vortex-tube field built from an axisymmetric flux function
#   psi(r,z) = Gamma/(2*pi) * (1-exp(-(r/a(z))^2)).
# Then omega_r = -(1/r) psi_z and omega_z = (1/r) psi_r, so div omega = 0
# identically and the vorticity flux through every transverse z-plane is Gamma.
GAMMA = 1.0


def a_of_z(z):
    return 0.18 + 0.10 * (1.0 + np.tanh(1.4*z)) / 2.0


def flux_numeric(z, nr=300000):
    a = a_of_z(z)
    # omega_z = Gamma/(pi a^2) exp(-r^2/a^2)
    rmax = 7.0 * a
    r = np.linspace(0.0, rmax, nr)
    wz = GAMMA/(np.pi*a*a) * np.exp(-(r/a)**2)
    return np.trapezoid(wz * 2*np.pi*r, r)

zs = np.linspace(-3.0, 3.0, 13)
rows = []
for z in zs:
    a = a_of_z(z)
    flux = flux_numeric(z)
    wcenter = GAMMA/(np.pi*a*a)
    rows.append((z, a, flux, wcenter))
arr = np.array(rows)
np.savetxt(OUT/'checkpoint_87_vortex_flux_inheritance.csv', arr, delimiter=',',
           header='z,tube_radius_a,numerical_vorticity_flux,centerline_omega_z', comments='')

text = []
text.append('Checkpoint 87 - instantaneous vortex-tube flux inheritance')
text.append('Kinematic divergence-free example; NOT a Navier-Stokes time evolution.')
text.append('')
text.append('For any instantaneous vortex tube whose side surface is tangent to omega, div omega=0 implies equal vorticity flux through every cross-section.')
text.append('The toy field uses an axisymmetric flux function psi(r,z)=Gamma/(2pi)[1-exp(-(r/a(z))^2)].')
text.append('It narrows/widens with z while maintaining flux Gamma=1 across every transverse section.')
text.append('')
for z,a,flux,wc in rows:
    text.append(f'z={z:+.2f}  a={a:.8f}  flux={flux:.12f}  omega_center={wc:.8f}')
text.append('')
text.append(f'max |flux-Gamma| = {np.max(np.abs(arr[:,2]-GAMMA)):.3e}')
text.append('')
text.append('Interpretation for the renormalization argument:')
text.append('  Merely choosing a smaller geometric ruler inside the SAME coherent instantaneous vortex tube does not manufacture a larger circulation Reynolds number Gamma/nu. The tube strength is the same across its sections.')
text.append('  Therefore a same-tube scale escape can reset the geometry coefficient A at a smaller ruler, but it does not by itself increase Re_Gamma.')
text.append('  To make Re_Gamma grow from generation to generation, the dynamics must change the tube strength in time, aggregate flux from other structures, or cease to admit a coherent-tube description.')
(OUT/'checkpoint_87_vortex_flux_inheritance.txt').write_text('\n'.join(text))
print('\n'.join(text))
