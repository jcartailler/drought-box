import sys
import time 
import csv
from Phidget22.Devices.VoltageRatioInput import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *

ch1  = VoltageRatioInput()
ch10 = VoltageRatioInput()
ch11 = VoltageRatioInput()
ch12 = VoltageRatioInput()
ch13 = VoltageRatioInput()
ch2  = VoltageRatioInput()
ch20 = VoltageRatioInput()
ch21 = VoltageRatioInput()
ch22 = VoltageRatioInput()
ch23 = VoltageRatioInput()

def init ():
	
	ch1.setDeviceSerialNumber(513024)
	ch1.openWaitForAttachment(5000)
	ch1.setBridgeGain(1)
	ch1.setDataInterval(8)
	ch1.setBridgeEnabled(1)
	ch1.close()
	time.sleep(0.5)
	ch2.setDeviceSerialNumber(514788)
	ch2.openWaitForAttachment(5000)
	ch2.setBridgeGain(1)
	ch2.setDataInterval(8)
	ch2.setBridgeEnabled(1)
	ch2.close()
	time.sleep(0.5)
	ch10.setChannel(0)
	ch10.setDeviceSerialNumber(513024)
	ch10.openWaitForAttachment(5000)
	ch11.setChannel(1)
	ch11.setDeviceSerialNumber(513024)
	ch11.openWaitForAttachment(5000)
	ch12.setChannel(2)
	ch12.setDeviceSerialNumber(513024)
	ch12.openWaitForAttachment(5000)
	ch13.setChannel(3)
	ch13.setDeviceSerialNumber(513024)
	ch13.openWaitForAttachment(5000)
	print("wait 5s")
	time.sleep(5)
	ch20.setChannel(0)
	ch20.setDeviceSerialNumber(514788)
	ch20.openWaitForAttachment(5000)
	ch21.setChannel(1)
	ch21.setDeviceSerialNumber(514788)
	ch21.openWaitForAttachment(5000)
	ch22.setChannel(2)
	ch22.setDeviceSerialNumber(514788)
	ch22.openWaitForAttachment(5000)
	ch23.setChannel(3)
	ch23.setDeviceSerialNumber(514788)
	ch23.openWaitForAttachment(5000)
	print("wait 5s")
	time.sleep(5)
	
	
def lecture(fichier, n, t1):
	if n==1:
		ch10.open()
		m11=ch10.getVoltageRatio()
		time.sleep(0.1)
		m12=ch10.getVoltageRatio()
		time.sleep(0.1)
		m13=ch10.getVoltageRatio()
		time.sleep(0.1)
		m14=ch10.getVoltageRatio()
		time.sleep(0.1)
		m15=ch10.getVoltageRatio()
		m1=(m11+m12+m13+m14+m15)/5	
		file=open("/var/www/html/resultats/C_"+fichier,"a")
		f= csv.writer(file)
		f.writerow([t1, m1])
		file.close()
		print("temps= %.2f" %t1,  "mesure=",m1)
	if n==2:
		ch10.open()
		m11=ch10.getVoltageRatio()
		time.sleep(0.1)
		m12=ch10.getVoltageRatio()
		time.sleep(0.1)
		m13=ch10.getVoltageRatio()
		time.sleep(0.1)
		m14=ch10.getVoltageRatio()
		time.sleep(0.1)
		m15=ch10.getVoltageRatio()
		m1=(m11+m12+m13+m14+m15)/5
		ch11.open()
		m21=ch11.getVoltageRatio()
		time.sleep(0.1)
		m22=ch11.getVoltageRatio()
		time.sleep(0.1)
		m23=ch11.getVoltageRatio()
		time.sleep(0.1)
		m24=ch11.getVoltageRatio()
		time.sleep(0.1)
		m25=ch11.getVoltageRatio()
		m2=(m21+m22+m23+m24+m25)/5
		file=open("/var/www/html/resultats/C_"+fichier,"a")
		f= csv.writer(file)
		f.writerow([t1, m1, m2])
		file.close()
		print("temps= %.2f" %t1,  "mesure=",m1, ",", m2)
	if n==3:
		ch10.open()
		m11=ch10.getVoltageRatio()
		time.sleep(0.1)
		m12=ch10.getVoltageRatio()
		time.sleep(0.1)
		m13=ch10.getVoltageRatio()
		time.sleep(0.1)
		m14=ch10.getVoltageRatio()
		time.sleep(0.1)
		m15=ch10.getVoltageRatio()
		m1=(m11+m12+m13+m14+m15)/5
		ch11.open()
		m21=ch11.getVoltageRatio()
		time.sleep(0.1)
		m22=ch11.getVoltageRatio()
		time.sleep(0.1)
		m23=ch11.getVoltageRatio()
		time.sleep(0.1)
		m24=ch11.getVoltageRatio()
		time.sleep(0.1)
		m25=ch11.getVoltageRatio()
		m2=(m21+m22+m23+m24+m25)/5
		ch12.open()
		m31=ch12.getVoltageRatio()
		time.sleep(0.1)
		m32=ch12.getVoltageRatio()
		time.sleep(0.1)
		m33=ch12.getVoltageRatio()
		time.sleep(0.1)
		m34=ch12.getVoltageRatio()
		time.sleep(0.1)
		m35=ch12.getVoltageRatio()
		m3=(m31+m32+m33+m34+m35)/5
		file=open("/var/www/html/resultats/C_"+fichier,"a")
		f= csv.writer(file)
		f.writerow([t1, m1, m2, m3])
		file.close()
		print("temps= %.2f" %t1,  "mesure=",m1, ",", m2, ",", m3)
	if n==4:
		ch10.open()		
		m11=ch10.getVoltageRatio()
		time.sleep(0.1)
		m12=ch10.getVoltageRatio()
		time.sleep(0.1)
		m13=ch10.getVoltageRatio()
		time.sleep(0.1)
		m14=ch10.getVoltageRatio()
		time.sleep(0.1)
		m15=ch10.getVoltageRatio()
		m1=(m11+m12+m13+m14+m15)/5
		ch11.open()
		m21=ch11.getVoltageRatio()
		time.sleep(0.1)
		m22=ch11.getVoltageRatio()
		time.sleep(0.1)
		m23=ch11.getVoltageRatio()
		time.sleep(0.1)
		m24=ch11.getVoltageRatio()
		time.sleep(0.1)
		m25=ch11.getVoltageRatio()
		m2=(m21+m22+m23+m24+m25)/5
		ch12.open()
		m31=ch12.getVoltageRatio()
		time.sleep(0.1)
		m32=ch12.getVoltageRatio()
		time.sleep(0.1)
		m33=ch12.getVoltageRatio()
		time.sleep(0.1)
		m34=ch12.getVoltageRatio()
		time.sleep(0.1)
		m35=ch12.getVoltageRatio()
		m3=(m31+m32+m33+m34+m35)/5
		ch13.open()
		m41=ch13.getVoltageRatio()
		time.sleep(0.1)
		m42=ch13.getVoltageRatio()
		time.sleep(0.1)
		m43=ch13.getVoltageRatio()
		time.sleep(0.1)
		m44=ch13.getVoltageRatio()
		time.sleep(0.1)
		m45=ch13.getVoltageRatio()
		m4=(m41+m42+m43+m44+m45)/5
		file=open("/var/www/html/resultats/C_"+fichier,"a")
		f= csv.writer(file)
		f.writerow([t1, m1, m2, m3, m4])
		file.close()
		print("temps= %.2f" %t1,  "mesure=",m1, ",", m2, ",", m3, ",", m4)
	if n==5:
		ch10.open()
		m11=ch10.getVoltageRatio()
		time.sleep(0.1)
		m12=ch10.getVoltageRatio()
		time.sleep(0.1)
		m13=ch10.getVoltageRatio()
		time.sleep(0.1)
		m14=ch10.getVoltageRatio()
		time.sleep(0.1)
		m15=ch10.getVoltageRatio()
		m1=(m11+m12+m13+m14+m15)/5
		ch11.open()
		m21=ch11.getVoltageRatio()
		time.sleep(0.1)
		m22=ch11.getVoltageRatio()
		time.sleep(0.1)
		m23=ch11.getVoltageRatio()
		time.sleep(0.1)
		m24=ch11.getVoltageRatio()
		time.sleep(0.1)
		m25=ch11.getVoltageRatio()
		m2=(m21+m22+m23+m24+m25)/5
		ch12.open()
		m31=ch12.getVoltageRatio()
		time.sleep(0.1)
		m32=ch12.getVoltageRatio()
		time.sleep(0.1)
		m33=ch12.getVoltageRatio()
		time.sleep(0.1)
		m34=ch12.getVoltageRatio()
		time.sleep(0.1)
		m35=ch12.getVoltageRatio()
		m3=(m31+m32+m33+m34+m35)/5
		ch13.open()
		m41=ch13.getVoltageRatio()
		time.sleep(0.1)
		m42=ch13.getVoltageRatio()
		time.sleep(0.1)
		m43=ch13.getVoltageRatio()
		time.sleep(0.1)
		m44=ch13.getVoltageRatio()
		time.sleep(0.1)
		m45=ch13.getVoltageRatio()
		m4=(m41+m42+m43+m44+m45)/5
		ch20.open()
		m51=ch20.getVoltageRatio()
		time.sleep(0.1)
		m52=ch20.getVoltageRatio()
		time.sleep(0.1)
		m53=ch20.getVoltageRatio()
		time.sleep(0.1)
		m54=ch20.getVoltageRatio()
		time.sleep(0.1)
		m55=ch20.getVoltageRatio()
		m5=(m51+m52+m53+m54+m55)/5
		file=open("/var/www/html/resultats/C_"+fichier,"a")
		f= csv.writer(file)
		f.writerow([t1, m1, m2, m3, m4, m5])
		file.close()
		print("temps= %.2f" %t1,  "mesure=",m1, ",", m2, ",", m3, ",", m4, ",", m5)
	if n==6:
		ch10.open()
		m11=ch10.getVoltageRatio()
		time.sleep(0.1)
		m12=ch10.getVoltageRatio()
		time.sleep(0.1)
		m13=ch10.getVoltageRatio()
		time.sleep(0.1)
		m14=ch10.getVoltageRatio()
		time.sleep(0.1)
		m15=ch10.getVoltageRatio()
		m1=(m11+m12+m13+m14+m15)/5
		ch11.open()
		m21=ch11.getVoltageRatio()
		time.sleep(0.1)
		m22=ch11.getVoltageRatio()
		time.sleep(0.1)
		m23=ch11.getVoltageRatio()
		time.sleep(0.1)
		m24=ch11.getVoltageRatio()
		time.sleep(0.1)
		m25=ch11.getVoltageRatio()
		m2=(m21+m22+m23+m24+m25)/5
		ch12.open()
		m31=ch12.getVoltageRatio()
		time.sleep(0.1)
		m32=ch12.getVoltageRatio()
		time.sleep(0.1)
		m33=ch12.getVoltageRatio()
		time.sleep(0.1)
		m34=ch12.getVoltageRatio()
		time.sleep(0.1)
		m35=ch12.getVoltageRatio()
		m3=(m31+m32+m33+m34+m35)/5
		ch13.open()
		m41=ch13.getVoltageRatio()
		time.sleep(0.1)
		m42=ch13.getVoltageRatio()
		time.sleep(0.1)
		m43=ch13.getVoltageRatio()
		time.sleep(0.1)
		m44=ch13.getVoltageRatio()
		time.sleep(0.1)
		m45=ch13.getVoltageRatio()
		m4=(m41+m42+m43+m44+m45)/5
		ch20.open()
		m51=ch20.getVoltageRatio()
		time.sleep(0.1)
		m52=ch20.getVoltageRatio()
		time.sleep(0.1)
		m53=ch20.getVoltageRatio()
		time.sleep(0.1)
		m54=ch20.getVoltageRatio()
		time.sleep(0.1)
		m55=ch20.getVoltageRatio()
		m5=(m51+m52+m53+m54+m55)/5
		ch21.open()
		m61=ch21.getVoltageRatio()
		time.sleep(0.1)
		m62=ch21.getVoltageRatio()
		time.sleep(0.1)
		m63=ch21.getVoltageRatio()
		time.sleep(0.1)
		m64=ch21.getVoltageRatio()
		time.sleep(0.1)
		m65=ch21.getVoltageRatio()
		m6=(m61+m62+m63+m64+m65)/5
		file=open("/var/www/html/resultats/C_"+fichier,"a")
		f= csv.writer(file)
		f.writerow([t1, m1, m2, m3, m4, m5, m6])
		file.close()
		print("temps= %.2f" %t1,  "mesure=",m1, ",", m2, ",", m3, ",", m4, ",", m5, ",", m6)
	if n==7:
		ch10.open()
		m11=ch10.getVoltageRatio()
		time.sleep(0.1)
		m12=ch10.getVoltageRatio()
		time.sleep(0.1)
		m13=ch10.getVoltageRatio()
		time.sleep(0.1)
		m14=ch10.getVoltageRatio()
		time.sleep(0.1)
		m15=ch10.getVoltageRatio()
		m1=(m11+m12+m13+m14+m15)/5
		ch11.open()
		m21=ch11.getVoltageRatio()
		time.sleep(0.1)
		m22=ch11.getVoltageRatio()
		time.sleep(0.1)
		m23=ch11.getVoltageRatio()
		time.sleep(0.1)
		m24=ch11.getVoltageRatio()
		time.sleep(0.1)
		m25=ch11.getVoltageRatio()
		m2=(m21+m22+m23+m24+m25)/5
		ch12.open()
		m31=ch12.getVoltageRatio()
		time.sleep(0.1)
		m32=ch12.getVoltageRatio()
		time.sleep(0.1)
		m33=ch12.getVoltageRatio()
		time.sleep(0.1)
		m34=ch12.getVoltageRatio()
		time.sleep(0.1)
		m35=ch12.getVoltageRatio()
		m3=(m31+m32+m33+m34+m35)/5
		ch13.open()
		m41=ch13.getVoltageRatio()
		time.sleep(0.1)
		m42=ch13.getVoltageRatio()
		time.sleep(0.1)
		m43=ch13.getVoltageRatio()
		time.sleep(0.1)
		m44=ch13.getVoltageRatio()
		time.sleep(0.1)
		m45=ch13.getVoltageRatio()
		m4=(m41+m42+m43+m44+m45)/5
		ch20.open()
		m51=ch20.getVoltageRatio()
		time.sleep(0.1)
		m52=ch20.getVoltageRatio()
		time.sleep(0.1)
		m53=ch20.getVoltageRatio()
		time.sleep(0.1)
		m54=ch20.getVoltageRatio()
		time.sleep(0.1)
		m55=ch20.getVoltageRatio()
		m5=(m51+m52+m53+m54+m55)/5
		ch21.open()
		m61=ch21.getVoltageRatio()
		time.sleep(0.1)
		m62=ch21.getVoltageRatio()
		time.sleep(0.1)
		m63=ch21.getVoltageRatio()
		time.sleep(0.1)
		m64=ch21.getVoltageRatio()
		time.sleep(0.1)
		m65=ch21.getVoltageRatio()
		m6=(m61+m62+m63+m64+m65)/5
		ch22.open()
		m71=ch22.getVoltageRatio()
		time.sleep(0.1)
		m72=ch22.getVoltageRatio()
		time.sleep(0.1)
		m73=ch22.getVoltageRatio()
		time.sleep(0.1)
		m74=ch22.getVoltageRatio()
		time.sleep(0.1)
		m75=ch22.getVoltageRatio()
		m7=(m71+m72+m73+m74+m75)/5
		file=open("/var/www/html/resultats/C_"+fichier,"a")
		f= csv.writer(file)
		f.writerow([t1, m1, m2, m3, m4, m5, m6,m7])
		file.close()
		print("temps= %.2f" %t1,  "mesure=",m1, ",", m2, ",", m3, ",", m4, ",", m5, ",", m6, ",", m7)
	if n==8:
		ch10.open()
		m11=ch10.getVoltageRatio()
		time.sleep(0.1)
		m12=ch10.getVoltageRatio()
		time.sleep(0.1)
		m13=ch10.getVoltageRatio()
		time.sleep(0.1)
		m14=ch10.getVoltageRatio()
		time.sleep(0.1)
		m15=ch10.getVoltageRatio()
		m1=(m11+m12+m13+m14+m15)/5
		ch11.open()
		m21=ch11.getVoltageRatio()
		time.sleep(0.1)
		m22=ch11.getVoltageRatio()
		time.sleep(0.1)
		m23=ch11.getVoltageRatio()
		time.sleep(0.1)
		m24=ch11.getVoltageRatio()
		time.sleep(0.1)
		m25=ch11.getVoltageRatio()
		m2=(m21+m22+m23+m24+m25)/5
		ch12.open()
		m31=ch12.getVoltageRatio()
		time.sleep(0.1)
		m32=ch12.getVoltageRatio()
		time.sleep(0.1)
		m33=ch12.getVoltageRatio()
		time.sleep(0.1)
		m34=ch12.getVoltageRatio()
		time.sleep(0.1)
		m35=ch12.getVoltageRatio()
		m3=(m31+m32+m33+m34+m35)/5
		ch13.open()
		m41=ch13.getVoltageRatio()
		time.sleep(0.1)
		m42=ch13.getVoltageRatio()
		time.sleep(0.1)
		m43=ch13.getVoltageRatio()
		time.sleep(0.1)
		m44=ch13.getVoltageRatio()
		time.sleep(0.1)
		m45=ch13.getVoltageRatio()
		m4=(m41+m42+m43+m44+m45)/5
		ch20.open()
		m51=ch20.getVoltageRatio()
		time.sleep(0.1)
		m52=ch20.getVoltageRatio()
		time.sleep(0.1)
		m53=ch20.getVoltageRatio()
		time.sleep(0.1)
		m54=ch20.getVoltageRatio()
		time.sleep(0.1)
		m55=ch20.getVoltageRatio()
		m5=(m51+m52+m53+m54+m55)/5
		ch21.open()
		m61=ch21.getVoltageRatio()
		time.sleep(0.1)
		m62=ch21.getVoltageRatio()
		time.sleep(0.1)
		m63=ch21.getVoltageRatio()
		time.sleep(0.1)
		m64=ch21.getVoltageRatio()
		time.sleep(0.1)
		m65=ch21.getVoltageRatio()
		m6=(m61+m62+m63+m64+m65)/5
		ch22.open()
		m71=ch22.getVoltageRatio()
		time.sleep(0.1)
		m72=ch22.getVoltageRatio()
		time.sleep(0.1)
		m73=ch22.getVoltageRatio()
		time.sleep(0.1)
		m74=ch22.getVoltageRatio()
		time.sleep(0.1)
		m75=ch22.getVoltageRatio()
		m7=(m71+m72+m73+m74+m75)/5
		ch23.open()
		m81=ch23.getVoltageRatio()
		time.sleep(0.1)
		m82=ch23.getVoltageRatio()
		time.sleep(0.1)
		m83=ch23.getVoltageRatio()
		time.sleep(0.1)
		m84=ch23.getVoltageRatio()
		time.sleep(0.1)
		m85=ch23.getVoltageRatio()
		m8=(m81+m82+m83+m84+m85)/5
		file=open("/var/www/html/resultats/C_"+fichier,"a")
		f= csv.writer(file)
		f.writerow([t1, m1, m2, m3, m4, m5, m6, m7, m8])
		file.close()
		print("temps= %.2f" %t1,  "mesure=",m1, ",", m2, ",", m3, ",", m4, ",", m5, ",", m6, ",", m7, ",", m8)