import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blanck', blank)

# # Paint the image a colour
# blank[:] = 0, 255, 0
# cv.imshow('Green', blank)

# # Paint in a particular area
# blank[200:300, 300:400] = 255, 0, 0
# cv.imshow('Blue', blank)

# # Draw a rectangle
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)
# cv.imshow('Rectangle', blank)

# # Draw a filled rectangle
# 1 # cv.rectangle(blank, (50, 50), (200, 200), (0, 0, 255), thickness=cv.FILLED)
# 2 # cv.rectangle(blank, (50, 50), (200, 200), (0, 0, 255), thickness=-1)
# cv.imshow('Rectangle Filled', blank)

# # Draw a circle
# cv.circle(blank, (250, 250), 50, (0, 255, 0), thickness=cv.FILLED)
# cv.imshow('Circle', blank)

# # Draw a line
# cv.line(blank, (0, 250), (250, 250), (255, 255, 255), thickness=3)
# cv.imshow('Line', blank)

# Write Text
cv.putText(blank, 'Hello World', (100, 200), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 20), 2)
cv.imshow('Text', blank)

cv.waitKey(0)