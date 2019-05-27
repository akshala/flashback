import cv2
import serial
import time
import tryinglens as ocr
 
def cameraclick():

	# file=open("hash.txt","a")
	cam = cv2.VideoCapture(1)

	cv2.namedWindow("test")
	# cam2 = cv2.VideoCapture(0)

	# cv2.namedWindow("test2")
	# count=1
	# img_counter = 0
	key = ""

	while True:
		# ret2, frame2 = cam2.read()
		ret, frame = cam.read()
		
		cv2.imshow("test", frame)
		# cv2.imshow("test", frame)
		# cv2.imshow("test2", frame2)
		arduiOp=0
		ArduinoSerial=serial.Serial("/dev/ttyACM0", 9600)
		try:
			arduiOp=int(str(ArduinoSerial.readline().strip("\n")))
			print (arduiOp)
		except:
			pass
		if not ret:
			break
		# if not ret2:
		# 	break   
		# cv2.waitKey(1)
		k = cv2.waitKey(1)

		# if k%256 == 27:
		#     # ESC pressed
		#     print("Escape hit, closing...")
		#     break
		# elif k%256 == 32:
		    # SPACE pressed
		    # img_name = "opencv_frame_{}.png".format(img_counter)
		if arduiOp==2:
			print ("clicked")
			# cv2.imshow("test", frame)
			img_name="camera1.jpg"
			cv2.imwrite(img_name, frame)
			key=ocr.detect_document(img_name)
			break
			# arduiOp2=int(str(ArduinoSerial.readline().strip("\n")))
			# if arduiOp2==2:
			# 	print ("clicked2")
			# 	cv2.imshow("test2", frame2)
			# 	img_name2="camera"+str(count)+"_info.jpg"
			# 	cv2.imwrite(img_name2, frame2)
			# 	record=key+";"+img_name2+"\n"
			# 	file.write(record)
			# 	count+=1
			# break
		    # print("{} written!".format(img_name))
		    # img_counter += 1

	print(key)
	print("Key Printed")
	cam.release()
	cv2.destroyAllWindows()
	return key

# cameraclick()