import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame, Series  # for convenience
import pims
import trackpy as tp
import moviepy

link = "Sample/video2.mp4"
diamater = 35
mass = 4000

frames = pims.as_grey(pims.Video(link))
#On analysela vidéo
max_deplacement = 5
f = tp.batch(frames[:300], diamater, minmass=mass)
t = tp.link_df(f, max_deplacement, memory=3)
t.head()
t1 = tp.filter_stubs(t, 25)
# Compare the number of particles in the unfiltered and filtered data.
print('Before:', t['particle'].nunique())
print('After:', t1['particle'].nunique())
plt.figure()
tp.plot_traj(t1)
d = tp.compute_drift(t1)
plt.figure()
d.plot()
tm = tp.subtract_drift(t1.copy(), d)
plt.figure()
ax = tp.plot_traj(tm)


im = tp.imsd(tm, 1/2, 24)  # microns per pixel = .001, frames per second = 24

fig, ax = plt.subplots()
ax.plot(im.index, im, 'k-', alpha=0.1)  # black lines, semitransparent
ax.set(ylabel=r'$\langle \Delta r^2 \rangle$ [$\mu$m$^2$]', xlabel='lag time $t$')
ax.set_xscale('log')
ax.set_yscale('log')






em = tp.emsd(tm, 1/2, 24) # microns per pixel = 100/285., frames per second = 24

fig, ax = plt.subplots()
ax.plot(em.index, em, 'o')
#ax.set_xscale('log')
#ax.set_yscale('log')
ax.set(ylabel=r'$\langle \Delta r^2 \rangle$ [$\mu$m$^2$]',
       xlabel='lagddddd time $t$')
ax.set(ylim=(1e-2, 10));


em = tp.emsd(tm, 1/2, 24)
plt.figure()
plt.ylabel(r'$\langle \Delta r^2 \rangle$ [$\mu$m$^2$]')
plt.xlabel('lag timehfhfhf $t$')
a = tp.utils.fit_powerlaw(em)  # performs linear best fit in log space, plots
print(a)
#print(a.iat[0,1])
