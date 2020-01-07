# This file creates and saves dendrogram plots, then writes the dendrogram data to a catalog
# (in the form of an Astropy table).

from astropy.io import fits
from astrodendro import Dendrogram, pp_catalog
import matplotlib.pyplot as plt
import numpy as np

# Define sigma (rms/error) value to establish astrodendro parameters
sigma = .026

# Define empty lists of leaves and total objects
leaves = []
objects = []

# Define file from which dendrogram should be created and extract file's data
image_file = 'G:/My Drive/Research/Yancy/Youngmin/Cropped Images/B10_NH3_int_crop.fits'
image = fits.getdata(image_file)

# Make dendrogram and structure catalog for varying min_delta with constant min_value
for i in range(1,11):
    # Compute dendrogram of file, save as fits file, and open interactive dendrogram viewer
    d = Dendrogram.compute(image, min_value=3*sigma, min_delta=multiple*sigma, min_npix=4, verbose=True)
    v=d.viewer()
    v.show()
    
    # Establish important metadata for catalog
    metadata = {}
    metadata['data_unit'] = u.Jy/u.beam
    metadata['spatial_scale'] = (1.67*(10**-3))*3600*u.arcsec
    metadata['frequency'] = (2.37*(10**10))*u.Hz
    metadata['beam_major'] = 0.008554*u.arcsec # FWHM
    metadata['beam_minor'] = 0.008554*u.arcsec # FWHM
    metadata['vaxis'] = 0
    
    # Write catalog
    cat = pp_catalog(d, metadata)
    cat['x_cen'].unit = u.deg
    cat['y_cen'].unit = u.deg
    text_file = 'G:/My Drive/Research/Yancy/Youngmin/February_14_Catalogs/B10/B10_min3sig_delt{0}sig.txt'.format(multiple)
    cat.write(text_file,format='ascii.ecsv',overwrite=True)
    
    # calculate number of leaves/objects
    num_leaves=len(d.leaves)
    #num_objects=len(d)
    leaves.append(num_leaves)
    #objects.append(num_objects)
    print("Number of Leaves for {0}*sigma: {1}".format(str(multiple),str(num_leaves)))
    print("Number of Objects for {0}*sigma: {1}".format(str(multiple), str(num_objects)))
    
"""
# Plot num_leaves trend
plt.scatter(multiples,leaves)
plt.xlabel('Multiple')
#plt.xlim(0)
plt.ylabel('Number of Leaves')
#plt.ylabel('Number of Objects')
#plt.yscale('log)')
#plt.ylim(0)
plt.title("Number of Leaves vs. Multiple*sigma (vary minVal)")
#plt.title("Number of Objects vs. Multiple*sigma (vary minVal)")
plt.show()
#plt.close()