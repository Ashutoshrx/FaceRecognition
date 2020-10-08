import cv2
import numpy as np
#kernel=np.ones((5),np.uint8)
#print(kernel)

#print("OpenCV imported")


##### IMPORTING IMAGE FROM A FOLDER####
''''
img=cv2.imread("C:\\Users\dell\Pictures\Saved Pictures\FAM.jpg")
cv2.imshow("Output",img)
cv2.waitKey(0)
''''
#####IMPORTING A VIDEO USING WEBCAM####

''''cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,1000)#For brighness
while True:
#   success,img=cap.read()
#   cv2.imshow("video",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
''''
####FINDING THE EDGES OF AN IMAGE ####

''''path="C:\\Users\dell\Pictures\Saved Pictures\IMG_1538~2.jpg"

img=cv2.imread(path)
imgresize=cv2.resize(img,(500,500))
imgcanny=cv2.Canny(imgresize,200,200)
imgdilated=cv2.dilate(imgcanny,kernel,iterations=1)
cv2.imshow("Orginial Image",img)
cv2.imshow("Canny Image",imgcanny)
cv2.imshow("Dilated Image",imgdilated)
cv2.imshow("Resize Image",imgresize)
cv2.waitKey(0)
print(img.shape)''''

###### DRAWING A LINE ON AN IMAGE ######

''''img=np.zeros((450,500,3))
img[:]=(0,0,255)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(255,0,0))
cv2.rectangle(img,(120,130),(350,350),(255,255,0))

cv2.imshow("Image",img)
cv2.waitKey(0)''''

#### CHAPTER 5 ###  GETTING WARP PERSPECTIVE#########IMPORTANT##########

''''path="C:\\Users\dell\Pictures\Camera Roll\wrap.jpg"
img=cv2.imread(path)

width,height=250,350

pts1=np.float32([[524,28],[738,43],[490,423],[797,417]])
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix=cv2.getPerspectiveTransform(pts1,pts2)
#imgop=cv2.warpPerspective(img,matrix,(width,height))

#imgcanny=cv2.Canny(imgop,200,200)
#kernel=np.ones((5),np.uint8)
#imgdilate=cv2.dilate(imgcanny,kernel)

#cv2.imshow("Canny image",imgcanny)
#cv2.imshow("Wrap image",imgop)
#cv2.imshow("Dilated image",imgdilate)
#cv2.waitKey(0)
'''''

