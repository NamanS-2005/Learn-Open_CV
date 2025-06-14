import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)


# # Translation
# def translate(img, x, y):                                                                     # ------> x
#     transMat = np.float32([[1, 0, x], [0, 1, y]])                                             # |
#     dimensions = (img.shape[1], img.shape[0])                                                 # |
#     return cv.warpAffine(img, transMat, dimensions)                                           # y

# translated = translate(img, 100, 100)
# cv.imshow('Translated', translated)


# # Rotation
# def rotate(img, angle, rotPoint=None):
#     (height, width) = img.shape[:2]
#     if rotPoint is None:
#         rotPoint = (width//2, height//2)
    
#     rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#     dimensions = (width, height)

#     return cv.warpAffine(img, rotMat, dimensions)

# rotated = rotate(img, 45)
# cv.imshow('Rotated', rotated)


# # resizing an image
# resized = cv.resize(img, (500, 500), interpolation = cv.INTER_LINEAR)
# cv.imshow('Resized', resized)


# Flipping an image
# flip vertically ie about x-axis
flipped_v = cv.flip(img, 0)
cv.imshow('Flip_v', flipped_v)

# flip horizontally ie about y-axis
flipped_h = cv.flip(img, 1)
cv.imshow('Flip_h', flipped_h)

# flip by both axes
flipped_both = cv.flip(img, -1)
cv.imshow('Flip_both', flipped_both)

cv.waitKey(0)