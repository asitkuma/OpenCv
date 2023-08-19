import cv2
import matplotlib.pyplot as plt
img=cv2.imread("mask_image.jpg")
img=cv2.resize(img,(1000,1000))
gs=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
threshold,image=cv2.threshold(gs,70,255,cv2.THRESH_BINARY)
threshold,image2=cv2.threshold(gs,70,255,cv2.THRESH_BINARY_INV)
adaptive_thresh=cv2.adaptiveThreshold(gs,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,10)#here the integer 3 will be subtracted from the block size

adaptive_thresh2=cv2.adaptiveThreshold(gs,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,10)
cv2.imshow("Mean_C",adaptive_thresh)
cv2.imshow("Gussian_C",adaptive_thresh2)

#according to my point of view if u want darkness from the image then u must use mean_c from adaptive threshold and if u want lightness then u must use gussians
cv2.waitKey(0)