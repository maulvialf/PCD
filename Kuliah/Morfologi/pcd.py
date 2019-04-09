import numpy as np
import cv2

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


def floodfill(image, x, y):
	new_image = image.copy() 
	
	theStack = [ (x, y) ]

	while len(theStack) > 0:
		x, y = theStack.pop()
		if new_image[x, y] != 0:
			continue

		new_image[x, y] = 255

		if(x < new_image.shape[0] - 1): theStack.append( (x + 1, y) )  # right
		if(x > 0): theStack.append( (x - 1, y) )  # left
		if(y < new_image.shape[1] - 1 ): theStack.append( (x, y + 1) )  # down
		if(y > 0): theStack.append( (x, y - 1) )  # up

	return new_image

def show(image, title):
	# tulis ke disk
	cv2.imwrite(title, image)
	# tampilkan gambar
	cv2.imshow(title, image)

def inverse(image):
	new_image = image.copy()
	(row, col, chan) = new_image.shape    
	for y in range(row):
		for x in range(col):
			if(new_image[y, x] == 255):
				new_image[y, x] = 0
			else:
				new_image[y, x] = 255            

	return new_image

def selected_dil(img, kernel, select_filter):
    # ambil dimensi
    row, col, _ = img.shape
    # buat canvas
    canvas = img.copy()
    # loop matrix pixel
    for i in range(0, row):
        for j in range(0, col):
            if(select_filter[i, j] == 255):
	            hasil = 0
	            # mengecek ujung edge. Apakah
	            if (i - kernel // 2 < 0) or (i + kernel // 2 > row - 1) or (j - kernel // 2) < 0 or (
	                    j + kernel // 2 > col - 1):
	                continue
	            
	            # Loop submatrix n x n dari gambar. 
	            for ii in range(i - kernel // 2, i + kernel // 2 + 1):
	                for jj in range(j - kernel // 2, j + kernel // 2 + 1):
	                    # cek apakah pixel berwarna putih
	                    if img[ii][jj] > 0:
	                        # jika iya. jumlahkan hasil. hasil akan digunakan untuk melakukan pengecekan
	                        # apakah pixel tersebut fit, hit, atau tidak keduanya
	                        hasil += 1

	            # Jika hasil > 0. Maka pixel fit. Sehingga gambar akan mengalami perluasan (dilasi)
	            if (hasil > 0):
	                canvas.itemset((i, j, 0), 255)
    return canvas


def main():
	# preprocessing 
	image = load_image("aaaa.png")
	image_bin = to_binary(image)
	
	# cari hole
	image_hole = floodfill(image_bin, 0, 30)
	image_inverse = inverse(image_hole)
	img_selected = image_inverse

	# tanpa memakai morfologi
	image_hasil = img_selected + image_bin
	show(image_bin, "naon.png")
	show(image_bin_copy, "flood.png")
	show(image_inverse, "hasil.png")
	show(image_hasil, "hasilhasil.png")
	
	# pake morfologi
	region_filling = selected_dil(image_bin, 3, img_selected)
	for x in xrange(1,4):
		region_filling = selected_dil(region_filling, 3, img_selected)
	show(region_filling, "region_filling.png")	

	cv2.waitKey(0)

main()