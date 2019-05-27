import serial

while True:
	arduiOp=0
	ArduinoSerial=serial.Serial("/dev/ttyACM0", 9600)
	try:

		arduiOp=int(str(ArduinoSerial.readline().strip("\n")))
		print (arduiOp)
	except:
		pass

