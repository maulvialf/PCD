import cv2
import numpy as np
from pprint import pprint
from sys import *
import matplotlib.pyplot as plt

# bit.ly/LKP3-PCD
# Ahmad Maulvi Alfansuri
# G64160081

##### LKP5
def calculate(b, g, r):
	grey = r * 0.299 + g * 0.587 + b * 0.114
	return grey

def greyscaling_image(image):
	(row, col, chan) = image.shape
	# print (image.shape)
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

#####
# get max from list / array numpy
def get_max(image):
	if(AUTO == 1):
		return np.amax(image)
	else:
		# To do
		# To lazy to implement this
		(row, col, chan) = image.shape
		# for y in range(row):
		# 	for x in range(col):
	

# get min from list / array numpy
def get_min(image):
	if(AUTO == 1):
		return np.amin(image)
	else:
		pass

# return file
def load_image(filename="car.png"):
	image = cv2.imread(filename)
	return image

def contrast_formula(pixel, maks, mini):
	return 255.0 * (pixel - mini)/(maks - mini)

def contrast_stretching(image):
	(row, col, chan) = image.shape
	new_image = image.copy()
	maks = get_max(image)
	mini = get_min(image)
	# print(maks, mini)
	for y in range(row):
		for x in range(col):						
			pix = contrast_formula(image[y, x], maks, mini)
			new_image.itemset((y,x,0), pix)
	return new_image

def extract_intensity(image, include_zero = 0):
	(row, col, chan) = image.shape
	color_pixel = [0 for _ in range(256)]
	selected = {}
	for y in range(row):
		for x in range(col):
			color = image[y, x, 0]
			color_pixel[color] += 1

	for idx, isi in enumerate(color_pixel):
		if(isi != 0 or include_zero == 1):
			selected[idx] = isi
	return selected

def scaling(data, y_size, y_maks, y_margin=1):
	histValue = int(data * (y_size - y_margin)/ y_maks)
	return histValue

def get_maks_dict(image):
	maks = 0
	for i in image:
		if(image[i] > maks):
			maks = image[i]
	return maks

def get_min_dict(image):
	mini = 0
	for i in image:
		if(mini == 0):
			mini = image[i]
		elif(image[i] < mini):
			mini = image[i]
	return mini

def cummulative_distributive_function(image_intensity):
	cdf_table = image_intensity.copy()
	old_key = -1
	for key in image_intensity:
		if(old_key != -1):
			cdf_table[key] += cdf_table[old_key] 
		old_key = key		
	return cdf_table

def equalize(image):
	image_intensity = extract_intensity(image)
	cdf_table 	= cummulative_distributive_function(image_intensity)
	cdf_min 	= get_min_dict(cdf_table)
	(row, col, chan) = image.shape
	# Greyscale
	new_image = image.copy()
	L = 255.0
	for y in range(row):
		for x in range(col):
			v = image[y, x, 0]
			cdf_v = cdf_table[v]
			dividen = 1.0 * (row * col) - cdf_min
			h_v = int(round( L*(cdf_v - cdf_min)/dividen  ))
			# print (cdf_v - cdf_min),
			new_image.itemset((y,x,0), h_v)
	
	return new_image

# Sebelumnya buat pake manual. Ternyata disuruhnya pake matplot lib. Mau dihapus sayang cuman
def drawHistogram(image, xScale, yScale,title="Contoh",cummulative=0,include_zero=0):
	image_intensity = extract_intensity(image, include_zero)
	if(cummulative == 1):
		image_intensity = cummulative_distributive_function(image_intensity)
	yMaks = get_maks_dict(image_intensity)
	ySize = 128*yScale
	xSize = 256*xScale
	yMargin = 1
	image_hist = np.zeros((ySize,xSize,1), np.uint8)
	for x in image_intensity:
		value = image_intensity[x]
		high = scaling(value, ySize, yMaks)
		for y in range(high):
			image_hist.itemset((ySize-y-1, x, 0), 255)
	cv2.imshow(title, image_hist)

def drawHistogramWithMathplotlib(image, title, cummulative=0, method = 0):
	# kodingan awal
	if(method == 0):
		image_pixel = image.ravel()
		plt.hist(image_pixel, 256, cumulative=cummulative, facecolor = 'blue')
		plt.xlabel('Pixel')
		plt.ylabel('Jumlah pixel')
		plt.title(title)
		plt.show()

	# kodingan dari abangnya
	elif(method == 1):
		image_intensity = extract_intensity(image)
		id_n = [i for i in range(256)]
		image_intensity = cummulative_distributive_function(image_intensity)
		print image_intensity
		# plt.bar(id_n, freq)
		
	return 0

# Environtment variable
AUTO = 1
# baca image
image = load_image()
# Ubah menjadi greyscale
image_greyscale 				= greyscaling_image(image)
# Dengan contrast stretching
image_with_contrast_stretching  = contrast_stretching(image_greyscale)
# Dengan histogram equalize
image_equalize 					= equalize(image_greyscale)

# Normal Histogram
drawHistogram(image_greyscale, 1,1,"Normal")
drawHistogramWithMathplotlib(image_greyscale, "Normal")

# Image with contrast stretching
drawHistogram(image_with_contrast_stretching, 1,1,"Contrast Stretching")
drawHistogramWithMathplotlib(image_with_contrast_stretching, "Contrast Stretching")

# Image with equalize
drawHistogram(image_equalize, 1,1,"Equalize")
drawHistogramWithMathplotlib(image_equalize, "Equalize")

# Cummulative
drawHistogram(image_greyscale, 1,1, "cummulative", cummulative=1, include_zero=1)
drawHistogram(image_equalize, 1,1, "cummulative equalize", cummulative=1, include_zero=1)

drawHistogramWithMathplotlib(image_greyscale, "cummulative", cummulative=1)
drawHistogramWithMathplotlib(image_equalize, "cummulative equalize", cummulative=1)

extract_intensity(image_greyscale)
# drawHistogram(, 1,1,"Contrast Stretching")
cv2.imshow("original", image)
cv2.imshow("contrast_up", image_with_contrast_stretching)
cv2.imshow("equalize", image_equalize)
cv2.waitKey(0)
