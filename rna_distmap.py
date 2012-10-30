#!/usr/bin/env python
from numpy import *
import scipy.spatial.distance as dista
import matplotlib.pyplot as plt
from pylab import *
# The following python script is aimed at recreating interatomic distance plots such
# as the one in Figure 2 of Malathi and Yathindra, Biochemical Journal, 1982,
# 205, 457-460.
# http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1158502/?page=3 

#The file Pmat.dat contains the cartesian coordinates for the phosphate
#atoms.
#inp = open("Pmat.dat");
inp = genfromtxt("Pmat.dat")

#Arrange the data in an array
#cart_arr = []
#for line in inp.readlines():
#    cart_arr.append([])
#    for i in line.split():
#        cart_arr[-1].append(float(i))

#inp.close()        

#M = array(cart_arr)
M = inp

#Compute the distance matrix
D = dista.cdist(M,M)

#This is a trick to get a lower diagonal displayed alone.
mask =  triu(D)               # the upper diagonal is masked
D = ma.array(D, mask=mask)    # mask out the upper triangle

#Make the plot.
plt.clf()
plt.suptitle('Interatomic Phosphorus Distance Matrix', fontsize=18)
#plt.title('RNA P4-P6 Ribozyme Domain of Group I Intron (PDB_ID:1GID)')
plt.title('yeast tRNA (PDB_ID:1EHZ)')
plt.xlabel('Residue Number')
plt.ylabel('Residue Number')
cmap = cm.get_cmap('gist_heat',10)
cmap.set_bad('w')
plt.imshow(D, vmin=0, vmax=25, origin='upper',
	cmap=cmap, aspect='equal', interpolation='nearest')           
plt.colorbar()
plt.grid(True)
#If you want to get a png figure uncomment the next line.
#savefig("confmat.png", dpi=200, format="png")
plt.show()

