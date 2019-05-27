import cv2
import tryinglens as ocr
import serial
import time
from PIL import Image, ImageFilter
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from camera import cameraclick
from imageopen import photoback


# var=10


def Assign():
	file2=open("counter.txt","a+")
	s=file2.readlines()
	if len(s)==0:
		file2.write(str(0)+"\n")
		file2.close()
		file2=open("counter.txt","a+")
		s=file2.readlines()
	mycount=int(s[len(s)-1].strip("\n"))
	print("assign")
	key = cameraclick().lower()
	path =""

	cam2 = cv2.VideoCapture(2)
	cv2.namedWindow("testInfo")
	file = open("KeynInfo.txt", "a+")
	img_name = ""

	while(True):
		retI, frameI = cam2.read()
		
		cv2.imshow("testInfo", frameI)
		arduiOp=0
		ArduinoSerial=serial.Serial("/dev/ttyACM0", 9600)

		try:
			arduiOp=int(str(ArduinoSerial.readline().strip("\n")))
		except:
			pass

		if not retI:
			break

		k = cv2.waitKey(1)

		if arduiOp==3:
			print ("clicked")
			img_name="camera_info" + str(mycount) + ".jpg"
			print (img_name+"imgname")
			cv2.imwrite(img_name, frameI)
			mycount+=1
			file2.write(str(mycount)+"\n")
			file2.close()
			break

	file.write(str(key)+";"+str(img_name)+"\n")
	file.close()
	cv2.destroyAllWindows()
	return






		
		# while True:
	# 	ArduinoSerial=serial.Serial("/dev/ttyACM1", 9600)

	# 	arduiOp=str(ArduinoSerial.readline())
	# 	arduiOp=arduiOp.strip("\n")
	# 	arduiOp=int(arduiOp)
	# 	if(arduiOp==2):
	# 		#key image get clicked
	# 		#image goes through cloud vision
	# 		#key get stored in a variable
	# 	else if(arduiOp==3):
	# 		#derivation get clicked and get saved as per key
			
	# 		return 
def Recall():
	print("recall")
	photoback()
	return
	# while True:
	# 	ArduinoSerial=serial.Serial("/dev/ttyACM1", 9600)

	# 	arduiOp=str(ArduinoSerial.readline())
	# 	arduiOp=arduiOp.strip("\n")
	# 	arduiOp=int(arduiOp)		
	# 	if (arduiop==5):
	# 		#get image of key
	# 		#image goes through cloud vision
	# 		#matches from folder

	# 		#derivation image get open
	# 		return 

# def match(file, recallKey): # to match recall key with the list 
# 	# fileName is in string
# 	# recallKey in string
# 	key = []
# 	with open(file) as f:
# 		for line in f:
# 			line_elts = line.strip(" \n").split(",")
# 			try:
# 				key.append(line_elts[0])
# 			except ValueError:
# 				pass
# 	n = len(key)
# 	for i in range(0, n):
# 		if recallKey == key[i]:
# 			return key[i]
# 	fuzz = []
# 	for i in range(0, n):
# 		fuzz.append(fuzz.WRatio(recallKey, key[i]))
# 	maxIndex = fuzz.index(max(fuzz))
# 	return key[maxIndex]





def func():
	
	ArduinoSerial=serial.Serial("/dev/ttyACM0", 9600)
	while True:
		arduiOp=0
		try:
			arduiOp=int(str(ArduinoSerial.readline().strip("\n")))
			# print (arduiOp)
		except:
			print ("blah")
			pass
		# if (var==1):
		# 	f1()
		# 	var=10
		# if (var==4):
		# 	f2()
		# 	var=10

		if (arduiOp==1):
			# var=1
			Assign()
		elif (arduiOp==4):
			# var=4
			Recall()

func()