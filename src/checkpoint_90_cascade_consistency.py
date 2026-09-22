from pathlib import Path
import numpy as np

OUT=Path('outputs'); OUT.mkdir(parents=True,exist_ok=True)

# Combine checkpoints 88-89 into a consistency table.
# m>1 circulation growth; q ruler shrink.  We ask whether the abstract sequence
# can simultaneously have: increasing Re, decreasing relative core, finite total
# stage energy/dissipation proxy, finite Zeno time, and enough O(1)-per-generation
# strain impulse to satisfy the backward-area gate.
# We parameterize the available normalized strain impulse per generation by I.

ms=[2,3,4]
qs=np.geomspace(.003,.5,260)
Is=[1.0,2.0,3.0,4.0]
rows=[]
for m in ms:
    for q in qs:
        energy_ok=m*m*q<1
        time_ok=q*q/m<1
        Jreq=.5*np.log(m/(q*q))
        for I in Is:
            area_ok=I>=Jreq
            allok=energy_ok and time_ok and area_ok
            rows.append((m,q,I,m*m*q,q*q/m,Jreq,float(energy_ok),float(time_ok),float(area_ok),float(allok)))
arr=np.array(rows,float)
np.savetxt(OUT/'checkpoint_90_cascade_consistency.csv',arr,delimiter=',',
           header='m,q,available_strain_impulse_I,stage_energy_ratio,time_ratio,Jreq_area_gate,energy_sum_ok,time_sum_ok,area_gate_ok,all_three_ok',comments='')

lines=[]
lines.append('Checkpoint 90 - combined abstract escape-window audit')
lines.append('Algebraic consistency test only; NOT a Navier-Stokes solution or existence result.')
lines.append('')
lines.append('Conditions tested:')
lines.append('  finite model dissipation/energy series: m^2 q < 1')
lines.append('  finite Zeno time: q^2/m < 1')
lines.append('  stochastic-Kelvin backward-area gate with available normalized strain impulse I: I >= 0.5 log(m/q^2)')
lines.append('')
for m in ms:
    lines.append(f'm={m}:')
    for I in Is:
        mask=(arr[:,0]==m)&(arr[:,2]==I)&(arr[:,-1]==1)
        if np.any(mask):
            qok=arr[mask,1]
            lines.append(f'  I={I:.1f}: nonempty formal window q in [{qok.min():.6g}, {qok.max():.6g}] on sampled grid')
        else:
            lines.append(f'  I={I:.1f}: no sampled q satisfies all three gates')
lines.append('')
lines.append('Result: for sufficiently large but finite dimensionless strain impulse per generation, there remains a nonempty formal Type-II window satisfying every reduced budget derived so far. Example: m=2, q=0.20 needs J>=~1.956 per generation while its stage energy ratio is 0.8 and time ratio is 0.02.')
lines.append('Therefore the present geometric/core/energy/stochastic-circulation bookkeeping has NOT slain the final beast. It has isolated a very specific adversary: a rapidly shrinking, circulation-amplifying Type-II cascade with O(1)-to-few units of normalized strain impulse every generation.')
lines.append('')
lines.append('What would be needed next: a true NSE estimate showing that such repeated circulation amplification/area distortion cannot occur indefinitely, or that the required normalized strain impulse cannot stay high enough while the scale-critical amplitude diverges. Without that new PDE estimate, continuing to add algebraic budget gates will only reparameterize the known Type-II difficulty.')
(OUT/'checkpoint_90_cascade_consistency.txt').write_text('\n'.join(lines))
print('\n'.join(lines))
