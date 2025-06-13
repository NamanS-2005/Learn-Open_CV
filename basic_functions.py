import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# # Converting to Grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # Blurring the image
# blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# # Edge Cascading
# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny Edges', canny)

# # dilating the image
# dilated = cv.dilate(canny, (3, 3), iterations=1)
# cv.imshow('Dilated', dilated)

# # Eroding the image
# eroded = cv.erode(dilated, (3, 3), iterations=1)
# cv.imshow('Eroded', eroded)

# # Resize
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

# # Cropping the image
# cropped = img[50:100, 100:200]
# cv.imshow('Cropped', cropped)


cv.waitKey(0)