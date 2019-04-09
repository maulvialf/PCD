# import library yang digunakan
import cv2
import numpy as np

# baca gambar sudo.pmg
img = cv2.imread("sudo.png")

# konversi gambar bgr menjadi grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# lakukan edge detection gambar grayscale yang didapatkan menggunakan canny edge detection
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# gunakan fungsi houghlines untuk mendapatkan garis.
# penjelasan parameter akan dijelaskan dibawah
# hasil kembalian adalah list berisi rho dan theta

lines = cv2.HoughLines(edges, 1, np.pi/180, 200)
# @param image 8-bit, single-channel binary source image. The image may be modified by the function.
# @param rho Distance resolution of the accumulator in pixels.
# @param theta Angle resolution of the accumulator in radians.
# @param threshold Accumulator threshold parameter. Only those lines are returned that get enough votes

# print lines[0][0] 
print len(lines) # hasil kembalian berbentuk [[[rho theta(dalam rad)]]]
# looping sebanyak jumlah lines yang ditemukan

for x in range(0, len(lines)):
    # looping setiap rho dan theta dari garis tersebut
    for rho, theta in lines[x]:
        
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
        print x1, y1
        print x2, y2
        
        # gambarkan garis berwarna (183,166,20)
        # dengan koordinat (x1, y1) dan (x2, y2)
        # setebal 6 pixel
        cv2.line(img, (x1,y1), (x2,y2), (183,166,20), 6)


# print lines
print(lines)
# tampilkan hasil edges detection
cv2.imshow('edges', edges)
# tampilkan gambar dengan line detection
cv2.imshow('final', img)
cv2.waitKey(0)


# import cv2
# import numpy as np
# # import library opencv dan numpy

# img = cv2.imread('coin.jpg', 0)
# print img
# # baca gambar dengan satu channel saja

# img = cv2.medianBlur(img, 5)
# # lakukan medianblur pada image

# cv2.imshow('detected circles', img)
# # tampilkan gambar sebelum dideteksi

# cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# # print cv2.HOUGH_GRADIENT
# circles = cv2.HoughCircles(img, cv2.cv.CV_HOUGH_GRADIENT, 1, 20, param1=290, param2=55, minRadius=0, maxRadius=0)
# print circles
# for i in circles[0, :]:
#     cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)

# cv2.imshow('detected circles', cimg)
# cv2.waitKey(0)
