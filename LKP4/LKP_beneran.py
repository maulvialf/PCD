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

def kernel_summation(box, kernel):   
	(row, col) = kernel.shape	
	hasil = 0
	for y in range(0, row):
		for x in range(0, col):
			hasil += box[y,x] * kernel[y,x]
	return hasil			

def konvolusi(image, kernel):	
	(row, col, chan) = image.shape
	(mrow, mcol) = kernel.shape	
	
	new_image = image.copy()
	for y in range(0, row):
		for x in range(0, col):
			if(x == 0 or y == 0 or y == row-1 or x == col -1):
				new_image.itemset((y, x, 0), 0)
				continue
			box = []
			# simple implementation
			# 3 x 3 matrix
			# Memasukkan array tetangga dengan menggunakan looping
			# Masih berfungsi jika matriks yang diberikan adalah 3x3
			box = get_adjescent(image,y,x,dim)
			new_pixel = kernel_summation(box, kernel)
			if(new_pixel >= 255):
				new_pixel = 255
			new_image.itemset((y, x, 0), new_pixel)

	return new_image

def get_adjescent(image,y,x,n):
	# Inisialisasi list
	box = np.zeros((n,n), np.float32)
	# Cari batas untuk seleksi matriks tetangga
	bound = n // 2 
	# nested loop untuk seleksi matriks tetangga
	y_idx = 0
	for i in range(-bound,bound+1,1):
		x_idx = 0
		for j in range(-bound,bound+1,1):
			# Masukin pixel tetangga dan pixel sendiri kedalam list
			box[y_idx,x_idx] = image[y+i,x+j]			
			"""
			Yang dimasukkan kedalam matriks adalah pixel image
			image[y-n,  x-n] . . image[y-n  , x+n] 
			image[y-n+1,x-n] . . image[y-n+1, x+n] 
				.
			image[y+n,  x-1] . . image[y+n  , x+n] 
			"""
			x_idx += 1
		y_idx += 1
	return box

# Baca image yang ingin diblur. Dalam tugas adalah LennaInput.jpg
image = load_image()
# Ubah menjadi greyscale
image_greyscale = greyscaling_image(image)
# Fungsi utama untuk melakukan medianBlur
kernel = np.ones((3,3), np.float32) / 9
image_blur = konvolusi(image_greyscale, kernel)
# tampilkan gambar yang telah diblur
cv2.imshow("konvolusi", image_blur)
cv2.waitKey(0)


# # class implementation
# class Image:
# 	def __init__(self, file_name):
# 		self.image = cv2.imread(file_name)
# 		self.image_greyscale = 	cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)


# class Konvolusi:
# 	def __init__(self, image, ):


# 	def kernel_summation(box, kernel):   
# 		(row, col) = kernel.shape	
# 		hasil = 0
# 		for y in range(0, row):
# 			for x in range(0, col):
# 				hasil += box[y,x] * kernel[y,x]
# 		return hasil			

# 	def get_adjescent(image,y,x,n):
# 		# Inisialisasi list
# 		box = np.zeros((3,3), np.float32)
# 		# Cari batas untuk seleksi matriks tetangga
# 		bound = n // 2 
# 		# nested loop untuk seleksi matriks tetangga
# 		y_idx = 0
# 		for i in range(-bound,bound+1,1):
# 			x_idx = 0
# 			for j in range(-bound,bound+1,1):
# 				# Masukin pixel tetangga dan pixel sendiri kedalam list
# 				box[y_idx,x_idx] = image[y+i,x+j]			
# 				"""
# 				Yang dimasukkan kedalam matriks adalah pixel image
# 				image[y-n,  x-n] . . image[y-n  , x+n] 
# 				image[y-n+1,x-n] . . image[y-n+1, x+n] 
# 					.
# 				image[y+n,  x-1] . . image[y+n  , x+n] 
# 				"""
# 				x_idx += 1
# 			y_idx += 1
# 		return box





# image = Image("LennaInput.jpg")
# image = Konvolusi(image.greyscale, kernel)