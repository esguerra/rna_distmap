#!/usr/bin/env python
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
################################################################################
## File:        rna_distmap.py
## Authors:     Mauricio Esguerra
## Date:        February 21, 2013
## Email:       mauricio.esguerra@gmail.com
##
## Description:
## The following python script is aimed at recreating
## interatomic distance plots such as the one in Figure 2
## of Malathi and Yathindra, Biochemical Journal, 1982,
## 205, 457-460.
## http://www.ncbi.nlm.nih.gov/pmc/articles/PMC1158502/?page=3 
##
################################################################################
import os, sys
if len(sys.argv) != 2:
        print '===================================='    
        print 'Usage: rna_distmap.py <pdbid>'
        print '===================================='    
        print 'Notice that the pdb extension is'
        print 'not needed to invoke the map maker.'
        print '===================================='            
        sys.exit(1) 


from numpy import *
import scipy.spatial.distance as dista
import matplotlib
matplotlib.use('Agg') #Call before importing matplotlib.pyplot or pylab!
import matplotlib.pyplot as plt
from pylab import *


#A file called Pmat.dat is created to contains P atom coordinates
pdbname=sys.argv[1]
os.system("awk '{if (substr($0,1,6) ~ /ATOM/ && substr($0,14,1) ~ /P/) \
          print substr($0,32,23) }' %s.pdb > Pmat.dat" % (pdbname)) 
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
#Thanks to scipy's distance function it's easy to play around
#with other metrics
D = dista.cdist(M,M, metric='minkowski', p=2)
#D = dista.cdist(M,M)

#This is a trick to get a lower diagonal displayed alone.
mask =  triu(D)               # the upper diagonal is masked
D = ma.array(D, mask=mask)    # mask out the upper triangle


#Define the color map
cdict = {'red': ((0., 1, 1),
                 (0.05, 1, 1),
                 (0.11, 0, 0),
                 (0.66, 1, 1),
                 (0.89, 1, 1),
                 (1, 1.0, 1.0)),
         'green': ((0., 1, 1),
                   (0.05, 1, 1),
                   (0.11, 0, 0),
                   (0.375, 1, 1),
                   (0.64, 1, 1),
                   (0.91, 0, 0),
                   (1, 1, 1)),
         'blue': ((0., 1, 1),
                  (0.05, 1, 1),
                  (0.11, 1, 1),
                  (0.34, 1, 1),
                  (0.65, 0, 0),
                  (1, 1, 1))}

my_cmap = matplotlib.colors.LinearSegmentedColormap('my_colormap',cdict,256)


#Make the plot.
plt.clf()
plt.suptitle('Interatomic Phosphorus Distance Matrix', fontsize=18)
#plt.title('RNA P4-P6 Ribozyme Domain of Group I Intron (PDB_ID:1GID)')
plt.title('%s.pdb'%(pdbname))
plt.xlabel('Residue Number')
plt.ylabel('Residue Number')
cmap = cm.get_cmap('gist_heat',10)
#cmap = cm.get_cmap('Reds_r',20)
#cmap = cm.get_cmap('Blues_r',16)
#cmap = my_cmap
#cmap.set_bad('w')
plt.imshow(D, vmin=0.2, vmax=30, origin='upper',
    cmap=cmap, aspect='equal', interpolation='nearest')
plt.colorbar()
plt.grid(True)
#If you want to get a png figure uncomment the next line.
plt.savefig('%s_dmap.png'%(pdbname), dpi=200, format="png")
#plt.show()


