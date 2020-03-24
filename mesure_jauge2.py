import sys
import time 
import csv
#bibliotheque pour utiliser la carte 1046 de phidget
from Phidget22.Devices.VoltageRatioInput import *
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *
#programme pour initialiser les cartes d'acquisition
import init_carte

#nom fichier avec la date et l'heure en csv
fichier=time.strftime("%Y%m%d_%H%M%S"+".csv")
t0=time.time()-time.time()


init_carte.init()
print("OK")
#lecture de 8 voies
init_carte.lecture(fichier,8,t0)


