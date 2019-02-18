import cv2
import numpy as np
from pprint import pprint
# bit.ly/LKP3-PCD
# Ahmad Maulvi Alfansuri
# G64160081

def calculate(b, g, r):
	grey = r * 0.299 + g * 0.587 + b * 0.114
	return grey


def greyscaling_image(image):
	(row, col, chan) = image.shape
	print (image.shape)
	greyscale = np.zeros((row,col,1), np.uint8)
	for y in range(row):
		for x in range(col):
			# get pixel
			b, g, r = image[y, x]
			# calculate
			grey =  calculate(b,g,r)
			# assign
			greyscale.itemset((y,x,0), grey) # assign
	return greyscale	  

def load_image(filename="LennaInput.jpg"):
	image = cv2.imread(filename)
	return image

def get_median(array_of_pixel):
	# implementation of median
	# Sorting list pixel
	array_of_pixel.sort()
	panjang = len(array_of_pixel)
	# ambil titik tengah (median)
	mid = panjang / 2
	new_pixel =  array_of_pixel[mid]
	# kembalikan nilai pixel baru
	return new_pixel


def medianBlur(image, dim=3, normal=1):	
	(row, col, chan) = image.shape	
	new_image = image
	for y in range(1, row-1):
		for x in range(1, col-1):
			box = []
			# simple implementation for king move
			# 3 x 3 matrix
			if(normal == 0):	
				# Masukkan array tetangga secara manual
				box.append(image[y,x] )
				
				box.append(image[y+1,x] )			
				box.append(image[y-1,x] )

				box.append(image[y,x+1])			
				box.append(image[y,x-1])			

				box.append(image[y+1,x+1]) 			
				box.append(image[y+1,x-1]) 			

				box.append(image[y-1,x+1]) 			
				box.append(image[y-1,x-1]) 			
			else:
				# Experimental
				# Memasukkan array tetangga dengan menggunakan looping
				# Masih berfungsi jika matriks yang diberikan adalah 3x3
				box = get_list_of_adjescent(image,y,x,3)

			new_pixel = get_median(box)
			new_image.itemset((y, x, 0), new_pixel)

	return new_image

def get_list_of_adjescent(image,y,x,n):
	# Inisialisasi list
	box = []
	# Cari batas untuk seleksi matriks tetangga
	bound = n // 2 
	# nested loop untuk seleksi matriks tetangga
	for i in range(-bound,bound+1,1):
		for j in range(-bound,bound+1,1):
			# Masukin pixel tetangga dan pixel sendiri kedalam list
			box.append(image[y+i, x+j])
			"""
			Yang dimasukkan kedalam matriks adalah pixel image
			image[y-n,  x-n] . . image[y-n  , x+n] 
			image[y-n+1,x-n] . . image[y-n+1, x+n] 
				.
			image[y+n,  x-1] . . image[y+n  , x+n] 
			"""
	return box

# Baca image yang ingin diblur. Dalam tugas adalah LennaInput.jpg
image = load_image()
# Ubah menjadi greyscale
image_greyscale = greyscaling_image(image)
# Fungsi utama untuk melakukan medianBlur
image_blur = medianBlur(image_greyscale)
# tampilkan gambar yang telah diblur
cv2.imshow("medianBlur", image_blur)
cv2.waitKey(0)
