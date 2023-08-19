import cv2
import matplotlib.pyplot as plt
#color spaces
img=cv2.imread("contour_image.png")
img=cv2.resize(img,(500,500))
cv2.imshow("window1",img)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img=cv2.resize(img,(500,500))
cv2.imshow("window2",img2)
img3=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img=cv2.resize(img,(500,500))
cv2.imshow("window3",img3)
img4=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
img=cv2.resize(img,(500,500))
cv2.imshow("window4",img4)

img5=cv2.cvtColor(img3,cv2.COLOR_HSV2BGR)



cv2.waitKey(0)
cv2.destroyAllWindows()