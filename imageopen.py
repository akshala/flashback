from PIL import Image, ImageFilter
import cv2
import serial
import time
import tryinglens as ocr
from recall import *


def photoback():
	cv2.destroyAllWindows()
	file=open("KeynInfo.txt","r")
	cam = cv2.VideoCapture(1)
	cv2.namedWindow("test3")
	arduiOp=0
	while(True):
		key=""
		
		ret, frame3 = cam.read()
		cv2.imshow("test3", frame3)

		
		
		if not ret:
			break
		cv2.waitKey(1)
		
		ArduinoSerial=serial.Serial("/dev/ttyACM0", 9600)
		try:
			arduiOp=int(str(ArduinoSerial.readline().strip("\n")))
		except:
			pass
		if arduiOp==5:
			print ("clicked")
			
			img_name="recall.jpg"
			cv2.imwrite(img_name, frame3)
			key=ocr.detect_document(img_name).lower()
			print(key)
			path = match(key)
			imageDisplay(path)
			break
				
def imageDisplay(imagePath):
	# input as string
	im=Image.open(imagePath)
	im=im.resize((1850,1000))
	im.show()
	return

# photoback()
