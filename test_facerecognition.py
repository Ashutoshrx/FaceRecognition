import cv2

path=r"C:\Users\dell\Downloads\test_faces.jpg"


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

img= cv2.imread(path)
imgcvt=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgblur=cv2.blur(imgcvt,(5,5),1)


faces= face_cascade.detectMultiScale(imgcvt,1.1,4)

for(x,y,w,h) in faces:
    cv2.rectangle(imgcvt,(x,y),(x+w,y+h),(255,0,0),3)


cv2.imshow("Original image",imgcvt)
cv2.imshow("blur",imgblur)
cv2.waitKey(0)
