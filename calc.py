import numpy as np

r = 2.1*10**-6
D4 = 0.144821*10**-12
Kb = 1.38*10**-23
T = 293

n = (Kb * T) / (6 * np.pi * (D4 / 4) * r) * 10**3


print(n)