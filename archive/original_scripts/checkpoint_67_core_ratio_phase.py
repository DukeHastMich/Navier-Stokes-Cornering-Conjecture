import numpy as np

# Analytic coherent-core ratio model.
# Geometry: R^2' = -2 c_g Gamma (self-similar comparable-scale collapse)
# Core: b' = -sigma b + 4 nu, sigma = c_s Gamma/R^2
# y=b/R^2, tau=-log(R^2/R0^2):
# dy/dtau = 2/(c_g Re_Gamma) + (1 - c_s/(2c_g))*y.
# If lambda=c_s/(2c_g)>1, y -> y*=2/[c_g Re (lambda-1)]
# equivalently 4 nu/[(c_s-2c_g)Gamma].

Res=[100,1000,4000,10000,1_000_000]
lams=[0.8,1.0,1.25,1.5,2.0,4.0]
cg=0.5  # normalization 2*c_g=1; only sets illustrative coefficient table.

lines=[]
lines.append('Checkpoint 67 - finite-core ratio phase table')
lines.append('Model: R^2dot=-2 c_g Gamma; bdot=-c_s Gamma b/R^2 + 4 nu; y=b/R^2.')
lines.append('tau=-ln(R^2/R0^2): dy/dtau=2/(c_g Re_Gamma)+(1-lambda)y, lambda=c_s/(2c_g).')
lines.append('For lambda>1: y*=2/[c_g Re_Gamma (lambda-1)], so a/R -> sqrt(y*) > 0 at finite Re.')
lines.append('For lambda<=1: y does not approach zero; it grows (linearly at lambda=1, exponentially for lambda<1).')
lines.append('Illustrative normalization c_g=0.5 (2 c_g=1).\n')

for Re in Res:
    lines.append(f'Re_Gamma={Re}')
    for lam in lams:
        if lam<=1:
            lines.append(f'  lambda={lam:4.2f}: no positive attracting floor; y grows, not ->0')
        else:
            ystar=2/(cg*Re*(lam-1))
            lines.append(f'  lambda={lam:4.2f}: y*={ystar:.8g}, (a/R)*={np.sqrt(ystar):.8g}')
    lines.append('')

# Demonstrate convergence for one case under repeated geometric shrinkage.
# tau increments by -ln(q^2) per generation.
q=0.5
Dtau=-np.log(q*q)
for Re,lam,y0 in [(4000,2.0,0.0225),(1000,2.0,0.0225),(4000,1.5,0.0225)]:
    mu=2/(cg*Re)
    A=1-lam
    y=y0
    seq=[]
    for n in range(12):
        seq.append((n,y,np.sqrt(y)))
        if abs(A)<1e-14:
            y=y+mu*Dtau
        else:
            ystar=-mu/A
            y=ystar+(y-ystar)*np.exp(A*Dtau)
    lines.append(f'Cascade example Re={Re}, lambda={lam}, q={q}, y0={y0}:')
    lines.append('  '+'; '.join(f'n{n}:a/R={ar:.5f}' for n,yy,ar in seq))
    lines.append('')

open('/mnt/data/checkpoint_67_core_ratio_phase.txt','w').write('\n'.join(lines))
print('\n'.join(lines))
