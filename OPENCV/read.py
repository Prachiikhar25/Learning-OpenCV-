import cv2 as cv
img= cv.imread('Photos/cat.webp')
# cv.imshow('Cat',img)
# the 1st argument is for the Window name and 2nd for the one i defined in imread
#cv.waitKey(0)
# it is a delay timestamp
# we need to read the docs
# if image is too big than the comp screen then cropped aayegi 

# now reading videos in opencv
capture=cv.VideoCapture('Video/dogv.mp4')# webcam access using integer 0, 1
while True:
	isTrue, frame = capture.read()
	# to display individual frame-->
	cv.imshow('Video', frame)

	if cv.waitKey(20) & 0xFF==ord('d'):#if letter d is pressed then break
		break 
capture.release()
cv.destroyAllWindows()
# cv.waitKey(0)