# import library yang dibutuhkan
import cv2
import numpy as np
from matplotlib import pyplot as plt

# size filter
size = 30
# baca image
img = cv2.imread('tomat-single.jpg',0)
# ubah image dengan spasial domain menjadi frequency domain
f = np.fft.fft2(img)

fshift = np.fft.fftshift(f)
# hitung spectrum
magnitude_spectrum = 20*np.log(np.abs(fshift))

# gambanrkan image
plt.subplot(121),plt.imshow(img, cmap = 'gray')
# Labelling image
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# gambarkan hasil spectrum
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
# Labelling image
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

# tampilkan gambar
plt.show()

# ambil row and column
rows, cols = img.shape

# bagi dua row kolom
crow,ccol = rows/2 , cols/2

# hitung f_ishift
fshift[crow-size:crow+size, ccol-size:ccol+size] = 0

# kembalikan image dengan inverse fourier transform shift
f_ishift = np.fft.ifftshift(fshift)
# kembalikan image
img_back = np.fft.ifft2(f_ishift)
# jadikan domain frequency menjadi spatial domain kembali
img_back = np.abs(img_back)

# tampilkan hasil gambar.
# tampilkan image awal
plt.subplot(131),plt.imshow(img, cmap = 'gray')
# labelling
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# tampilkan hasil magnitude filter
plt.subplot(132),plt.imshow(20*np.log(np.abs(fshift)), cmap = 'gray')
# labelling
plt.title('Magnitude filter'), plt.xticks([]), plt.yticks([])
# tampilkan hasil image inverse
plt.subplot(133),plt.imshow(img_back, cmap = 'gray')
# labelling
plt.title('Image after HPF'), plt.xticks([]), plt.yticks([])
# tampilkan image
plt.show()

# hasil kembalian
cv2.imshow('res2',img_back)
cv2.waitKey(0)
cv2.destroyAllWindows()
