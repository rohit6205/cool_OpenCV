import cv2
import numpy as np 

#read images from computer
img = cv2.imread('F:\\python_opencv\\cat.jpg')
img1 = cv2.imread('F:\\python_opencv\\catfears.jpg')
img2 = cv2.imread('F:\\python_opencv\\emily.jpg')


# making images in identical in size 
sameSize = cv2.resize(img, (500, 300))
sameSize1 = cv2.resize(img1, (500, 300))
sameSize2 = cv2.resize(img2, (500, 300))

#Add images togather
add = sameSize + sameSize1

#Add images togather using add()
#(155,211,79) + (50, 170, 200) = 205, 381, 279...translated to (205, 255,255)
addUsingCV = cv2.add(sameSize, sameSize1)

# add images using addWeighted()
weighted = cv2.addWeighted(sameSize, 0.4, sameSize1, 0.6, 0)

#Show images
# cv2.imshow('image', sameSize)
# cv2.imshow('image2', sameSize1)
# cv2.imshow('image3', sameSize2)
cv2.imshow('add', add)
cv2.imshow('addUsingCV', addUsingCV)
cv2. imshow('weighted', weighted)

cv2.waitKey(0)
cv2.destroyAllWindows()