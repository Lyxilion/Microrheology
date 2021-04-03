"""
    File name: 3 - EMSD curve fitting.py
    Author: Rubens BOUCHER
    Date created: 25/01/2021
    Date last modified: 03/04/2021
    Python Version: 3.7
    Email : boucher.rubens.974@gmail.com
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pandas as pd


def f(t, r0, td):                               # function we want to fit
    return r0**2*(1-np.exp(-t/td))


df = pd.read_pickle("pickle.plk")
emsd = []
lagt = []
for name, value in df.iteritems():
    lagt.append(name)
    emsd.append(value)
emsd = np.array(emsd[:2100])*10**-12
lagt = np.array(lagt[:2100])
res = curve_fit(f, lagt, emsd, method="lm")     # fitting the function to the dataset
print("r0 = " + str(res[0][0]))                 # printng the results
print("td = " + str(res[0][1]))
fit = f(lagt, res[0][0], res[0][1])             # calculating the points
fig, ax = plt.subplots()                        # ploting
plt.rcParams.update({'mathtext.default': 'regular'})
ax.plot(lagt, emsd, "+", label='$< \Delta r^2 >$')
ax.plot(lagt, fit, label="Fit")
ax.set_yscale('log')
plt.legend()
plt.title("Ajustement de la courbe de $< \Delta r^2 >$")
plt.ylabel('''$< \Delta r^2 > \quad (m^2)$''')
plt.xlabel("$Temps \quad (s)$")
plt.show()
