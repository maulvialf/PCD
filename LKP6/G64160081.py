import cv2
import numpy as np
from pprint import pprint
from sys import *
import matplotlib.pyplot as plt

# bit.ly/LKP6-PCD
# Ahmad Maulvi Alfansuri
# G64160081

##### LKP6

def load_image(filename="FACE DETECTION.png"):
	image = cv2.imread(filename)
	return image

def conv_pixel_bgr_to_hsv(pixel):
	new_pixel = np.zeros((3), np.uint32)
	v = max(pixel)
	v = int(v) 
	s = 0
	h = 0
	if(v != 0):
		s = (v - min(pixel)) * 1.0 / v
	b, g, r = pixel
	b = int(b)
	g = int(g)
	r = int(r)
	if(v == min(pixel)):
		h == 0
	else:
		if(v == r):
			h =  (60 * (g - b))/(v - min(pixel))
		elif(v == g):
			h = 120 + (60 * (b - r))/(v - min(pixel))
		elif(v == b):
			h = 240 + ((60 * (r - g))/(v - min(pixel)))
		if(h < 0):
			h += 360

	v = int(v)
	s = int(255 * s)
	h = int(h / 2)
	
	new_pixel = np.array([h,s,v])
	return new_pixel

def conv_image_bgr_to_hsv(image):
	(row, col, chan) = image.shape
	new_image = np.zeros((row,col,3), np.uint8)	
	for y in range(row):
		for x in range(col):
			new_image[y, x] = conv_pixel_bgr_to_hsv(image[y, x])
	
	return new_image

def show(image, title):
	cv2.imwrite(title, image)
	cv2.imshow(title, image)

def masking(image):

	# must tuning this one
	lower_color = np.array([0, 0.10 * 255, 50])
	upper_color = np.array([50, 0.68 * 255, 255])
	(row, col, chan) = image.shape
	masker = np.zeros((row,col,1), np.uint8)	
		
	for y in range(row):
		for x in range(col):
			if( np.all(lower_color <= image[y, x]) and \
				np.all(upper_color >= image[y, x]) ) :
				masker[y,x,0] = 255
	return masker
			
def select_image(image, masker):
	(row, col, chan) = image.shape
	new_image = np.zeros((row,col,3), np.uint8)	
	for y in range(row):
		for x in range(col):
			if(np.all(masker[y,x,0] == 255)):
				new_image[y,x] = image[y,x] 
	return new_image

def main():
	image = load_image()
	# (row, col, chan) = image.shape
	# create canvas
	image_new = conv_image_bgr_to_hsv(image)
	image_2 = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	masker = masking(image_new)
	image_selected = select_image(image, masker)

	show(image_new, "naon.jpg")	
	show(image_2, "naon2.jpg")	
	show(masker, "masker.jpg")	
	show(image_selected, "image selected.jpg")	
	
	cv2.waitKey(0)

main()