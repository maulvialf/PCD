import numpy as np
import cv2
# bit.ly/LKP8-PCD

def treshold(img1):
    row, col, ch = img1.shape
    treshold = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            val = img1[i, j]
            if (val < 65):
                val = 0
            if (val > 65):
                val = 255

            treshold.itemset((i, j, 0), val)
    return treshold

def substract(image, image2):
    row, col = image.shape
    canvas = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            subs = int(image[i, j]) - int(image2[i, j])
            if (subs < 0):
                canvas.itemset((i, j, 0), 0)
            else:
                canvas.itemset((i, j, 0), subs)
    return canvas


def subrgbgray(rgb, treshold):
    row, col, raw = rgb.shape
    output = np.zeros((row, col, 3), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            if treshold[i, j] != 255:
                output.itemset((i, j, 0), 0)
                output.itemset((i, j, 1), 0)
                output.itemset((i, j, 2), 0)
            else:
                output[i, j] = rgb[i, j]
    return output


def ero(img, kernel):
    row, col, _ = img.shape
    canvas = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            hasil = 0

            if (i - kernel // 2 < 0) or (i + kernel // 2 > row - 1) or (j - kernel // 2) < 0 or (
                    j + kernel // 2 > col - 1):
                continue
            for ii in range(i - kernel // 2, i + kernel // 2 + 1):
                for jj in range(j - kernel // 2, j + kernel // 2 + 1):
                    if img[ii][jj] > 0:
                        hasil += 1
            if (hasil == kernel * kernel):
                canvas.itemset((i, j, 0), 255)
    return canvas


def dil(img, kernel):
    row, col, _ = img.shape
    canvas = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            hasil = 0

            if (i - kernel // 2 < 0) or (i + kernel // 2 > row - 1) or (j - kernel // 2) < 0 or (
                    j + kernel // 2 > col - 1):
                continue
            for ii in range(i - kernel // 2, i + kernel // 2 + 1):
                for jj in range(j - kernel // 2, j + kernel // 2 + 1):
                    if img[ii][jj] > 0:
                        hasil += 1
            if (hasil > 0):
                canvas.itemset((i, j, 0), 255)
    return canvas

def load_image(filename="FACE DETECTION.png"):
    image = cv2.imread(filename)
    return image


def main():
    # load image pada soal
    image = load_image('tomat-single.jpg')
    
    b,g,r = cv2.split(image)
    b = treshold(substract(r,g))

    cv2.imshow("r", r)
    cv2.imshow("g", g)

    cv2. imshow("1", substract(r,g))
    cv2.imshow("2", b)

    kernel3 = np.ones((3,3), np.uint8)
    kernel5 = np.ones((5,5), np.uint8)

    dilation5 = cv2.dilate(b, kernel3, iterations = 16)
    cv2.imshow("dilate", dilation5)
    final = cv2.erode(dilation5, kernel3, iterations = 16)

    # for i in range(0,16):
    #     b = dil(b,3)
        
    # for i in range(0,16):
    #     b = ero(b,3)
        
    cv2.imshow("hasil",b)
    cv2.imshow("final", final)

    b = subrgbgray(image, b)

    cv2.waitKey(0)

# Fungsi main yang menjalankan program
main()