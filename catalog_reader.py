# -Program to read out catalogs and extract useful physical properties
# -This script can be used in conjunction with "B10_NH3_Int_dendrogram_sigma_eval.py"
#  to plot the changes in physical properties as a function of min_delta

from astropy.io import fits
from astrodendro import Dendrogram
from astrodendro.analysis import PPStatistic
from astropy.table import Table
import numpy as np
import matplotlib.pyplot as plt

# Establish lists of quantities of interest
sigma = .026
sigmas = []
area_ellipses = []
area_exacts_main = []
area_exacts_main = np.array(area_exacts_main)

for i in range(1,11):
    sigma_new = i*sigma
    sigmas.append(sigma_new)
    area_exacts = []
    area_exacts = np.array(area_exacts)
    
    # Read-in catalog file and recreate catalog as cat
    catalog_file = 'G:/My Drive/Research/Yancy/Youngmin/min3sig_delt{1}sigNH3_11_INT.txt'.format(i,j)
    cat = Table.read(catalog_file,format='ascii.ecsv')

    area_exact = cat['area_exact']
    np.append(area_exacts,area_exact)

    area_ellipse = cat['area_ellipse']    
    area_ellipses.append(area_ellipse)

# Make scatter plot of area_exact vs. sigma
plt.scatter(sigmas,area_exacts)
plt.xlabel('min_delt (as multiple of .01)')
#plt.ylabel('area_exact')
"""
# Make scatter plot of area_ellpise vs. sigma
plt.scatter(sigmas,area_ellipses)
plt.xlabel('min_delt (as multiple of .01)')
#plt.ylabel('area_ellipses')

plt.legend(['area_exact','area_ellipses'])
"""