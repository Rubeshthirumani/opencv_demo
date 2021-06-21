import cv2
import numpy
import imutils

#img read 
img=cv2.imread("rubesh.jpg")



#eye_ROI
eye = img[120:160, 170:220]
img[100:140, 10:60] = eye



#image show
imgshow=cv2.imshow("Image", img)
cv2.waitKey(0)