#!/usr/bin/env python
# The following python script is aimed at recreating interatomic distance plots such
# as the one in Figure 2 of Malathi and Yathindra, Biochemical Journal, 1982,
# 205, 457-460. It also creates a clustering diagram in both axes.
# http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1158502/?page=3

from numpy import *
#import matplotlib.pyplot as plt
import pylab 
import scipy
import scipy.cluster.hierarchy as sch

#
# CMmatr is the output of and octave script
# which computes the interatomic distance 
# matrix from pdbfiles which have been parsed
# with an awk/bash script called PPdistance
#

inp = open("CMmatr");

#Arrange the data in an array
dist_arr = []
for line in inp.readlines():
    dist_arr.append([])
    for i in line.split():
        dist_arr[-1].append(float(i))

inp.close()        
M = array(dist_arr)

# Compute and plot first dendrogram.
fig = pylab.plt.figure(figsize=(8,8))
ax1 = fig.add_axes([0.09,0.1,0.2,0.6])
Y = sch.linkage(M, method='centroid')
Z1 = sch.dendrogram(Y, orientation='right')
ax1.set_xticks([])
ax1.set_yticks([])

# Compute and plot second dendrogram.
ax2 = fig.add_axes([0.3,0.71,0.6,0.2])
Y = sch.linkage(M, method='single')
Z2 = sch.dendrogram(Y)
ax2.set_xticks([])
ax2.set_yticks([])

# Plot distance matrix.
axmatrix = fig.add_axes([0.3,0.1,0.6,0.6])
idx1 = Z1['leaves']
idx2 = Z2['leaves']
M = M[idx1,:]
M = M[:,idx2]
im = axmatrix.matshow(M, aspect='auto', origin='lower', cmap=pylab.cm.YlGnBu)
axmatrix.set_xticks([])
axmatrix.set_yticks([])

# Plot colorbar.
axcolor = fig.add_axes([0.91,0.1,0.02,0.6])
pylab.colorbar(im, cax=axcolor)
fig.show()

