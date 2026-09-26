def g(u): return 2/u**13 - 1/u**7

def falsa_posicion(f, ua, ub, iters):
    hist = []
    for _ in range(iters):
        uc = ub - f(ub)*(ub-ua)/(f(ub)-f(ua))
        hist.append((ua, ub, uc, f(uc)))
        ua, ub = (ua, uc) if f(ua)*f(uc) < 0 else (uc, ub)
    return hist

for h in falsa_posicion(g, 0.90, 1.50, 2):
    print(h)

def falsa_posicion_completa(f, ua, ub, tol=1e-10, maxit=500):
    for i in range(maxit):
        uc = ub - f(ub)*(ub-ua)/(f(ub)-f(ua))
        if abs(f(uc)) < tol: return uc, i+1
        ua, ub = (ua, uc) if f(ua)*f(uc) < 0 else (uc, ub)
    return uc, maxit

sigma = 3.40
u_star, n = falsa_posicion_completa(g, 0.90, 1.50)
print(f"u* = {u_star:.6f} (exacto {2**(1/6):.6f}), iters={n}")
print(f"r_e = {u_star*sigma:.4f} Å (exacto {2**(1/6)*sigma:.4f} Å)")