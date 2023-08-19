import cv2
import numpy as np
blank_image=np.zeros((500,500),np.uint8)
rectangles=cv2.rectangle(blank_image.copy(),(30,30),(470,470),255,-1)
cv2.imshow("Rectangle",rectangles)

circles=cv2.circle(blank_image.copy(),(250,250),250,255,-1)
cv2.imshow("Circle",circles)

bitwise_and=cv2.bitwise_and(rectangles,circles)
cv2.imshow("Bwise_and",bitwise_and)

bitwise_or=cv2.bitwise_or(rectangles,circles)
cv2.imshow("Bwise_or",bitwise_or)

bitwise_xor=cv2.bitwise_xor(rectangles,circles)
cv2.imshow("Bitwise_xor",bitwise_xor)

bitwise_not=cv2.bitwise_not(rectangles)
cv2.imshow("BwiseNot",bitwise_not)

cv2.waitKey(0)