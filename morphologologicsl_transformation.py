import cv2
real_img=cv2.imread("morphology.jpg")
#now we need to perform morphological transformation on real image
# cv2.imshow("window",real_img)
# cv2.resizeWindow("window",(1000,1000))

#step-1
# canny=cv2.Canny(real_img,100,175)
# cv2.imshow("canny image",canny)

# step-2
# erosions=cv2.erode(canny,(7,7),iterations=2)
# cv2.imshow("Erode image",erosions)

# dilate=cv2.dilate(canny,(7,7),iterations=11)
# # cv2.imshow("dilate image",canny)
# erode=cv2.erode(dilate,(2,2),iterations=1)
# # cv2.imshow("Erode image",erode)

# erode2=cv2.erode(erode,(2,2),iterations=30)
# cv2.imshow("Erode image",erode2)

resizing=cv2.resize(real_img,(500,500),interpolation=cv2.INTER_LINEAR)
resizing2=cv2.resize(real_img,(500,500),interpolation=cv2.INTER_CUBIC)
cv2.imshow("showing..",resizing)
cv2.imshow("showing2..",resizing2)


crops=resizing[0:100,200:500]
cv2.imshow("crops",crops)

cv2.waitKey(0)
cv2.destroyAllWindows()
