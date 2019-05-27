import serial
import time
import pygame
import pygame.camera
from pygame.locals import * 

ArduinoSerial=serial.Serial("/dev/ttyACM1", 9600)
while True:
	
	arduiOp=str(ArduinoSerial.readline())
	arduiOp=arduiOp.strip("\n")
	arduiOp=int(arduiOp)
	
	try:
		pygame.init()
		pygame.camera.init()
		if arduiOp:
			print ("clicked")
			
			cam = pygame.camera.Camera("/dev/video1",(640,480))
			cam.start()
			img = cam.get_image()
			pygame.image.save(img,"filename.jpg")
	except:
		pass
	
