import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread("morphology.jpg")
img=cv2.resize(img,(500,500))
gray_scale=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blank_image=np.zeros((500,500),np.uint8)
circle=cv2.circle(blank_image,(250,250),100,255,-1)
# mask=cv2.bitwise_and(blank_image,img)
# mask=cv2.resize(mask,(500,500))

cv2.imshow("mask",circle)

#normal gray scale image
# gray_scale_hist=cv2.calcHist([gray_scale],[0],None,[256],[0,256])
# plt.plot(gray_scale_hist)

#Of Mask

# blank_image=np.zeros((500,500),np.uint8)
# circle=cv2.circle(blank_image,(250,250),100,255,-1)
# mask=cv2.bitwise_and(blank_image,gray_scale)
# cv2.imshow("Masked",mask)
# gray_scale_hist=cv2.calcHist([gray_scale],[0],mask,[256],[0,256])

bitwising_and=cv2.bitwise_and(img,img,mask=circle)
# calculate Pixel Intensity of a image
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,col)
    plt.xlim([0,256])
plt.show()
cv2.waitKey(0)