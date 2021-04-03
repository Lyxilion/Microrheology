"""
    File name: 1 - Configuration of tracking parameters.py
    Author: Rubens BOUCHER
    Date created: 25/01/2021
    Date last modified: 03/04/2021
    Python Version: 3.7
    Email : boucher.rubens.974@gmail.com
"""
import matplotlib.pyplot as plt
import pims
import trackpy as tp

link = "Sample/eau.avi"                                         # path of the video
diamater = 21                                                   # diamater of the tracking circle in px
mass = 1000

frames = pims.as_grey(pims.Video(link))                         # Loading video frames
plt.imshow(frames[0])                                           # Show first frame
plt.show()
# On localise une première fois (false = bright)
f = tp.locate(frames[0], diamater, minmass=mass, invert=False)  # Locating features
tp.annotate(f, frames[0])                                       # Ploting feature
fig, ax = plt.subplots()
ax.hist(f['mass'], bins=20)                                     # cheking if mass distribution looks good
ax.set(xlabel='mass', ylabel='count')
tp.subpx_bias(f)                                                # check if subpixel are good
plt.show()
