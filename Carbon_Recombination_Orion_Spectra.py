#!/usr/bin/python

import os
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
import sys
import csv
from operator import itemgetter, attrgetter, methodcaller
import matplotlib.patches as mpatches



# Call in a csv file with the frequency and signal data
myfile=sys.argv[1]
source=sys.argv[2]


data = np.genfromtxt(myfile, delimiter=',', skip_header=10,skip_footer=10, names=['x', 'y'])
freq=data['x']
signal=data['y']


# Sort the data in frequency and write a file of the resultant sorted data if needed.

data=sorted(data, key=itemgetter(0))
freq, signal = zip(*data)
with open(str(source)+"_sorted.csv",'w') as f:
	writer = csv.writer(f,delimiter=',')
	writer.writerows(zip(freq,signal))


# Make one image as a full spectra

bigfig=plt.figure(figsize=(20,12))
ax1=bigfig.add_subplot(111)
ax1.step(freq, signal,color='blue')
ax1.set_title("Orion Nebula",fontsize=18)
ax1.set_xlabel("Frequency (MHz)",fontsize=18)
ax1.set_xlim(99,125)
ax1.set_ylabel("Flux Density (Jy/beam)",fontsize=18)
ax1.tick_params(labelsize=15)
      
bigfig.savefig("Orion_Full_Spectra"+source+".png")


# List of all the carbon alpha lines

ca_lines=[99.41,100.151,100.899,101.655,102.419,103.19,103.968,104.755,105.55,106.352,107.163,107.982,108.81,109.646,110.49,111.343,112.205,113.076,113.956,114.845,115.744,116.652,117.569,118.496,119.433,120.379,121.336,122.303,123.28,124.267,125.265,126.274,127.294,128.325]


# List of all the carbon beta lines

cb_lines=[104.018,104.642,105.271,105.905,106.544,107.189,107.838,108.493,109.154,109.819,110.49,111.167,111.849,112.536,113.229,113.928,114.633,115.344,116.06,116.782,117.511,118.245,118.986,119.733,120.486,121.245,122.011,122.783,123.562,124.347,125.139,125.938,126.743,127.556,128.375]


# Plot the first 9 cubes of data and mark the carbon alpha and beta lines.


fig, axs = plt.subplots(3, 3, sharex=False, sharey=True)
fig.set_figheight(15)
fig.set_figwidth(15)

axs[0,0].step(freq[0:86],signal[0:86],color='blue')
#axs[0,0].fill_between(np.arange(ca_lines[0]-0.01,ca_lines[0]+0.01,0.01), -1.5, 1.5, facecolor='plum', alpha=0.5)
#axs[0,0].fill_between(np.arange(ca_lines[1]-0.01,ca_lines[1]+0.01,0.01), -1.5, 1.5, facecolor='plum', alpha=0.5)
axs[0,0].set_title("Cube 1",fontsize=18)
axs[0,0].set_ylim(-1.5,1.5)
axs[0,0].set_ylabel("Flux Density (Jy/beam)",fontsize=18)
axs[0,0].get_xaxis().get_major_formatter().set_useOffset(False)
axs[0,0].tick_params(labelsize=15)
plum_patch = mpatches.Patch(color='plum', label='Carbon Alpha Lines')
axs[0,0].legend(handles=[plum_patch],loc=1)


axs[0,1].step(freq[101:220],signal[101:220],color='blue')
#axs[0,1].fill_between(np.arange(ca_lines[2]-0.01,ca_lines[2]+0.01,0.01), -1.5, 1.5, facecolor='plum', alpha=0.5)
axs[0,1].set_title("Cube 2",fontsize=18)
axs[0,1].set_ylim(-1.5,1.5)
axs[0,1].get_xaxis().get_major_formatter().set_useOffset(False)
axs[0,1].tick_params(labelsize=15)
green_patch = mpatches.Patch(color='mediumspringgreen', label='Carbon Beta Lines')
axs[0,1].legend(handles=[green_patch],loc=1)

axs[0,2].step(freq[231:280],signal[231:280],color='blue')
axs[0,2].set_title("Cube 3",fontsize=18)
axs[0,2].set_ylim(-1.5,1.5)
axs[0,2].get_xaxis().get_major_formatter().set_useOffset(False)
axs[0,2].tick_params(labelsize=15)


axs[1,0].step(freq[301:400],signal[301:400],color='blue')
#axs[1,0].fill_between(np.arange(ca_lines[4]-0.01,ca_lines[4]+0.01,0.01), -1.5, 1.5, facecolor='plum', alpha=0.5)
axs[1,0].set_title("Cube 4",fontsize=18)
axs[1,0].set_ylim(-1.5,1.5)
axs[1,0].get_xaxis().get_major_formatter().set_useOffset(False)
axs[1,0].tick_params(labelsize=15)

axs[1,1].step(freq[401:480],signal[401:480],color='blue')
axs[1,1].set_title("Cube 5",fontsize=18)
axs[1,1].set_ylim(-1.5,1.5)
axs[1,1].get_xaxis().get_major_formatter().set_useOffset(False)
axs[1,1].tick_params(labelsize=15)

axs[1,2].step(freq[496:585],signal[496:585],color='blue')
#axs[1,2].fill_between(np.arange(ca_lines[6]-0.01,ca_lines[6]+0.01,0.01), -1.5, 1.5, facecolor='plum', alpha=0.5)
#axs[1,2].fill_between(np.arange(cb_lines[0]-0.01,cb_lines[0]+0.01,0.01), -1.5, 1.5, facecolor='mediumspringgreen', alpha=0.5)
axs[1,2].set_title("Cube 6",fontsize=18)
axs[1,2].set_ylim(-1.5,1.5)
axs[1,2].get_xaxis().get_major_formatter().set_useOffset(False)
axs[1,2].tick_params(labelsize=15)

axs[2,0].step(freq[596:685],signal[596:685],color='blue')
#axs[2,0].fill_between(np.arange(ca_lines[7]-0.01,ca_lines[7]+0.01,0.01), -1.5, 1.5, facecolor='plum', alpha=0.5)
#axs[2,0].fill_between(np.arange(cb_lines[1]-0.01,cb_lines[1]+0.01,0.01), -1.5, 1.5, facecolor='mediumspringgreen', alpha=0.5)
#axs[2,0].fill_between(np.arange(cb_lines[2]-0.01,cb_lines[2]+0.01,0.01), -1.5, 1.5, facecolor='mediumspringgreen', alpha=0.5)
axs[2,0].set_title("Cube 7",fontsize=18)
axs[2,0].set_xlabel("Frequency (MHz)",fontsize=18)
axs[2,0].set_ylim(-1.5,1.5)
axs[2,0].get_xaxis().get_major_formatter().set_useOffset(False)
axs[2,0].tick_params(labelsize=15)
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

axs[2,1].step(freq[696:785],signal[696:785],color='blue')
#axs[2,1].fill_between(np.arange(ca_lines[9]-0.01,ca_lines[9]+0.01,0.01), -1.5, 1.5, facecolor='plum', alpha=0.5)
#axs[2,1].fill_between(np.arange(cb_lines[3]-0.01,cb_lines[3]+0.01,0.01), -1.5, 1.5, facecolor='mediumspringgreen', alpha=0.5)
#axs[2,1].fill_between(np.arange(cb_lines[4]-0.01,cb_lines[4]+0.01,0.01), -1.5, 1.5, facecolor='mediumspringgreen', alpha=0.5)
axs[2,1].set_title("Cube 8",fontsize=18)
axs[2,1].set_xlabel("Frequency (MHz)",fontsize=18)
axs[2,1].set_ylim(-1.5,1.5)
axs[2,1].get_xaxis().get_major_formatter().set_useOffset(False)
axs[2,1].tick_params(labelsize=15)

axs[2,2].step(freq[796:885],signal[796:885],color='blue')
#axs[2,2].fill_between(np.arange(ca_lines[10]-0.01,ca_lines[10]+0.01,0.01), -1.5, 1.5, facecolor='plum', alpha=0.5)
#axs[2,2].fill_between(np.arange(ca_lines[11]-0.01,ca_lines[11]+0.01,0.01), -1.5, 1.5, facecolor='plum', alpha=0.5)
#axs[2,2].fill_between(np.arange(cb_lines[5]-0.01,cb_lines[5]+0.01,0.01), -1.5, 1.5, facecolor='mediumspringgreen', alpha=0.5)
axs[2,2].set_title("Cube 9",fontsize=18)
axs[2,2].set_xlabel("Frequency (MHz)",fontsize=18)
axs[2,2].set_ylim(-1.5,1.5)
axs[2,2].get_xaxis().get_major_formatter().set_useOffset(False)
axs[2,2].tick_params(labelsize=15)

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

fig.savefig(source+"-Part1.png", pad_inches=0.5,bbox_inches='tight')


# Create a plot of Cubes 10-18

fig, axs = plt.subplots(3, 3, sharex=False, sharey=True)
fig.set_figheight(15)
fig.set_figwidth(15)

axs[0,0].step(freq[891:980],signal[891:980],color='blue')
#axs[0,0].fill_between(np.arange(ca_lines[12]-0.01,ca_lines[12]+0.01,0.01), -1.5, 1.5, facecolor='plum', alpha=0.5)
#axs[0,0].fill_between(np.arange(cb_lines[7]-0.01,cb_lines[7]+0.01,0.01), -1.5, 1.5, facecolor='mediumspringgreen', alpha=0.5)
#axs[0,0].fill_between(np.arange(cb_lines[8]-0.01,cb_lines[8]+0.01,0.01), -1.5, 1.5, facecolor='mediumspringgreen', alpha=0.5)
axs[0,0].set_title("Cube 10",fontsize=18)
axs[0,0].set_ylim(-1.5,1.5)
axs[0,0].set_ylabel("Flux Density (Jy/beam)",fontsize=18)
axs[0,0].get_xaxis().get_major_formatter().set_useOffset(False)
axs[0,0].tick_params(labelsize=15)
plum_patch = mpatches.Patch(color='plum', label='Carbon Alpha Lines')
axs[0,0].legend(handles=[plum_patch],loc=1)

axs[0,1].step(freq[991:1090],signal[991:1090],color='blue')
#axs[0,1].fill_between(np.arange(ca_lines[13]-0.01,ca_lines[13]+0.01,0.01), -1.5, 1.5, facecolor='plum', alpha=0.5)
#axs[0,1].fill_between(np.arange(cb_lines[9]-0.01,cb_lines[9]+0.01,0.01), -1.5, 1.5, facecolor='mediumspringgreen', alpha=0.5)
axs[0,1].set_title("Cube 11",fontsize=18)
axs[0,1].set_ylim(-1.5,1.5)
axs[0,1].get_xaxis().get_major_formatter().set_useOffset(False)
axs[0,1].tick_params(labelsize=15)
green_patch = mpatches.Patch(color='mediumspringgreen', label='Carbon Beta Lines')
axs[0,1].legend(handles=[green_patch],loc=1)

axs[0,2].step(freq[1091:1170],signal[1091:1170],color='blue')
axs[0,2].set_title("Cube 12",fontsize=18)
axs[0,2].set_ylim(-1.5,1.5)
axs[0,2].get_xaxis().get_major_formatter().set_useOffset(False)
axs[0,2].tick_params(labelsize=15)

axs[1,0].step(freq[1193:1293],signal[1193:1293],color='blue')
#axs[1,0].fill_between(np.arange(cb_lines[11]-0.01,cb_lines[11]+0.01,0.01), -1.5, 1.5, facecolor='mediumspringgreen', alpha=0.5)
axs[1,0].set_title("Cube 13",fontsize=18)
axs[1,0].set_ylim(-1.5,1.5)
axs[1,0].get_xaxis().get_major_formatter().set_useOffset(False)
axs[1,0].tick_params(labelsize=15)

axs[1,1].step(freq[1295:1370],signal[1295:1370],color='blue')
#axs[1,1].fill_between(np.arange(ca_lines[15]-0.01,ca_lines[15]+0.01,0.01), -1.5, 1.5, facecolor='plum', alpha=0.5)
axs[1,1].set_title("Cube 14",fontsize=18)
axs[1,1].set_ylim(-1.5,1.5)
axs[1,1].get_xaxis().get_major_formatter().set_useOffset(False)
axs[1,1].tick_params(labelsize=15)

axs[1,2].step(freq[1386:1475],signal[1386:1475],color='blue')
#axs[1,2].fill_between(np.arange(ca_lines[16]-0.01,ca_lines[16]+0.01,0.01), -1.5, 1.5, facecolor='plum', alpha=0.5)
#axs[1,2].fill_between(np.arange(cb_lines[13]-0.01,cb_lines[13]+0.01,0.01), -1.5, 1.5, facecolor='mediumspringgreen', alpha=0.5)
axs[1,2].set_title("Cube 15",fontsize=18)
axs[1,2].set_ylim(-1.5,1.5)
axs[1,2].get_xaxis().get_major_formatter().set_useOffset(False)
axs[1,2].tick_params(labelsize=15)

axs[2,0].step(freq[1486:1575],signal[1486:1575],color='blue')
#axs[2,0].fill_between(np.arange(ca_lines[18]-0.01,ca_lines[18]+0.01,0.01), -1.5, 1.5, facecolor='plum', alpha=0.5)
#axs[2,0].fill_between(np.arange(cb_lines[15]-0.01,cb_lines[15]+0.01,0.01), -1.5, 1.5, facecolor='mediumspringgreen', alpha=0.5)
axs[2,0].set_title("Cube 16",fontsize=18)
axs[2,0].set_xlabel("Frequency (MHz)",fontsize=18)
axs[2,0].set_ylim(-1.5,1.5)
axs[2,0].get_xaxis().get_major_formatter().set_useOffset(False)
axs[2,0].tick_params(labelsize=15)
plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

axs[2,1].step(freq[1586:1675],signal[1586:1675],color='blue')
#axs[2,1].fill_between(np.arange(ca_lines[19]-0.01,ca_lines[19]+0.01,0.01), -1.5, 1.5, facecolor='plum', alpha=0.5)
#axs[2,1].fill_between(np.arange(cb_lines[17]-0.01,cb_lines[17]+0.01,0.01), -1.5, 1.5, facecolor='mediumspringgreen', alpha=0.5)
axs[2,1].set_title("Cube 17",fontsize=18)
axs[2,1].set_xlabel("Frequency (MHz)",fontsize=18)
axs[2,1].set_ylim(-1.5,1.5)
axs[2,1].get_xaxis().get_major_formatter().set_useOffset(False)
axs[2,1].tick_params(labelsize=15)

axs[2,2].step(freq[1687:1775],signal[1687:1775],color='blue')
#axs[2,2].fill_between(np.arange(ca_lines[22]-0.01,ca_lines[22]+0.01,0.01), -1.5, 1.5, facecolor='plum', alpha=0.5)
axs[2,2].set_title("Cube 18",fontsize=18)
axs[2,2].set_xlabel("Frequency (MHz)",fontsize=18)
axs[2,2].set_ylim(-1.5,1.5)
axs[2,2].get_xaxis().get_major_formatter().set_useOffset(False)
axs[2,2].tick_params(labelsize=15)

plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)

fig.savefig(source+"-Part2.png", pad_inches=0.5,bbox_inches='tight')






