import cv2
import time
image=cv2.imread("fire.jpeg")
def rotation_image(img,angle,scale,point=None):
    (height,width)=img.shape[:2]
    if point==None:
        point=(img.shape[1]//2,img.shape[0]//2)
    rot_matrix=cv2.getRotationMatrix2D(point,angle,scale)
    dimension=(width,height)
    return cv2.warpAffine(img,rot_matrix,dimension)
count=1.0
angle=1
img=rotation_image(image,-45,count)
while True:
    img2=rotation_image(img,angle,count)
    img2=cv2.resize(img2,(500,500))
    cv2.imshow("windo)w",img2)
    time.sleep(0.01)
    angle=(angle+1)%360
    if cv2.waitKey(1)==ord('q'):
        break
cv2.destroyAllWindows()