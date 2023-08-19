import imp


import cv2
import numpy as np
img1=cv2.imread("morphology.jpg")
img1=cv2.resize(img1,(500,500))
blue,green,red=cv2.split(img1)
blank_image=np.zeros((500,500),np.uint8)

Blues=cv2.merge([blue,blank_image,blank_image])
Green=cv2.merge([blank_image,green,blank_image])
Red=cv2.merge([blank_image,blank_image,red])

cv2.imshow("Blue",Blues)
cv2.imshow("Green",Green)
cv2.imshow("Red",Red)
cv2.waitKey(0)
cv2.destroyAllWindows()