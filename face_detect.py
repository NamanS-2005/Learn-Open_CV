import cv2 as cv

img = cv.imread('Photos/faces.jpg')
# resized = cv.resize(img, (300, 400), interpolation = cv.INTER_LINEAR)
# cv.imshow('Resized', resized)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)

print(f'Number of faces found : {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv.imshow('Image with detected face', img)

cv.waitKey(0)