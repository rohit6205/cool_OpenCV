#import libs
import cv2
import numpy as np 


#capture video using webcam i.e. 0
# for video reading use full path of video location ex. VideoCapture('F:\\python_opencv\\video.mp4')
cap = cv2.VideoCapture(0)

while True:
	#read frames of video
	ret, frame = cap.read()

	#show images
	cv2.imshow('frame', frame)

	#Quit video by pressing 'q'
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

