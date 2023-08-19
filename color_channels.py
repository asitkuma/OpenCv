import cv2
img=cv2.imread("morphology.jpg")
img=cv2.resize(img,(500,500))
blue,green,red=cv2.split(img)
blue=cv2.resize(blue,(500,500))
# print(blue)
cv2.imshow("Blue",blue)
green=cv2.resize(green,(500,500))
# print(green)
cv2.imshow("Green",green)
red=cv2.resize(red,(500,500))
# print(red)
cv2.imshow("Red",red)

img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("Image_RGB",img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()