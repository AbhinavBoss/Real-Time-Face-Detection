# Face detection on webcam 
import cv2

#Add Haarcascade pre-trained xml file for face detetction
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

#Capture the video through webcam (0 for default camera)
cap = cv2.VideoCapture(0) 
while 1:  
	_ , img = cap.read() 

	#Conversion of video to gray scale for face detection
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
	
	#Draw the rectangle
	for (x,y,w,h) in faces: 
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
	cv2.imshow('img',img) 
	
	#press q to exit
	if cv2.waitKey(30) & 0xff==ord('q'): 
		break
cap.release() 
cv2.destroyAllWindows() 
