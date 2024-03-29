# import library yang dibutuhkan
import numpy as np
import cv2
from matplotlib import pyplot as plt

# read image
img = cv2.imread('tomat-single.jpg',0)

# ukuran filter
size = 50

# change image to discrete fourier transform
dft = cv2.dft(np.float32(img),flags = cv2.DFT_COMPLEX_OUTPUT)
# shift hasil shifting
dft_shift = np.fft.fftshift(dft)
# perhitungan magnitude spectrum dari real dan imaginary number
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

# draw image awal
plt.subplot(121),plt.imshow(img, cmap = 'gray')
# labelling
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# draw magnitude spectrum
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
# labelling
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()

# ambil dimensi image
rows, cols = img.shape
# ambil setengan posisi tengah image
crow,ccol = rows/2 , cols/2

# create a mask first, center square is 1, remaining all zeros
# buat masking untuk menseleksi image
mask = np.zeros((rows,cols,2),np.uint8)
# filter image dimana pixel diseleksi. terlihat bahwa filter berukuran size diletakkan berada ditengah
mask[crow-size:crow+size, ccol-size:ccol+size] = 1

# apply mask and inverse DFT
# lakukan seleksi dft dengan mask
fshift = dft_shift*mask
# kembalikan fourier shift ke fourier inverse
f_ishift = np.fft.ifftshift(fshift)
# kembalikan fourier inverse ke image spasial
dfti = cv2.idft(f_ishift)
# hitung magnitude dari fshift
magnitude = 20*np.log(cv2.magnitude(fshift[:,:,0],fshift[:,:,1]))
# hitung gambar asli dari magnitute
image_kembalian = cv2.magnitude(dfti[:,:,0],dfti[:,:,1])

plt.subplot(121),plt.imshow(magnitude, cmap = 'gray')
plt.title('Magnitude filterize'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(image_kembalian, cmap = 'gray')
plt.title('Image kembalian'), plt.xticks([]), plt.yticks([])
plt.show()
