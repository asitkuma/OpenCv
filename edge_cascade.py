import cv2
img=cv2.imread("one_image.jpg")
img=cv2.GaussianBlur(img,(3,3),cv2.BORDER_DEFAULT)
canny_image=cv2.Canny(img,120,150)
cv2.imshow("window2",canny_image)
cv2.waitKey(0)
cv2.destroyAllWindows()