import cv2
import numpy as np
from pprint import pprint
from sys import *
import matplotlib.pyplot as plt

# bit.ly/LKP5-PCD
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

def load_image(filename="car.png"):
	image = cv2.imread(filename)
	return image

def extract_image(image):
	pixel = np.array([0 for i in range(256)])
	(row, col, chan) = image.shape	
	for y in range(row):
		for x in range(col):
			pix = image[y, x, 0]
			pixel[pix] += 1
	return pixel

def transform(pr):
	rk = np.array([i for i in range(256)])
	for i in range(256):
		hasil = 0
		for j in range(i+1):
			hasil += 255 * pr[j]
		rk[i] = round(hasil)
	return rk

def new_data(sk, nk):
	box = {}
	for i in range(256):
		print sk[i], nk[i]
	for idx, i in enumerate(sk):
		if(i in box):
			box[i] += nk[idx]
		elif(i not in box):
			box[i] = nk[idx]
	return box

def normalized(box, n):
	new_box = {}
	for i in box:
		new_box[i] = box[i] * 1.0 / n
	return new_box

def extract_dict(data):
	key = []
	value = []
	for i in data:
		key.append(i)
		value.append(data[i])
	return((key, value))

def histogram(data):
	(x, y) = data
	plt.bar(x, y)
	plt.show()
	return 0	

def main():
	image = load_image()
	image_greyscale = greyscaling_image(image)
	nk = extract_image(image_greyscale)
	(row, col, chan) = image_greyscale.shape
	n = row * col * 1.0
	pr_rk = nk / n 
	sk = transform(pr_rk)
	new_dataaaaa = new_data(sk, nk)
	normalized_data = normalized(new_dataaaaa, n)
	data = extract_dict(normalized_data)
	return_value = histogram(data)

main()