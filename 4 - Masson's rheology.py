"""
    File name: 4 - Masson's rheology.py
    Author: Rubens BOUCHER
    Date created: 25/01/2021
    Date last modified: 03/04/2021
    Python Version: 3.7
    Email : boucher.rubens.974@gmail.com
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_pickle("pickle.plk")           # we read the stored emsd
a = 2.1*10**-6/2                            # diameter of the particule in m
Kb = 1.38*10**-23                           # Boltzman constant
T = 295.15                                  # temperature in K
r0 = 3.17238348e-05                         # Parameters of the fit
td = 1.26073680e+04


def f(t, r0, td):                           # the fonction that was fited
    return r0**2*(1-np.exp(-t/td))


def derive(x, y):
    """
    Calculate the derivative of a function
    :param x: x
    :param y: y
    :return: x',y
    """
    nbx = len(x)
    xnew = np.zeros(nbx - 1)
    yp = np.zeros(nbx - 1)
    for i in range(nbx - 1):
        xnew[i] = (x[i] + x[i + 1]) / 2
        yp[i] = (y[i + 1] - y[i]) / (x[i + 1] - x[i])
    return xnew, yp


lagt = []                                   # for conviniance, we put the time in numpy array
for name, value in df.iteritems():
    lagt.append(name)
lagt = np.array(lagt[:2100])
w = 1/lagt

emsd = f(lagt, r0, td)                      # we use the fited function to calculate the emsd
ln_emsd = np.log(emsd)                      # we need the log of this value to calculate alpha
ln_lagt = np.log(lagt)

time, alpha = derive(ln_lagt, ln_emsd)                  # we calculate alpha

gamma = 0.457 * (1 + alpha)**2 - 1.36 * (1 + alpha) + 1.9     # we calculate the gamma of alpha

G = (Kb * T) / (np.pi * a * emsd[:-1] * gamma)          # we calculate G

g1 = G * np.cos(np.pi * alpha / 2)                      # we calculate g'
g2 = G * np.sin(np.pi * alpha / 2)                      # we calculate g"

fig, ax = plt.subplots()                                # we plot g' and g"
ax.plot(w[:-1], g1, label="G'")
ax.plot(w[:-1], g2, label='G"')
plt.legend()
plt.rcParams.update({'mathtext.default': 'regular'})
plt.title("Propriétés Dynamiques de la Gélatine")
plt.ylabel('''$G'(\omega), G''(\omega) \quad (Pa)$''')
plt.xlabel("$\omega \quad(s^{-1})$")
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()
