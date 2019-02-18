import cv2
import numpy as np

# bit.ly/LKP3-PCD
# Ahmad Maulvi Alfansuri
# G64160081

def calculate(b, g, r):
	grey = r * 0.299 + g * 0.587 + b * 0.114
	return grey

def greyscaling_image(image):
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

def rata_rata_intensitas(image):
	jumlah = 0
	for y in range(row):
		for x in range(col):
			grey = image[y, x]
			jumlah += int(grey)
	rata = jumlah / (x * y)
	return rata

def perkuat_citra(image):
	new_image = np.zeros((row,col,1), np.uint8)
	rata_rata = rata_rata_intensitas(image)
	for y in range(row):
		for x in range(col):
			if(image[y, x] >= rata_rata):
				powered_pixel = (image[y, x]) * 2
				if(powered_pixel > 255):
					powered_pixel = 255
				elif(powered_pixel < 0):
					powered_pixel = 0
				new_image.itemset((y, x, 0), powered_pixel)
			elif(image[y, x] < rata_rata):
				powered_pixel = (image[y, x]) * 0.5
				if(powered_pixel > 255):
					powered_pixel = 255
				elif(powered_pixel < 0):
					powered_pixel = 0
				new_image.itemset((y, x, 0), powered_pixel)
				
	return new_image			

def difference(image1, image2):
	new_image = np.zeros((row,col,1), np.uint8)
	for y in range(row):
		for x in range(col):
			diff = int(image1[y, x]) - int(image2[y, x])
			if(diff > 255):
				diff = 255
			elif(diff < 0):
				diff = 0
			new_image.itemset((y, x, 0), diff)

	return new_image

def imageDiff(image1, image2, saved=1, debug=0, hasil="saved.jpg"):
	greyscale_1 = greyscaling_image(image1)
	greyscale_2 = greyscaling_image(image2)
	
	greyscale_1_powered = perkuat_citra(greyscale_1)
	greyscale_2_powered = perkuat_citra(greyscale_2)
	image = difference(greyscale_1_powered, greyscale_2_powered)
	
	if(debug == 1):	
		cv2.imshow("greyscale 1", greyscale_1)
		cv2.imshow("greyscale 2", greyscale_2)
		cv2.imshow("greyscale 1 powered", greyscale_1_powered)
		cv2.imshow("greyscale 2 powered", greyscale_2_powered)
	if(saved == 1):
		cv2.imwrite(hasil, image)
	return image


image1 = cv2.imread("k_cameraman.jpg")
image2 = cv2.imread("k_equalized.jpg")
(row, col, ch) = image1.shape
image_diff = imageDiff(image1, image2)
cv2.imshow("image diff", image_diff)
cv2.waitKey(0)