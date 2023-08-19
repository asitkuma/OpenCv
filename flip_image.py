import time
import cv2
image=cv2.imread("face.jpeg")
image=cv2.resize(image,(500,500))
count=0
while True:
    flip=cv2.flip(image,(count)%2)
    cv2.imshow("win",flip)
    count+=1
    time.sleep(1)
    if cv2.waitKey(1)==ord('1'):
        break
cv2.destroyAllWindows()