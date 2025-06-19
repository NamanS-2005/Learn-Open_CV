import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# Averaging
average = cv.blur(img, (7, 7))
cv.imshow('Averaging', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussion blur', gauss)

# Median Blur
median =  cv.medianBlur(img, 3)
cv.imshow('Median', median)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 10, 35, 35)
cv.imshow('bilateral', bilateral)


cv.waitKey(0)