import numpy as np
import cv2
#creating an empty image

empty_image=np.zeros((500,500,3),np.uint8)#uint8 is a image dtype
empty_image[100:150,320:500]=0,0,255

cv2.rectangle(empty_image,(10,10),(empty_image.shape[0]//2,empty_image.shape[1]//2),(0,255,0),3)

cv2.circle(empty_image,(255,255),30,(0,255,0),-1)

cv2.line(empty_image,(0,0),(255,255),(255,0,0),6)

cv2.putText(empty_image,"Hello Looser",(80,230),cv2.FONT_HERSHEY_TRIPLEX,1.0,(255,0,0),2)
cv2.imshow("empty",empty_image)


# gray_image=cv2.cvtColor(empty_image,cv2.COLOR_BGR2GRAY)

# cv2.imshow("gray",gray_image)


clr_img=cv2.imread("one_image.jpg")

cv2.imshow("window",clr_img)

blur_image=cv2.GaussianBlur(clr_img,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow("blur",blur_image)





cv2.waitKey(0)
cv2.destroyAllWindows()