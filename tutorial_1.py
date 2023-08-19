import cv2
var1=cv2.VideoCapture("one_demo.mp4")
while True:
    ret,value=var1.read()
    cv2.imshow("window",value)
    cv2.resizeWindow("window",(600,600))
    if cv2.waitKey(1)==ord('1'):
        break
cv2.destroyAllWindows()