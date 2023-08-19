import cv2
import numpy as np
img=cv2.imread("mask_image.jpg")
img=cv2.resize(img,(500,500))

blank_image=np.zeros((500,500),dtype=np.uint8)
circle=cv2.circle(blank_image.copy(),(250,250),100,255,-1)
cv2.imshow("Circled Image",circle)
cv2.imshow("Masked image",img)

bwise_and=cv2.bitwise_and(img,img,mask=circle)

rectangle=cv2.rectangle(blank_image.copy(),(30,30),(200,200),255,-1)
bwise_and2=cv2.bitwise_and(img,img,mask=rectangle)

cv2.imshow("Masked Image",bwise_and2)
cv2.imshow("Masked image",bwise_and)
cv2.waitKey(0)