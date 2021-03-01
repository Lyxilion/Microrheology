import matplotlib.pyplot as plt
import pims
import trackpy as tp

link = "Sample/4060.avi"
diamater =21
mass = 1000

frames = pims.as_grey(pims.Video(link))
# On affiche la première image
plt.imshow(frames[0])
plt.show()
# On localise une première fois (false = bright)
f = tp.locate(frames[0], diamater, minmass=mass, invert=False)
tp.annotate(f, frames[0])
# On plot les mass
fig, ax = plt.subplots()
ax.hist(f['mass'], bins=20)
ax.set(xlabel='mass', ylabel='count')
# On verifie les subpixels pour verifier le param de diametre
tp.subpx_bias(f)
plt.show()
