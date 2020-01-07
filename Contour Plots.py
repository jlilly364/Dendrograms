# -Program to plot contours of specific leaves
# -Currently tailored to N(H_2) map

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astrodendro import Dendrogram
from astropy import wcs

# Extract data, header, and WCS information from fits file
data, header = fits.getdata('G:/My Drive/Research/Yancy/Ayushi/NEW_crop_ColDens.fits', header='True')
wcs = wcs.WCS(header)

# Identify dendrogram files and load them
colDens = 'G:/My Drive/Research/Yancy/Ayushi/dendro_B10_ColDens_min3sig_delt3sig.fits'
NH3 = 'G:/My Drive/Research/Yancy/Ayushi/dendro_B10_NH3_min3sig_delt3sig.fits'
d = Dendrogram.load_from(colDens)
p = d.plotter()

# Plot map with contours on top of specific structures (identified by astrodendro ID)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1,projection =  wcs)
ax.imshow(data, origin='lower',cmap=plt.cm.Blues)
plt.title("Leaves from NH$_{2}$ Map ($\sigma=1.02x10^{20} cm^{-2})$")
p.plot_contour(ax, structure=12, lw=3, colors='red')
p.plot_contour(ax, structure=10, lw=3, colors='red')
p.plot_contour(ax, structure=5, lw=3, colors='red')
p.plot_contour(ax, structure=11, lw=3, colors='red')
p.plot_contour(ax, structure=8, lw=3, colors='red')
p.plot_contour(ax, structure=7, lw=3, colors='red')
p.plot_contour(ax, structure=3, lw=3, colors='red')