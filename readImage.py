#import libs
import numpy as np
import cv2
import matplotlib.pyplot as plt


# read image from computer
img = cv2.imread('C:\\original.jpg', 0) # 0 for reading in grayscale

#show images
cv2.imshow('image', img)

#wait for window untill any key pressed
cv2.waitKey(0)
cv2.destroyAllWindows()


#save images in directory
cv2.imwrite('grayscaleImage.jpg', img)