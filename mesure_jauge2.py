import sys
import time 
import csv
from Phidget22.Devices.VoltageRatioInput import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *
import init_carte

fichier=time.strftime("%Y%m%d_%H%M%S"+".csv")
t0=time.time()-time.time()


init_carte.init()
print("OK")
init_carte.lecture(fichier,8,t0)


