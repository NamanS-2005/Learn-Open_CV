import cv2 as cv


# For images, videos, and live videos
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# For only live videos
def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

    



# img = cv.imread('Photos/large_cat.jpg')
# cv.imshow('Cat', img)

# resized_image = rescaleFrame(img, scale = 0.2)
# cv.imshow('Resized Image', resized_image)

# cv.waitKey(0)



capture = cv.VideoCapture('Videos/video.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale = 0.3)
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()