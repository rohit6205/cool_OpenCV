#import libs
import cv2
import numpy as np 

# read images
img = cv2.imread('F:\\python_opencv\\cat.jpg')
img2 = cv2.imread('F:\\python_opencv\\emily.jpg')

# resize images 
catSize = cv2.resize(img, (100, 150))
emilySize = cv2.resize(img2, (500, 300))


#Get the shape of Images
row, col, cannel = catSize.shape
row1, col1, cannel1 = emilySize.shape

roi = emilySize[0:row, 0:col]

#creating mask of the image
img2gray = cv2.cvtColor(catSize, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 80, 255, cv2.THRESH_BINARY_INV)
mask_inv = cv2.bitwise_not(mask)

# Creating background and foreground for the images 
emilySize_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)
catSize_fg = cv2.bitwise_and(catSize, catSize, mask=mask)

# add images togather where emilySize_bg is in background and catSize_fg is in foreground
dst = cv2.add(emilySize_bg, catSize_fg)
emilySize[0:row, 0:col] = dst 

# #show imgaes
# cv2.imshow('image1', catSize)
# cv2.imshow('image2', emilySize)
cv2.imshow('res',emilySize)
cv2.imshow('img2gray',img2gray)
cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('emilySize_bg',emilySize_bg)
cv2.imshow('catSize_fg',catSize_fg)
cv2.imshow('dst',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()