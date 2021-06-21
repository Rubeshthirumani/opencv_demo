import cv2
import numpy
import imutils

#img read and display
img=cv2.imread("baby.jpg")



#REctangle over ROI
output = img.copy()
#cv2.rectangle(output, (170, 110), (270,220), (200, 150, 200), 3)
#circle_img = cv2.circle(img,(450,330), 200, (0,0,255), 2)
#cv2.imshow("Rectangle", output)
#cv2.imshow ("circle", circle_img )
line = cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.imshow ("LINE", line )
cv2.waitKey(0)


