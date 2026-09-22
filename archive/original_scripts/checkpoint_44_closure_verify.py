import sympy as sp

a, th, d, G, R, z = sp.symbols('a th d Gamma R z', positive=True, real=True)
S = sp.diag(-2*a, a, a)
n = sp.Matrix([1,0,0])
t = sp.Matrix([0, sp.cos(th), sp.sin(th)])
P = sp.eye(3) - t*t.T
print('normal compression n^T S n =', sp.simplify((n.T*S*n)[0]))
print('direction evolution P S t =', sp.simplify(P*S*t))
print('tangent stretching t^T S t =', sp.simplify((t.T*S*t)[0]))

u_axis = G*R**2/(2*(R**2+z**2)**sp.Rational(3,2))
print('ring center axial velocity =', sp.simplify(u_axis.subs(z,0)))
print('ring center axial derivative =', sp.simplify(sp.diff(u_axis,z).subs(z,0)))
print('ring center axial second derivative =', sp.simplify(sp.diff(u_axis,z,2).subs(z,0)))
