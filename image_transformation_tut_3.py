#image transformation

import time
import cv2
import numpy as np

img=cv2.imread("morphology.jpg")
img=cv2.resize(img,(500,500))
# cv2.imshow("window",img)
def apply_trasformation(inp_img,x,y):
    transmatrix=np.float32([[1,0,x],[0,1,y]])#1,0,x means we want to change in x axis without disturbing y  and vice versa. for y it becomes 0
    dimensions=(inp_img.shape[1],inp_img.shape[0])#1 for width and 0 for height
    return cv2.warpAffine(inp_img,transmatrix,dimensions)
count1=-100
count2=-100

while True:
    while count1<0 and count2<0:    
        transforming=apply_trasformation(img,count1,count2)
        cv2.imshow("window",transforming)
        time.sleep(0.02)
        count1+=1
        count2+=1
        cv2.waitKey(1)
    while count1<101 and count2>-101:
        transforming=apply_trasformation(img,count1,count2)
        cv2.imshow("window",transforming)
        time.sleep(0.02)
        count1+=1
        count2-=1
        cv2.waitKey(1)
    while count1>-110:
        transforming=apply_trasformation(img,count1,count2)
        cv2.imshow("window",transforming)
        time.sleep(0.02)
        count1-=1
        cv2.waitKey(1)
    while count2<103:
        transforming=apply_trasformation(img,count1,count2)
        cv2.imshow("window",transforming)
        time.sleep(0.02)
        count2+=1
        cv2.waitKey(1)
    count1=-100
    count2=-100
    