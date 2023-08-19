import cv2
img=cv2.imread("face.jpeg")
img=cv2.resize(img,(500,500))
cv2.imshow("Face",img)
blur=cv2.blur(img,(17,17))#this is Avg blur
cv2.imshow("Blur",blur)
gussian_blur=cv2.GaussianBlur(img,(17,17),0)#0 is the std.
cv2.imshow("Gblur",gussian_blur)

bilatral_flter=cv2.bilateralFilter(img,5,100,100)
cv2.imshow("b_flter",bilatral_flter)

cv2.waitKey(0)