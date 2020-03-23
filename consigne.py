# -*-coding:Utf-8 -*
import time 
import csv
import serial
import re

#parametrage liaison entre arduino et raspberry pi (ttyACM0 usb)
def parametrage_serie ():
	ser = serial.Serial('/dev/ttyACM0', 57600, timeout=1.5, writeTimeout=0.5)
	return ser

#envoie consigne de temperature a l'arduino pour la regulation
def envoi_consigne(C, ser):
	C=str(C)
	C=str("C"+C)
	#print(C)
	time.sleep(1)
	ser.write(C.encode('utf-8'))
	consigne = ser.readline()
	consigne=str(consigne)
	consigne=consigne[2:7]
	#consigne=consigne[0:4]
	print("consigne=",consigne)
	
#l'utilisateur rentre la consigne de temperature
def choix_consigne():
	C=-1
		
	while C<0:
		C=input("Quelle est la temperature de consigne:")
		try:
			C=int(C)
		except ValueError:
			print("vous n'avez pas saisi de nombre")
			C=-1
			continue
		if C<=0:
			print("le nombre est negatif ou egal a zero")
			C=-1
			
		if C>60:
			print("la temperature max est de 60°C")
			C=-1
	return C
	
#le raspberry pi envoie la lettre M à arduino, l'arduino renvoie le temps, la temperature et HR de la boite grace au capteur HyT271
#ces inforamation sont enregistrer dans un fichier disponible via le web
def boucle(fichier2, t0,ser):
	
	#ser = serial.Serial('/dev/ttyACM0', 57600, timeout=1, writeTimeout=1)
	#time.sleep(2)
	t1=time.time()
	M=str("M")
	ser.write(M.encode('utf-8'))
	temp = ser.readline()
	#time.sleep(1)
	#print(temp)
	temperature=str(temp)
	tacq=t1-t0
	temp=re.split("[,\s\']+", temperature)
	temperature=temp[1:2]
	temperature=str(temperature)
	temperature=temperature[2:-2]
	temperature=float(temperature)
	HR=temp[2:3]
	HR=str(HR)
	HR=HR[2:-2]
	HR=float(HR)	
	print("temps=""%.2f"%tacq, "temperature=",temperature, "HR=",HR)
	fichier2=("/var/www/html/resultats/C_temp_"+fichier2)
	file2=open(fichier2,"a")
	f= csv.writer(file2)
	f.writerow(["%.2f"%tacq, temperature, HR])
	file2.close()
	#ser.close()
	#time.sleep(10)

def main():
	ser = serial.Serial('/dev/ttyACM0', 57600, timeout=1, writeTimeout=1)
	time.sleep(1)
	M=str("M")
	ser.write(M.encode('utf-8'))
	temp = ser.read(10)
	#print(temp)
