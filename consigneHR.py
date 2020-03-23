# -*-coding:Utf-8 -*
import time 
import csv
import serial
import re


def parametrage_serie ():
	ser = serial.Serial('/dev/ttyACM0', 57600, timeout=1.5, writeTimeout=0.5)
	return ser


def envoi_consigne(H, ser):
	H=str(H)
	H=str("H"+H)
#	print(H)
	time.sleep(1)
	ser.write(H.encode('utf-8'))
	consigne = ser.readline()
	consigne=str(consigne)
	#print(consigne)
	consigne=consigne[2:7]
	#consigne=consigne[0:4]
	print("consigne_HR=",consigne)
	
