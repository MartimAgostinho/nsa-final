import sympy as sp

# Definir variáveis simbólicas
vip, vz, vy, vx = sp.symbols('v_ip v_z v_y v_x')
gm11, gm1b, gm7b, gm7a, gm5, gm2a = sp.symbols(
    'g_m11 g_m1b g_m7b g_m7a g_m5 g_m2a')
iout = sp.symbols('i_out')

# Expressões das correntes nos ramos do circuito
i_gm11 = gm11 * vz
i_gm1b = gm1b * vip
i_gm7b = gm7b * vy
i_gm7a = gm7a * vy
i_gm5 = -gm5 * vx
i_gm2a = -gm2a * vip

# Expressão para i_out (somatório das correntes)
iout_expr = i_gm1b + i_gm7a

# Expressões de nós (substituir com base no circuito)
vx_expr = iout/(i_gm2a+i_gm7a)
vy_expr = (-i_gm7b*vz)/(-i_gm11+i_gm11+i_gm1b)
vz_expr = (i_gm1b*vy)/(i_gm7b+i_gm11+i_gm11*vy)


# Substituir relações de nós no circuito
iout_expr = iout_expr.subs(vx, vx_expr)
iout_expr = iout_expr.subs(vy, vy_expr)
iout_expr = iout_expr.subs(vz, vz_expr)

# Calcular Gm = i_out / v_ip
Gm = sp.simplify(iout_expr / vip)

# Exibir o resultado
print("Gm (i_out / v_ip):", Gm)
