import imp
import cv2
import numpy as np
img=cv2.imread("contour_image.png")
canny=cv2.Canny(img,80,175)
canny=cv2.resize(canny,(500,500))
cv2.imshow("window",canny)

blank=np.zeros((500,500,3),np.uint8)
counter,herarchy=cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(blank,counter,-1,(0,255,0),1)
cv2.imshow("contour",blank)



cv2.waitKey(0)
cv2.destroyAllWindows()