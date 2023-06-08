import matplotlib.pyplot as plt
from math import *
import pandas as pd

#Дано
P = 0.5 / 1000
print("P =", P)
cp = 0.2
print("cp =", cp)
cw = 0.2 / 100
print("cw =", cw)
cf = 0.71 / 100
print("cf =", cf)
q = 1.4
print("q =", q)
alpha = pow(q, 0.5)
print("alpha =", alpha)
Lel = 0.00001
print("Lel =", Lel)

#Расчет N и f
Rf = cf / (1 - cf)
print("Rf =", Rf)
Rw = cw / (1 - cw)
print("Rw =", Rw)
Rp = cp / (1 - cp)
print("Rp =", Rp)
N = round(2 * log(Rp / Rw) / log(q) - 1) + 1
print("N =", N)
print((2 * log(Rp / Rw) / log(q) - 1))
f = int(- log(Rp / Rf) / log(alpha) + N + 1)
print("f =", f)
print((- log(Rp / Rf) / log(alpha) + N + 1))
#New Cw and Cp
cw_new = pow(alpha, -f) * Rf / (1 + pow(alpha, -f) * Rf)
print("cw_new =", cw_new)
cp_new = pow(alpha, N-f + 1) * Rf / (1 + pow(alpha, N-f + 1) * Rf)
print("cp_new =", cp_new)

# F and W
W = P * (cp_new - cf) / (cf - cw_new)
print("W =", W)
F = P + W
print("F =", F)

# Concentration
cs = [Rf * pow(alpha, i - f + 1) / (1 + Rf * pow(alpha, i - f + 1)) for i in range(N)] #Зависимость концентрации от номера ступени

# Tetta
tetta = [(1 + cs[i] * (alpha - 1)) / (alpha + 1) for i in range(N)]

#L(s)
l = []
z = []
for i in range(N):
    if i + 1 < f:
        temp = (alpha + 1) * W * (cs[i] - cw_new) / ((alpha - 1) * cs[i] * (1 - cs[i]))
        z.append(round(temp / Lel))
        l.append(temp)
    else:
        temp = (alpha + 1) * P * (cp_new - cs[i]) / ((alpha - 1) * cs[i] * (1 - cs[i]))
        z.append(round(temp / Lel))
        l.append(temp)
Z = sum(z)
print("Z =", Z)
n_array = [i + 1 for i in range(N)]
df = pd.DataFrame({'Число ступеней s': n_array,
                   'Concentation': cs,
                   'Tetta(s)': tetta,
                   'L(s)': l,
                   'Число элментов ступени': z})
df.to_excel('./table.xlsx')
fig = plt.subplots()
plt.plot(n_array, l)
plt.title("L(s)")
plt.xlabel("S")
plt.ylabel("l_s")
plt.show()
