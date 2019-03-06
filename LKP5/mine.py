import numpy as np
import matplotlib.pyplot as plt
import cv2

#no. 1 dan 2
img = cv2.imread("car.png",0) #ambil citra dan jadikan dalam bentuk grayscale
row, col = img.shape #inisiasi row dan col
canvas1 = np.zeros((row,col), np.uint8)

#no.3, contrastStretching
def contrastStretching(img):
    frek = [0 for i in range(0,256)]
    a = 0
    b = 256
    c_min = frek[img[0,0]]
    d_max = frek[img[0,0]]
    for i in range(0,row):
        for j in range(0,col):
            frek[img[i,j]] += 1
            #if frek[img[i,j]] < c_min:
            #    c_min = frek[img[i,j]]
            #elif frek[img[i,j]] > d_max:
            #    d_max = frek[img[i,j]]
            #else:
            #    frek[img[i,j]] = frek[img[i,j]]
            frek[img[i,j]] = ((frek[img[i,j]]-min(frek)) * 1.0/(max(frek)-min(frek)))*255
            canvas1.itemset((i,j),frek[img[i,j]])

    print list(canvas1.ravel())

    plt.hist(canvas1.ravel(), 256, [0,256], histtype = 'bar', facecolor = 'blue')
    plt.show()
    return canvas1

contrastStretching(img)
cv2.imshow("Contrast Stretching", canvas1)

#plt.hist(img[:,:,0].ravel(), 256, [0,256], color="b")
#plt.hist(img[:,:,1].ravel(), 256, [0,256], color="g")
#plt.hist(img[:,:,2].ravel(), 256, [0,256], color="r")

#hitung frekuensi manual
#frek = [0 for i in range(0,256)]
#for i in range(0,row):
#    for j in range(0,col):
#        frek[img[i,j]] += 1

#hitung frekuensi cv2
#frek2 = cv2.calcHist([img],[0],None,[256],[0,256],)

#print(np.array(frek))
#print(frek2.flatten())

#canvas = np.zeros((row,col,1))

cv2.imshow("car", img)

cv2.waitKey(0)
cv2.destroyAllWindows()