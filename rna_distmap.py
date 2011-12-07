#!/usr/bin/env python
from numpy import *
import matplotlib.pyplot as plt
from pylab import *

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


#Make the plot.
plt.clf()
plt.suptitle('Interatomic Phosphorus Distance Matrix', fontsize=18)
plt.title('RNA P4-P6 Ribozyme Domain of Group I Intron (PDB_ID:1GID)')
plt.xlabel('Residue Number')
plt.ylabel('Residue Number')
plt.imshow(M, vmin=0, vmax=20, origin=0,
	cmap=cm.gist_heat, aspect='equal', interpolation='nearest')
plt.colorbar()
plt.grid(True)
#If you want to get a png figure uncomment the next line.
#savefig("confmat.png", dpi=200, format="png")
plt.show()

