import numpy as np
import cv2
from time import * 

def load_image(filename="FACE DETECTION.png"):
    image = cv2.imread(filename)
    return image

def to_binary(image):
	(row, col, chan) = image.shape
	new_image = np.zeros((row,col,1), np.uint8) 
	for y in range(row):
		for x in range(col):
			if(image[y, x, 0] > 255/2):
				new_image[y, x] = 255
			else:
				new_image[y, x, 0] = 0
	return new_image

def show(image, title):
    # tulis ke disk
    cv2.imwrite(title, image)
    # tampilkan gambar
    cv2.imshow(title, image)

def drawlines(image, lines):
	new_image = image.copy()
	# for x in range(0, len(lines)):
	for rho, theta in lines:
		print rho, theta
		# transformasi kembali garis dalam bentuk rho dan theta
		# agar bisa di draw
		# https://stackoverflow.com/questions/7613955/hough-transform-equation
		a = np.cos(theta)
		b = np.sin(theta)

		# x0 menyimpan nilai r cos theta
		x0 = a*rho
		# y0 menyimpan nilai r sin theta
		y0 = b*rho

		# x1 menyimpan nilai r cos theta + 1000(- sin theta)
		x1 = int(x0 + 1000*(-b))
		# y1 menyimpan nilai r sin theta + 1000( cos theta)
		y1 = int(y0 + 1000*(a))

		# x2 menyimpan nilai r cos theta - 1000(- sin theta)        
		x2 = int(x0 - 1000*(-b))

		# x2 menyimpan nilai r cos theta - 1000(- sin theta)
		y2 = int(y0 - 1000*(a))
		
		# print koordinat penggaris
		
		# gambarkan garis berwarna (183,166,20)
		# dengan koordinat (x1, y1) dan (x2, y2)
		# setebal 6 pixel
		cv2.line(new_image, (x1,y1), (x2,y2), (183,166,20), 6)
	
	return new_image



def houghlines(edges, threshold):
	rho, theta = 0, 0
	# print edges
	thetas = np.deg2rad(np.arange(-90.0, 90.0))
	(row, col) = edges.shape
	nonzero_pixel = np.nonzero(edges)
	# nonzero_pixel[0] is x
	# nonzero_pixel[1] is y
	(x_list, y_list) = nonzero_pixel
	unit_len = len(x_list)
	accumulator = {}
	for ind in range(unit_len):
		x = x_list[ind]
		y = y_list[ind]
		for theta_index, theta in enumerate(thetas):
			rho = int(round(x * np.cos(theta) + y * np.sin(theta)))
			piece = (rho, theta)
			if piece not in accumulator:
			    accumulator[piece] = 1
			else:
			    accumulator[piece] += 1			
			
	lines = []
	for piece in accumulator:
		value = accumulator[piece]
		if(value > threshold):
			lines.append(piece)

	# print lines
	return lines

def main():
	# load image pada soal
	img = load_image('sudo.png')
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray, 50, 150, apertureSize=3)
	lines = houghlines(edges, 200)
	print lines
	img_drawed = drawlines(img, lines)
	show(edges, "edges.png")
	show(img_drawed, "img_drawed.png")
	show(img, "img.png")
	cv2.waitKey(0)


main()