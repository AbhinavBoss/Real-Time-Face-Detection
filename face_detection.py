# Face detection on webcam 
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
cap = cv2.VideoCapture(0) 
cap.set(3, 640)
cap.set(4, 480)
while 1:  
	_ , img = cap.read() 
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
	faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
	for (x,y,w,h) in faces: 
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
	cv2.imshow('img',img) 
	if cv2.waitKey(30) & 0xff==ord('q'): 
		break
cap.release() 
cv2.destroyAllWindows() 

# face detection on image
# import cv2
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# img = cv2.imread('3.png')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
# cv2.imshow('img', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

# import cv2
# def detect_faces(image_path):
#     face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#     img = cv2.imread(image_path)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#     return img
# image_paths = ['3.png', '4.png'] 
# for image_path in image_paths:
#     result_image = detect_faces(image_path)
#     cv2.imshow('Detected Faces', result_image)
#     cv2.waitKey(0)
# cv2.destroyAllWindows()