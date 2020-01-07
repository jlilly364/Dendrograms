# Program to make small square crop of fits file using central coordinates

from astropy.io import fits
from astropy.nddata import Cutout2D
from astropy import coordinates
from astropy import units as u
from astropy.wcs import WCS
import matplotlib.pyplot as plt
from astropy.visualization.wcsaxes import WCSAxes

# Identify string of file
ColDens_file = 'G:/My Drive/Research/Yancy/Ayushi/TauL1521_ColDen_500_reso_masked.fits'
NH3_file = 'G:/My Drive/Research/Yancy/Youngmin/Maps/Youngmin_NH3_11_int_new.fits'

# Open file and extract data & WCS info
hdu_list = fits.open(NH3_file)
image_data = hdu_list[0].data
w = WCS(hdu_list[0].header)

# Define center of image via WCS coordinates (RA and Dec)
center = coordinates.SkyCoord(64.4583*u.deg, 28.1333*u.deg)#, frame='fk5')

# Use Cutout2D on the image data to cut a square around specified center
cutout = Cutout2D(image_data, center, size=[.20,.18]*u.deg, wcs=w)

# Show final cropped image
plt.imshow(cutout.data)

# Create a new FITS HDU for the cropped image
hdu = fits.PrimaryHDU(data=cutout.data, header=cutout.wcs.to_header())

# Write the HDU to a new file
#hdu.writeto('G:/My Drive/Research/Yancy/Ayushi/NEW_crop_ColDens.fits',overwrite=True)