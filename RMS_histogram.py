# -Program to extract data from fits image and plot histogram
# -Used to find median value for sigma (rms) to make dendrograms

import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from decimal import Decimal

# Identify string of file
image_file = 'G:/My Drive/Research/Yancy/Youngmin/Ayushi/crop_err_ColDens.fits'

# Open file and extract data
hdu_list = fits.open(image_file)
image_data = hdu_list[0].data
hdu_list.close()

# Extract real and non-zero values from image data to 
image_data_new = np.array(image_data[~(np.isnan(image_data))])
image_data_nonzero = []
for item in image_data_new:
    if item !=0:
        image_data_nonzero.append(item)
#print str(np.count_nonzero(np.isnan(image_data_new)))

# Find important statistics of image data
minval = np.min(image_data_new)
maxval = np.max(image_data_new)
mean = np.mean(image_data_new)
median =  np.median(image_data_new)

# Make histogram of data and print the mean and median on it
statistics = ('Mean=%.3E'+'\n'+'Median=%.3E'+'\n')%(mean,median)
"""
print('Min = ' + str(minval))
print('Max = ' + str(maxval))
print('Mean = '+ str(mean))
print('Median = ' + str(median))
"""
plt.hist(image_data_nonzero, bins=200)
plt.title('Histogram of B10 RMS File', fontsize = 20)
plt.xlabel('Value of Pixel (H atoms/(cm^2))', fontsize = 14)
plt.ylabel('Number of Pixels (#)',fontsize = 14)
plt.annotate(statistics,xy=(.5,.65),xycoords='axes fraction',fontsize = 16)
plt.show()
#plt.savefig('G:/My Drive/Research/Yancy/Youngmin/Ayushi/err_ColDens_histogram.png')