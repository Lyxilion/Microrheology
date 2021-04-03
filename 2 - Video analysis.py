"""
    File name: 2 - Video analysis.py
    Author: Rubens BOUCHER
    Date created: 25/01/2021
    Date last modified: 03/04/2021
    Python Version: 3.7
    Email : boucher.rubens.974@gmail.com
"""
import matplotlib.pyplot as plt
import pims
import trackpy as tp
import numpy as np

link = "Sample/eau.avi"                                               # path of the video
diamater = 21                                                         # diamater of the tracking circle in px
mass = 1000
frames_rate = 23.19                                                   # framerate of the video
max_deplacement = 5                                                   # max deplacement of a particule betweentwo frames

frames = pims.as_grey(pims.Video(link))                               # we load each frame of the video
f = tp.batch(frames[:], diamater, minmass=mass, engine='numba')       # tracking every particule in each frame
t = tp.link_df(f, max_deplacement, memory=3)                          # linking particules between each frame
t1 = tp.filter_stubs(t, 15)                                           # deleting tracks that are not completed

plt.figure()
tp.plot_traj(t1)                                                      # plot trajectories
d = tp.compute_drift(t1)                                              # we compute the general drift of the particules
plt.figure()
d.plot()                                                              # we plot the drift
tm = tp.subtract_drift(t1.copy(), d)                                  # we subtrack the drift in the trajectories
plt.figure()
ax = tp.plot_traj(tm)                                                 # we plot the tajectories without drift

em = tp.emsd(tm, 0.131, frames_rate)                                  # compute emsd, 0.131 micro/px in the video
em.to_pickle("Storage.plk")                                           # we store the emsd for later use

fig, ax = plt.subplots()
ax.plot(em.index, em, '-')                                            # plot the emsd in logscale
ax.set_xscale('log')
ax.set_yscale('log')
ax.set(ylabel=r'$\langle \Delta r^2 \rangle$ [$\mu$m$^2$]',
       xlabel='time $t$')

plt.figure()
plt.ylabel(r'$\langle \Delta r^2 \rangle$ [$\mu$m$^2$]')
plt.xlabel('time $t$')
fit = tp.utils.fit_powerlaw(em)                                       # performs linear best fit in log space, plots
print(fit)

r = 2.1*10**-6/2                                                      # Diamater of the particule
D4 = fit.iloc[0]['A']*10**-12
Kb = 1.38*10**-23                                                     # Botlzman constant
T = 293                                                               # Temperature

n = (Kb * T) / (6 * np.pi * (D4 / 4) * r) * 1E3                       # Calculation viscosity

print("eta =  ", n, " mPa s")
