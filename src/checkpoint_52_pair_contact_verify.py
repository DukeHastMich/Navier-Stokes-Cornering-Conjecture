import sympy as sp

# Symbols
s,d,G,kn,kb,theta,L = sp.symbols('s d G kn kb theta L', positive=True, real=True)
x1,x2,x3 = sp.symbols('x1 x2 x3', real=True)

# Source filament near s=0. Tangent t2=e_z at s=0.
# Curvature components: kn along separation normal e_x, kb along e_y=t2 x n.
X = sp.Matrix([kn*s**2/2, kb*s**2/2, s])
Xp = sp.diff(X,s)
x = sp.Matrix([x1,x2,x3])
r = x-X

u_int = G/(4*sp.pi) * Xp.cross(r) / (r.dot(r))**sp.Rational(3,2)
Grad = u_int.jacobian([x1,x2,x3])
S = sp.simplify((Grad + Grad.T)/2)

# Target at distance d along e_x, tangent in plane perpendicular to e_x.
t = sp.Matrix([0, sp.sin(theta), sp.cos(theta)])
subs_target = {x1:d, x2:0, x3:0}
alpha_int = sp.simplify((t.T*S*t)[0].subs(subs_target))
un_int = sp.simplify(u_int[0].subs(subs_target))

# First-order coefficients about straight source.
def lin_coeff(expr, var):
    return sp.simplify(sp.diff(expr,var).subs({kn:0,kb:0}))

alpha0 = sp.simplify(alpha_int.subs({kn:0,kb:0}))
alpha_kn = sp.factor(lin_coeff(alpha_int,kn))
alpha_kb = sp.factor(lin_coeff(alpha_int,kb))
un0 = sp.simplify(un_int.subs({kn:0,kb:0}))
un_kn = sp.factor(lin_coeff(un_int,kn))
un_kb = sp.factor(lin_coeff(un_int,kb))

# Symmetric infinite-window integrals where convergent.
alpha0_inf = sp.integrate(alpha0, (s,-sp.oo,sp.oo))
alpha_kn_inf = sp.integrate(alpha_kn, (s,-sp.oo,sp.oo))
alpha_kb_inf = sp.simplify(sp.integrate(alpha_kb, (s,-sp.oo,sp.oo)))

# Normal velocity kb correction over finite symmetric window [-L,L].
un_kb_L = sp.simplify(sp.integrate(un_kb, (s,-L,L)))

print('alpha0 integrand =', alpha0)
print('d(alpha)/d kn at 0 =', alpha_kn)
print('d(alpha)/d kb at 0 =', alpha_kb)
print('symmetric integral alpha0 =', alpha0_inf)
print('symmetric integral alpha_kn =', alpha_kn_inf)
print('symmetric integral alpha_kb =', alpha_kb_inf)
print()
print('normal velocity u.n straight =', un0)
print('d(u.n)/d kn at 0 =', un_kn)
print('d(u.n)/d kb at 0 =', un_kb)
print('finite-window integral d(u.n)/d kb =', un_kb_L)
print()
critical = sp.asin(sp.sqrt(sp.Rational(2,3)))
print('angle where 3 sin^2(theta)-2 changes sign =', critical)
print('degrees =', sp.N(critical*180/sp.pi, 12))

# Pair relation for aligned branches (theta=0), using global b=t x n curvature components k1,k2.
k1,k2,Q = sp.symbols('k1 k2 Q', real=True)
ddot = G/(4*sp.pi)*Q*(k1-k2)
alpha_sum = G/(2*sp.pi*d)*(k1-k2)
print()
print('aligned-pair local model:')
print('d_dot =', ddot)
print('alpha1+alpha2 =', alpha_sum)
print('(alpha1+alpha2) / d_dot =', sp.simplify(alpha_sum/ddot))
