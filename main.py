import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def face_detector(file_name):
	img = cv2.imread("zima-1.jpg")

	face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 1)

	for (x, y, width, height) in faces:
		cv2.rectangle(img, (x, y), (x + width, y + height), (255, 0, 0), 3)

	return img


img = face_detector("ogway.jpg")

cv2.imshow('Face detection', img)
cv2.waitKey(0)