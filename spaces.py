import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# plt.imshow(img)
# plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to l*a*b
Lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('Lab', Lab)

# BGR TO RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

# HSV to BGR
hsv_bgr = (cv.cvtColor(hsv, cv.COLOR_HSV2BGR))
cv.imshow('HSV to BGR', hsv_bgr)


cv.waitKey(0)