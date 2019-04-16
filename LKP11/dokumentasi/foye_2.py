# import library yang dibutuhkan
import numpy as np
import cv2
from matplotlib import pyplot as plt

# read image
img = cv2.imread('tomat-single.jpg',0)

# ukuran filter
size = 30

# change image to discrete fourier transform
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
# shift hasil shifting
dft_shift = np.fft.fftshift(dft)
print dft, dft_shift

# perhitungan spectrum
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

# draw image awal
plt.subplot(121),plt.imshow(img, cmap = 'gray')
# labelling
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# draw magnitude spectrum
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

rows, cols = img.shape
crow,ccol = rows/2 , cols/2

# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows,cols,2),np.uint8)
mask[crow-size:crow+size, ccol-size:ccol+size] = 1

# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back2= 20*np.log(cv2.magnitude(fshift[:,:,0],fshift[:,:,1]))
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(121),plt.imshow(img_back2, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
