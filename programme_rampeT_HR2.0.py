# -*-coding:Utf-8 -*
import time 
import csv
import serial
import consigne
import consigneHR
import init_carte

fichier=time.strftime("%Y%m%d_%H%M%S"+".csv")
z=input("Rentrer le nom de l'espece:") #demande Ã  l'utilisateur en quelle valeur faire la moyenne des conductances
fichier=z+"_"+fichier
fichier2=fichier
file=open("/var/www/html/resultats/C_"+fichier,"w")
file2=open("/var/www/html/resultats/C_temp_"+fichier,"w")
file.close()
file2.close()
rampe = open("rampeT_HR.txt","r") #ouvert le fichier rampe
reader = rampe.read() #lit le fichier en .txt
list_Temp=list()
list_temps=list()
list_HR=list()
reader=reader.split(",")
rampe.close()
n=len(reader)
n1=n/3
n2=n
print(n1)

while n1>0:
    a=n-n2
    b=n-n2+1
    t=reader[a:b]
    t=str(t)
    t=t[2:-2]
    t=int(t)
    T=reader[a+1:b+1]
    T=str(T)
    T=T[2:-2]
    T=int(T)
    HR=reader[a+2:b+2]
    HR=str(HR)
    HR=HR[2:-2]
    HR=int(HR)    
    n1=n1-1
    n2=n2-3
    list_Temp.append(T)
    list_temps.append(t)
    list_HR.append(HR)

print(list_temps, list_Temp, list_HR)
nbj=-1
ta=-1

while nbj<0 :
    nbj=input("Combien de jauges sont utilisés:")
    try:
        nbj=int(nbj)
    except ValueError:
        print("vous n'avez pas saisi de nombre")
        nbj=-1
        continue

    if nbj<=0:
        print("le nombre est negatif ou egal a zero")
        nbj=-1
    if nbj>8:
        print("le nombre max de jauges est 8")
        nbj=-1

while ta<0 :
    ta=input("Quel temps d'acquisition voulez-vous (en seconde) ?")
    try:
        ta=int(ta)
    except ValueError:
        print("vous n'avez pas saisi de nombre")
        ta=-1
        continue

    if ta<=0:
        print("le nombre est negatif ou egal a zero")
        ta=-1
   

t0=time.time()

if n/3==1:
    temps=list_temps[0:1]
    Temp=list_Temp[0:1]
    HR=list_HR[0:1]
    temps=str(temps)
    temps=temps[1:-1]
    temps=int(temps)
    temps=temps*60    
    Temp=str(Temp)
    Temp=Temp[1:-1]
    Temp=int(Temp)
    HR=str(HR)
    HR=HR[1:-1]
    HR=int(HR)
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp, ser)   
    consigneHR.envoi_consigne(HR, ser)   
    init_carte.init()
    t1=time.time()
    t=t1-t0
    while t<temps:
        print(temps,Temp,HR)
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps)

if n/3==2:
    temps1=list_temps[0:1]
    temps2=list_temps[1:2]
    Temp1=list_Temp[0:1]
    Temp2=list_Temp[1:2]
    HR1=list_HR[0:1]
    HR2=list_HR[1:2]
    temps1=str(temps1)
    temps1=temps1[1:-1]
    temps1=int(temps1)
    temps1=temps1*60   
    temps2=str(temps2)
    temps2=temps2[1:-1]
    temps2=int(temps2)
    temps2=temps2*60   
    Temp1=str(Temp1)
    Temp1=Temp1[1:-1]
    Temp1=int(Temp1)
    Temp2=str(Temp2)
    Temp2=Temp2[1:-1]
    Temp2=int(Temp2)    
    HR1=str(HR1)
    HR1=HR1[1:-1]
    HR1=int(HR1)
    HR2=str(HR2)
    HR2=HR2[1:-1]
    HR2=int(HR2)    
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp1, ser)   
    consigneHR.envoi_consigne(HR1, ser) 
    init_carte.init()
    print("Temp=",Temp1)
    print("HR=",HR1)
    t1=time.time()
    t=t1-t0
   
    while t<temps1:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1)    
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp2, ser)   
    consigneHR.envoi_consigne(HR2, ser)   
    print("Temp=",Temp2)
    print("HR=",HR2)
    while t<(temps1+temps2):
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, (temps1+temps2) )       



if n/3==3:
    temps1=list_temps[0:1]
    temps2=list_temps[1:2]
    temps3=list_temps[2:3]
    Temp1=list_Temp[0:1]
    Temp2=list_Temp[1:2]
    Temp3=list_Temp[2:3]
    HR1=list_HR[0:1]
    HR2=list_HR[1:2]
    HR3=list_HR[2:3]
    temps1=str(temps1)
    temps1=temps1[1:-1]
    temps1=int(temps1)
    temps1=temps1*60   
    temps2=str(temps2)
    temps2=temps2[1:-1]
    temps2=int(temps2)
    temps2=temps2*60   
    temps3=str(temps3)
    temps3=temps3[1:-1]
    temps3=int(temps3)
    temps3=temps3*60        
    Temp1=str(Temp1)
    Temp1=Temp1[1:-1]
    Temp1=int(Temp1)
    Temp2=str(Temp2)
    Temp2=Temp2[1:-1]
    Temp2=int(Temp2)    
    Temp3=str(Temp3)
    Temp3=Temp3[1:-1]
    Temp3=int(Temp3)        
    HR1=str(HR1)
    HR1=HR1[1:-1]
    HR1=int(HR1)
    HR2=str(HR2)
    HR2=HR2[1:-1]
    HR2=int(HR2)    
    HR3=str(HR3)
    HR3=HR3[1:-1]
    HR3=int(HR3)        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp1, ser)   
    consigneHR.envoi_consigne(HR1, ser) 
    init_carte.init()
    print("Temp=",Temp1)
    print("HR=",HR1)
    t1=time.time()
    t=t1-t0
 
    while t<temps1:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1)    
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp2, ser)   
    consigneHR.envoi_consigne(HR2, ser)   
    print("Temp=",Temp2)
    print("HR=",HR2)
    while t<(temps1+temps2):
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, (temps1+temps2) )         
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp3, ser)   
    consigneHR.envoi_consigne(HR3, ser) 
    print("Temp=",Temp3)
    print("HR=",HR3)
    t1=time.time()
    t=t1-t0

    while t<temps1+temps2+temps3:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3)   

if n/3==4:
    temps1=list_temps[0:1]
    temps2=list_temps[1:2]
    temps3=list_temps[2:3]
    temps4=list_temps[3:4]
    Temp1=list_Temp[0:1]
    Temp2=list_Temp[1:2]
    Temp3=list_Temp[2:3]
    Temp4=list_Temp[3:4]
    HR1=list_HR[0:1]
    HR2=list_HR[1:2]
    HR3=list_HR[2:3]
    HR4=list_HR[3:4]
    temps1=str(temps1)
    temps1=temps1[1:-1]
    temps1=int(temps1)
    temps1=temps1*60   
    temps2=str(temps2)
    temps2=temps2[1:-1]
    temps2=int(temps2)
    temps2=temps2*60   
    temps3=str(temps3)
    temps3=temps3[1:-1]
    temps3=int(temps3)
    temps3=temps3*60   
    temps4=str(temps4)
    temps4=temps4[1:-1]
    temps4=int(temps4)
    temps4=temps4*60       
    Temp1=str(Temp1)
    Temp1=Temp1[1:-1]
    Temp1=int(Temp1)
    Temp2=str(Temp2)
    Temp2=Temp2[1:-1]
    Temp2=int(Temp2)    
    Temp3=str(Temp3)
    Temp3=Temp3[1:-1]
    Temp3=int(Temp3)    
    Temp4=str(Temp4)
    Temp4=Temp4[1:-1]
    Temp4=int(Temp4)    
    HR1=str(HR1)
    HR1=HR1[1:-1]
    HR1=int(HR1)
    HR2=str(HR2)
    HR2=HR2[1:-1]
    HR2=int(HR2)    
    HR3=str(HR3)
    HR3=HR3[1:-1]
    HR3=int(HR3)    
    HR4=str(HR4)
    HR4=HR4[1:-1]
    HR4=int(HR4)      
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp1, ser)   
    consigneHR.envoi_consigne(HR1, ser) 
    init_carte.init()
    print("Temp=",Temp1)
    print("HR=",HR1)
    t1=time.time()
    t=t1-t0

    while t<temps1:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1)    
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp2, ser)   
    consigneHR.envoi_consigne(HR2, ser)   
    print("Temp=",Temp2)
    print("HR=",HR2)
    while t<(temps1+temps2):
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, (temps1+temps2) )         
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp3, ser)   
    consigneHR.envoi_consigne(HR3, ser) 
    print("Temp=",Temp3)
    print("HR=",HR3)
    t1=time.time()
    t=t1-t0
 
    while t<temps1+temps2+temps3:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3)   
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp4, ser)   
    consigneHR.envoi_consigne(HR4, ser) 
    print("Temp=",Temp4)
    print("HR=",HR4)
    t1=time.time()
    t=t1-t0
 
    while t<temps1+temps2+temps3+temps4:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4)       

if n/3==5:
    temps1=list_temps[0:1]
    temps2=list_temps[1:2]
    temps3=list_temps[2:3]
    temps4=list_temps[3:4]
    temps5=list_temps[4:5]
    Temp1=list_Temp[0:1]
    Temp2=list_Temp[1:2]
    Temp3=list_Temp[2:3]
    Temp4=list_Temp[3:4]
    Temp5=list_Temp[4:5]
    HR1=list_HR[0:1]
    HR2=list_HR[1:2]
    HR3=list_HR[2:3]
    HR4=list_HR[3:4]
    HR5=list_HR[4:5]
    temps1=str(temps1)
    temps1=temps1[1:-1]
    temps1=int(temps1)
    temps1=temps1*60   
    temps2=str(temps2)
    temps2=temps2[1:-1]
    temps2=int(temps2)
    temps2=temps2*60   
    temps3=str(temps3)
    temps3=temps3[1:-1]
    temps3=int(temps3)
    temps3=temps3*60   
    temps4=str(temps4)
    temps4=temps4[1:-1]
    temps4=int(temps4)
    temps4=temps4*60      
    temps5=str(temps5)
    temps5=temps5[1:-1]
    temps5=int(temps5)
    temps5=temps5*60      
    Temp1=str(Temp1)
    Temp1=Temp1[1:-1]
    Temp1=int(Temp1)
    Temp2=str(Temp2)
    Temp2=Temp2[1:-1]
    Temp2=int(Temp2)    
    Temp3=str(Temp3)
    Temp3=Temp3[1:-1]
    Temp3=int(Temp3)    
    Temp4=str(Temp4)
    Temp4=Temp4[1:-1]
    Temp4=int(Temp4)  
    Temp5=str(Temp5)
    Temp5=Temp5[1:-1]
    Temp5=int(Temp5)        
    HR1=str(HR1)
    HR1=HR1[1:-1]
    HR1=int(HR1)
    HR2=str(HR2)
    HR2=HR2[1:-1]
    HR2=int(HR2)    
    HR3=str(HR3)
    HR3=HR3[1:-1]
    HR3=int(HR3)    
    HR4=str(HR4)
    HR4=HR4[1:-1]
    HR4=int(HR4)   
    HR5=str(HR5)
    HR5=HR5[1:-1]
    HR5=int(HR5)      
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp1, ser)   
    consigneHR.envoi_consigne(HR1, ser) 
    init_carte.init()
    print("Temp=",Temp1)
    print("HR=",HR1)
    t1=time.time()
    t=t1-t0
 
    while t<temps1:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1)    
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp2, ser)   
    consigneHR.envoi_consigne(HR2, ser)   
    print("Temp=",Temp2)
    print("HR=",HR2)
    while t<(temps1+temps2):
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, (temps1+temps2) )         
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp3, ser)   
    consigneHR.envoi_consigne(HR3, ser) 
    print("Temp=",Temp3)
    print("HR=",HR3)
    t1=time.time()
    t=t1-t0
 
    while t<temps1+temps2+temps3:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3)   
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp4, ser)   
    consigneHR.envoi_consigne(HR4, ser) 
    print("Temp=",Temp4)
    print("HR=",HR4)
    t1=time.time()
    t=t1-t0

    while t<temps1+temps2+temps3+temps4:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4)    
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp5, ser)   
    consigneHR.envoi_consigne(HR5, ser) 
    print("Temp=",Temp5)
    print("HR=",HR5)
    t1=time.time()
    t=t1-t0

    while t<temps1+temps2+temps3+temps4+temps5:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5)    
    
if n/3==6:
    temps1=list_temps[0:1]
    temps2=list_temps[1:2]
    temps3=list_temps[2:3]
    temps4=list_temps[3:4]
    temps5=list_temps[4:5]
    temps6=list_temps[5:6]
    Temp1=list_Temp[0:1]
    Temp2=list_Temp[1:2]
    Temp3=list_Temp[2:3]
    Temp4=list_Temp[3:4]
    Temp5=list_Temp[4:5]
    Temp6=list_Temp[5:6]
    HR1=list_HR[0:1]
    HR2=list_HR[1:2]
    HR3=list_HR[2:3]
    HR4=list_HR[3:4]
    HR5=list_HR[4:5]
    HR6=list_HR[5:6]
    temps1=str(temps1)
    temps1=temps1[1:-1]
    temps1=int(temps1)
    temps1=temps1*60   
    temps2=str(temps2)
    temps2=temps2[1:-1]
    temps2=int(temps2)
    temps2=temps2*60   
    temps3=str(temps3)
    temps3=temps3[1:-1]
    temps3=int(temps3)
    temps3=temps3*60   
    temps4=str(temps4)
    temps4=temps4[1:-1]
    temps4=int(temps4)
    temps4=temps4*60      
    temps5=str(temps5)
    temps5=temps5[1:-1]
    temps5=int(temps5)
    temps5=temps5*60      
    temps6=str(temps6)
    temps6=temps6[1:-1]
    temps6=int(temps6)
    temps6=temps6*60          
    Temp1=str(Temp1)
    Temp1=Temp1[1:-1]
    Temp1=int(Temp1)
    Temp2=str(Temp2)
    Temp2=Temp2[1:-1]
    Temp2=int(Temp2)    
    Temp3=str(Temp3)
    Temp3=Temp3[1:-1]
    Temp3=int(Temp3)    
    Temp4=str(Temp4)
    Temp4=Temp4[1:-1]
    Temp4=int(Temp4)  
    Temp5=str(Temp5)
    Temp5=Temp5[1:-1]
    Temp5=int(Temp5)    
    Temp6=str(Temp6)
    Temp6=Temp6[1:-1]
    Temp6=int(Temp6)         
    HR1=str(HR1)
    HR1=HR1[1:-1]
    HR1=int(HR1)
    HR2=str(HR2)
    HR2=HR2[1:-1]
    HR2=int(HR2)    
    HR3=str(HR3)
    HR3=HR3[1:-1]
    HR3=int(HR3)    
    HR4=str(HR4)
    HR4=HR4[1:-1]
    HR4=int(HR4)   
    HR5=str(HR5)
    HR5=HR5[1:-1]
    HR5=int(HR5)     
    HR6=str(HR6)
    HR6=HR6[1:-1]
    HR6=int(HR6)     
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp1, ser)   
    consigneHR.envoi_consigne(HR1, ser) 
    init_carte.init()
    print("Temp=",Temp1)
    print("HR=",HR1)
    t1=time.time()
    t=t1-t0
  
    while t<temps1:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1)    
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp2, ser)   
    consigneHR.envoi_consigne(HR2, ser)   
    print("Temp=",Temp2)
    print("HR=",HR2)
    while t<(temps1+temps2):
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, (temps1+temps2) )         
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp3, ser)   
    consigneHR.envoi_consigne(HR3, ser) 
    print("Temp=",Temp3)
    print("HR=",HR3)
    t1=time.time()
    t=t1-t0
  
    while t<temps1+temps2+temps3:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3)   
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp4, ser)   
    consigneHR.envoi_consigne(HR4, ser) 
    print("Temp=",Temp4)
    print("HR=",HR4)
    t1=time.time()
    t=t1-t0
 
    while t<temps1+temps2+temps3+temps4:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4)    
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp5, ser)   
    consigneHR.envoi_consigne(HR5, ser) 
    print("Temp=",Temp5)
    print("HR=",HR5)
    t1=time.time()
    t=t1-t0
  
    while t<temps1+temps2+temps3+temps4+temps5:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5)   

    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp6, ser)   
    consigneHR.envoi_consigne(HR6, ser) 
    print("Temp=",Temp6)
    print("HR=",HR6)
    t1=time.time()
    t=t1-t0
  
    while t<temps1+temps2+temps3+temps4+temps5+temps6:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6)   
if n/3==7:
    temps1=list_temps[0:1]
    temps2=list_temps[1:2]
    temps3=list_temps[2:3]
    temps4=list_temps[3:4]
    temps5=list_temps[4:5]
    temps6=list_temps[5:6]
    temps7=list_temps[6:7]
    Temp1=list_Temp[0:1]
    Temp2=list_Temp[1:2]
    Temp3=list_Temp[2:3]
    Temp4=list_Temp[3:4]
    Temp5=list_Temp[4:5]
    Temp6=list_Temp[5:6]
    Temp7=list_Temp[6:7]
    HR1=list_HR[0:1]
    HR2=list_HR[1:2]
    HR3=list_HR[2:3]
    HR4=list_HR[3:4]
    HR5=list_HR[4:5]
    HR6=list_HR[5:6]
    HR7=list_HR[6:7]
    temps1=str(temps1)
    temps1=temps1[1:-1]
    temps1=int(temps1)
    temps1=temps1*60   
    temps2=str(temps2)
    temps2=temps2[1:-1]
    temps2=int(temps2)
    temps2=temps2*60   
    temps3=str(temps3)
    temps3=temps3[1:-1]
    temps3=int(temps3)
    temps3=temps3*60   
    temps4=str(temps4)
    temps4=temps4[1:-1]
    temps4=int(temps4)
    temps4=temps4*60      
    temps5=str(temps5)
    temps5=temps5[1:-1]
    temps5=int(temps5)
    temps5=temps5*60      
    temps6=str(temps6)
    temps6=temps6[1:-1]
    temps6=int(temps6)
    temps6=temps6*60     
    temps7=str(temps7)
    temps7=temps7[1:-1]
    temps7=int(temps7)
    temps7=temps7*60         
    Temp1=str(Temp1)
    Temp1=Temp1[1:-1]
    Temp1=int(Temp1)
    Temp2=str(Temp2)
    Temp2=Temp2[1:-1]
    Temp2=int(Temp2)    
    Temp3=str(Temp3)
    Temp3=Temp3[1:-1]
    Temp3=int(Temp3)    
    Temp4=str(Temp4)
    Temp4=Temp4[1:-1]
    Temp4=int(Temp4)  
    Temp5=str(Temp5)
    Temp5=Temp5[1:-1]
    Temp5=int(Temp5)    
    Temp6=str(Temp6)
    Temp6=Temp6[1:-1]
    Temp6=int(Temp6)
    Temp7=str(Temp7)
    Temp7=Temp7[1:-1]
    Temp7=int(Temp7)       
    HR1=str(HR1)
    HR1=HR1[1:-1]
    HR1=int(HR1)
    HR2=str(HR2)
    HR2=HR2[1:-1]
    HR2=int(HR2)    
    HR3=str(HR3)
    HR3=HR3[1:-1]
    HR3=int(HR3)    
    HR4=str(HR4)
    HR4=HR4[1:-1]
    HR4=int(HR4)   
    HR5=str(HR5)
    HR5=HR5[1:-1]
    HR5=int(HR5)     
    HR6=str(HR6)
    HR6=HR6[1:-1]
    HR6=int(HR6)    
    HR7=str(HR7)
    HR7=HR7[1:-1]
    HR7=int(HR7)        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp1, ser)   
    consigneHR.envoi_consigne(HR1, ser) 
    init_carte.init()
    print("Temp=",Temp1)
    print("HR=",HR1)
    t1=time.time()
    t=t1-t0
  
    while t<temps1:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1)    
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp2, ser)   
    consigneHR.envoi_consigne(HR2, ser)   
    print("Temp=",Temp2)
    print("HR=",HR2)
    while t<(temps1+temps2):
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, (temps1+temps2) )         
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp3, ser)   
    consigneHR.envoi_consigne(HR3, ser) 
    print("Temp=",Temp3)
    print("HR=",HR3)
    t1=time.time()
    t=t1-t0
 
    while t<temps1+temps2+temps3:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3)   
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp4, ser)   
    consigneHR.envoi_consigne(HR4, ser) 
    print("Temp=",Temp4)
    print("HR=",HR4)
    t1=time.time()
    t=t1-t0
 
    while t<temps1+temps2+temps3+temps4:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4)    
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp5, ser)   
    consigneHR.envoi_consigne(HR5, ser) 
    print("Temp=",Temp5)
    print("HR=",HR5)
    t1=time.time()
    t=t1-t0

    while t<temps1+temps2+temps3+temps4+temps5:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5)   

    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp6, ser)   
    consigneHR.envoi_consigne(HR6, ser) 
    print("Temp=",Temp6)
    print("HR=",HR6)
    t1=time.time()
    t=t1-t0
  
    while t<temps1+temps2+temps3+temps4+temps5+temps6:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6)  
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp7, ser)   
    consigneHR.envoi_consigne(HR7, ser) 
    print("Temp=",Temp7)
    print("HR=",HR7)
    t1=time.time()
    t=t1-t0
  
    while t<temps1+temps2+temps3+temps4+temps5+temps6+temps7:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6+temps7)     
if n/3==8:
    temps1=list_temps[0:1]
    temps2=list_temps[1:2]
    temps3=list_temps[2:3]
    temps4=list_temps[3:4]
    temps5=list_temps[4:5]
    temps6=list_temps[5:6]
    temps7=list_temps[6:7]
    temps8=list_temps[7:8]
    Temp1=list_Temp[0:1]
    Temp2=list_Temp[1:2]
    Temp3=list_Temp[2:3]
    Temp4=list_Temp[3:4]
    Temp5=list_Temp[4:5]
    Temp6=list_Temp[5:6]
    Temp7=list_Temp[6:7]
    Temp8=list_Temp[7:8]
    HR1=list_HR[0:1]
    HR2=list_HR[1:2]
    HR3=list_HR[2:3]
    HR4=list_HR[3:4]
    HR5=list_HR[4:5]
    HR6=list_HR[5:6]
    HR7=list_HR[6:7]
    HR8=list_HR[7:8]
    temps1=str(temps1)
    temps1=temps1[1:-1]
    temps1=int(temps1)
    temps1=temps1*60   
    temps2=str(temps2)
    temps2=temps2[1:-1]
    temps2=int(temps2)
    temps2=temps2*60   
    temps3=str(temps3)
    temps3=temps3[1:-1]
    temps3=int(temps3)
    temps3=temps3*60   
    temps4=str(temps4)
    temps4=temps4[1:-1]
    temps4=int(temps4)
    temps4=temps4*60      
    temps5=str(temps5)
    temps5=temps5[1:-1]
    temps5=int(temps5)
    temps5=temps5*60      
    temps6=str(temps6)
    temps6=temps6[1:-1]
    temps6=int(temps6)
    temps6=temps6*60     
    temps7=str(temps7)
    temps7=temps7[1:-1]
    temps7=int(temps7)
    temps7=temps7*60       
    temps8=str(temps8)
    temps8=temps8[1:-1]
    temps8=int(temps8)
    temps8=temps8*60       
    Temp1=str(Temp1)
    Temp1=Temp1[1:-1]
    Temp1=int(Temp1)
    Temp2=str(Temp2)
    Temp2=Temp2[1:-1]
    Temp2=int(Temp2)    
    Temp3=str(Temp3)
    Temp3=Temp3[1:-1]
    Temp3=int(Temp3)    
    Temp4=str(Temp4)
    Temp4=Temp4[1:-1]
    Temp4=int(Temp4)  
    Temp5=str(Temp5)
    Temp5=Temp5[1:-1]
    Temp5=int(Temp5)    
    Temp6=str(Temp6)
    Temp6=Temp6[1:-1]
    Temp6=int(Temp6)
    Temp7=str(Temp7)
    Temp7=Temp7[1:-1]
    Temp7=int(Temp7)       
    Temp8=str(Temp8)
    Temp8=Temp8[1:-1]
    Temp8=int(Temp8)        
    HR1=str(HR1)
    HR1=HR1[1:-1]
    HR1=int(HR1)
    HR2=str(HR2)
    HR2=HR2[1:-1]
    HR2=int(HR2)    
    HR3=str(HR3)
    HR3=HR3[1:-1]
    HR3=int(HR3)    
    HR4=str(HR4)
    HR4=HR4[1:-1]
    HR4=int(HR4)   
    HR5=str(HR5)
    HR5=HR5[1:-1]
    HR5=int(HR5)     
    HR6=str(HR6)
    HR6=HR6[1:-1]
    HR6=int(HR6)    
    HR7=str(HR7)
    HR7=HR7[1:-1]
    HR7=int(HR7)     
    HR8=str(HR8)
    HR8=HR8[1:-1]
    HR8=int(HR8)      
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp1, ser)   
    consigneHR.envoi_consigne(HR1, ser) 
    init_carte.init()
    print("Temp=",Temp1)
    print("HR=",HR1)
    t1=time.time()
    t=t1-t0
  
    while t<temps1:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1)    
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp2, ser)   
    consigneHR.envoi_consigne(HR2, ser)   
    print("Temp=",Temp2)
    print("HR=",HR2)
    while t<(temps1+temps2):
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, (temps1+temps2) )         
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp3, ser)   
    consigneHR.envoi_consigne(HR3, ser) 
    print("Temp=",Temp3)
    print("HR=",HR3)
    t1=time.time()
    t=t1-t0
 
    while t<temps1+temps2+temps3:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3)   
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp4, ser)   
    consigneHR.envoi_consigne(HR4, ser) 
    print("Temp=",Temp4)
    print("HR=",HR4)
    t1=time.time()
    t=t1-t0
 
    while t<temps1+temps2+temps3+temps4:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4)    
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp5, ser)   
    consigneHR.envoi_consigne(HR5, ser) 
    print("Temp=",Temp5)
    print("HR=",HR5)
    t1=time.time()
    t=t1-t0

    while t<temps1+temps2+temps3+temps4+temps5:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5)   

    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp6, ser)   
    consigneHR.envoi_consigne(HR6, ser) 
    print("Temp=",Temp6)
    print("HR=",HR6)
    t1=time.time()
    t=t1-t0
  
    while t<temps1+temps2+temps3+temps4+temps5+temps6:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6)  
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp7, ser)   
    consigneHR.envoi_consigne(HR7, ser) 
    print("Temp=",Temp7)
    print("HR=",HR7)
    t1=time.time()
    t=t1-t0
  
    while t<temps1+temps2+temps3+temps4+temps5+temps6+temps7:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6+temps7)
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp8, ser)   
    consigneHR.envoi_consigne(HR8, ser) 
    print("Temp=",Temp8)
    print("HR=",HR8)
    t1=time.time()
    t=t1-t0
  
    while t<temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8)         
    
if n/3==9:
    temps1=list_temps[0:1]
    temps2=list_temps[1:2]
    temps3=list_temps[2:3]
    temps4=list_temps[3:4]
    temps5=list_temps[4:5]
    temps6=list_temps[5:6]
    temps7=list_temps[6:7]
    temps8=list_temps[7:8]
    temps9=list_temps[8:9]
    Temp1=list_Temp[0:1]
    Temp2=list_Temp[1:2]
    Temp3=list_Temp[2:3]
    Temp4=list_Temp[3:4]
    Temp5=list_Temp[4:5]
    Temp6=list_Temp[5:6]
    Temp7=list_Temp[6:7]
    Temp8=list_Temp[7:8]
    Temp9=list_Temp[8:9]
    HR1=list_HR[0:1]
    HR2=list_HR[1:2]
    HR3=list_HR[2:3]
    HR4=list_HR[3:4]
    HR5=list_HR[4:5]
    HR6=list_HR[5:6]
    HR7=list_HR[6:7]
    HR8=list_HR[7:8]
    HR9=list_HR[8:9]
    temps1=str(temps1)
    temps1=temps1[1:-1]
    temps1=int(temps1)
    temps1=temps1*60   
    temps2=str(temps2)
    temps2=temps2[1:-1]
    temps2=int(temps2)
    temps2=temps2*60   
    temps3=str(temps3)
    temps3=temps3[1:-1]
    temps3=int(temps3)
    temps3=temps3*60   
    temps4=str(temps4)
    temps4=temps4[1:-1]
    temps4=int(temps4)
    temps4=temps4*60      
    temps5=str(temps5)
    temps5=temps5[1:-1]
    temps5=int(temps5)
    temps5=temps5*60      
    temps6=str(temps6)
    temps6=temps6[1:-1]
    temps6=int(temps6)
    temps6=temps6*60     
    temps7=str(temps7)
    temps7=temps7[1:-1]
    temps7=int(temps7)
    temps7=temps7*60       
    temps8=str(temps8)
    temps8=temps8[1:-1]
    temps8=int(temps8)
    temps8=temps8*60       
    temps9=str(temps9)
    temps9=temps9[1:-1]
    temps9=int(temps9)
    temps9=temps9*60        
    Temp1=str(Temp1)
    Temp1=Temp1[1:-1]
    Temp1=int(Temp1)
    Temp2=str(Temp2)
    Temp2=Temp2[1:-1]
    Temp2=int(Temp2)    
    Temp3=str(Temp3)
    Temp3=Temp3[1:-1]
    Temp3=int(Temp3)    
    Temp4=str(Temp4)
    Temp4=Temp4[1:-1]
    Temp4=int(Temp4)  
    Temp5=str(Temp5)
    Temp5=Temp5[1:-1]
    Temp5=int(Temp5)    
    Temp6=str(Temp6)
    Temp6=Temp6[1:-1]
    Temp6=int(Temp6)
    Temp7=str(Temp7)
    Temp7=Temp7[1:-1]
    Temp7=int(Temp7)       
    Temp8=str(Temp8)
    Temp8=Temp8[1:-1]
    Temp8=int(Temp8)        
    Temp9=str(Temp9)
    Temp9=Temp9[1:-1]
    Temp9=int(Temp9)       
    HR1=str(HR1)
    HR1=HR1[1:-1]
    HR1=int(HR1)
    HR2=str(HR2)
    HR2=HR2[1:-1]
    HR2=int(HR2)    
    HR3=str(HR3)
    HR3=HR3[1:-1]
    HR3=int(HR3)    
    HR4=str(HR4)
    HR4=HR4[1:-1]
    HR4=int(HR4)   
    HR5=str(HR5)
    HR5=HR5[1:-1]
    HR5=int(HR5)     
    HR6=str(HR6)
    HR6=HR6[1:-1]
    HR6=int(HR6)    
    HR7=str(HR7)
    HR7=HR7[1:-1]
    HR7=int(HR7)     
    HR8=str(HR8)
    HR8=HR8[1:-1]
    HR8=int(HR8)   
    HR9=str(HR9)
    HR9=HR9[1:-1]
    HR9=int(HR9)       
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp1, ser)   
    consigneHR.envoi_consigne(HR1, ser) 
    init_carte.init()
    print("Temp=",Temp1)
    print("HR=",HR1)
    t1=time.time()
    t=t1-t0
  
    while t<temps1:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1)    
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp2, ser)   
    consigneHR.envoi_consigne(HR2, ser)   
    print("Temp=",Temp2)
    print("HR=",HR2)
    while t<(temps1+temps2):
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, (temps1+temps2) )         
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp3, ser)   
    consigneHR.envoi_consigne(HR3, ser) 
    print("Temp=",Temp3)
    print("HR=",HR3)
    t1=time.time()
    t=t1-t0
 
    while t<temps1+temps2+temps3:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3)   
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp4, ser)   
    consigneHR.envoi_consigne(HR4, ser) 
    print("Temp=",Temp4)
    print("HR=",HR4)
    t1=time.time()
    t=t1-t0
 
    while t<temps1+temps2+temps3+temps4:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4)    
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp5, ser)   
    consigneHR.envoi_consigne(HR5, ser) 
    print("Temp=",Temp5)
    print("HR=",HR5)
    t1=time.time()
    t=t1-t0

    while t<temps1+temps2+temps3+temps4+temps5:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5)   

    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp6, ser)   
    consigneHR.envoi_consigne(HR6, ser) 
    print("Temp=",Temp6)
    print("HR=",HR6)
    t1=time.time()
    t=t1-t0
  
    while t<temps1+temps2+temps3+temps4+temps5+temps6:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6)  
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp7, ser)   
    consigneHR.envoi_consigne(HR7, ser) 
    print("Temp=",Temp7)
    print("HR=",HR7)
    t1=time.time()
    t=t1-t0
  
    while t<temps1+temps2+temps3+temps4+temps5+temps6+temps7:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6+temps7)
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp8, ser)   
    consigneHR.envoi_consigne(HR8, ser) 
    print("Temp=",Temp8)
    print("HR=",HR8)
    t1=time.time()
    t=t1-t0
  
    while t<temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8)     
    
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp9, ser)   
    consigneHR.envoi_consigne(HR9, ser) 
    print("Temp=",Temp9)
    print("HR=",HR9)
    t1=time.time()
    t=t1-t0

    while t<temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8+temps9:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8+temps9)     
        
if n/3==10:
    temps1=list_temps[0:1]
    temps2=list_temps[1:2]
    temps3=list_temps[2:3]
    temps4=list_temps[3:4]
    temps5=list_temps[4:5]
    temps6=list_temps[5:6]
    temps7=list_temps[6:7]
    temps8=list_temps[7:8]
    temps9=list_temps[8:9]
    temps10=list_temps[9:10]
    Temp1=list_Temp[0:1]
    Temp2=list_Temp[1:2]
    Temp3=list_Temp[2:3]
    Temp4=list_Temp[3:4]
    Temp5=list_Temp[4:5]
    Temp6=list_Temp[5:6]
    Temp7=list_Temp[6:7]
    Temp8=list_Temp[7:8]
    Temp9=list_Temp[8:9]
    Temp10=list_Temp[9:10]
    HR1=list_HR[0:1]
    HR2=list_HR[1:2]
    HR3=list_HR[2:3]
    HR4=list_HR[3:4]
    HR5=list_HR[4:5]
    HR6=list_HR[5:6]
    HR7=list_HR[6:7]
    HR8=list_HR[7:8]
    HR9=list_HR[8:9]
    HR10=list_HR[9:10]
    temps1=str(temps1)
    temps1=temps1[1:-1]
    temps1=int(temps1)
    temps1=temps1*60   
    temps2=str(temps2)
    temps2=temps2[1:-1]
    temps2=int(temps2)
    temps2=temps2*60   
    temps3=str(temps3)
    temps3=temps3[1:-1]
    temps3=int(temps3)
    temps3=temps3*60   
    temps4=str(temps4)
    temps4=temps4[1:-1]
    temps4=int(temps4)
    temps4=temps4*60      
    temps5=str(temps5)
    temps5=temps5[1:-1]
    temps5=int(temps5)
    temps5=temps5*60      
    temps6=str(temps6)
    temps6=temps6[1:-1]
    temps6=int(temps6)
    temps6=temps6*60     
    temps7=str(temps7)
    temps7=temps7[1:-1]
    temps7=int(temps7)
    temps7=temps7*60       
    temps8=str(temps8)
    temps8=temps8[1:-1]
    temps8=int(temps8)
    temps8=temps8*60       
    temps9=str(temps9)
    temps9=temps9[1:-1]
    temps9=int(temps9)
    temps9=temps9*60        
    temps10=str(temps10)
    temps10=temps10[1:-1]
    temps10=int(temps10)
    temps10=temps10*60         
    Temp1=str(Temp1)
    Temp1=Temp1[1:-1]
    Temp1=int(Temp1)
    Temp2=str(Temp2)
    Temp2=Temp2[1:-1]
    Temp2=int(Temp2)    
    Temp3=str(Temp3)
    Temp3=Temp3[1:-1]
    Temp3=int(Temp3)    
    Temp4=str(Temp4)
    Temp4=Temp4[1:-1]
    Temp4=int(Temp4)  
    Temp5=str(Temp5)
    Temp5=Temp5[1:-1]
    Temp5=int(Temp5)    
    Temp6=str(Temp6)
    Temp6=Temp6[1:-1]
    Temp6=int(Temp6)
    Temp7=str(Temp7)
    Temp7=Temp7[1:-1]
    Temp7=int(Temp7)       
    Temp8=str(Temp8)
    Temp8=Temp8[1:-1]
    Temp8=int(Temp8)        
    Temp9=str(Temp9)
    Temp9=Temp9[1:-1]
    Temp9=int(Temp9)       
    Temp10=str(Temp10)
    Temp10=Temp10[1:-1]
    Temp10=int(Temp10)     
    HR1=str(HR1)
    HR1=HR1[1:-1]
    HR1=int(HR1)
    HR2=str(HR2)
    HR2=HR2[1:-1]
    HR2=int(HR2)    
    HR3=str(HR3)
    HR3=HR3[1:-1]
    HR3=int(HR3)    
    HR4=str(HR4)
    HR4=HR4[1:-1]
    HR4=int(HR4)   
    HR5=str(HR5)
    HR5=HR5[1:-1]
    HR5=int(HR5)     
    HR6=str(HR6)
    HR6=HR6[1:-1]
    HR6=int(HR6)    
    HR7=str(HR7)
    HR7=HR7[1:-1]
    HR7=int(HR7)     
    HR8=str(HR8)
    HR8=HR8[1:-1]
    HR8=int(HR8)   
    HR9=str(HR9)
    HR9=HR9[1:-1]
    HR9=int(HR9)       
    HR10=str(HR10)
    HR10=HR10[1:-1]
    HR10=int(HR10)       
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp1, ser)   
    consigneHR.envoi_consigne(HR1, ser) 
    init_carte.init()
    print("Temp=",Temp1)
    print("HR=",HR1)
    t1=time.time()
    t=t1-t0
  
    while t<temps1:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1)    
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp2, ser)   
    consigneHR.envoi_consigne(HR2, ser)   
    print("Temp=",Temp2)
    print("HR=",HR2)
    while t<(temps1+temps2):
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, (temps1+temps2) )         
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp3, ser)   
    consigneHR.envoi_consigne(HR3, ser) 
    print("Temp=",Temp3)
    print("HR=",HR3)
    t1=time.time()
    t=t1-t0
 
    while t<temps1+temps2+temps3:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3)   
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp4, ser)   
    consigneHR.envoi_consigne(HR4, ser) 
    print("Temp=",Temp4)
    print("HR=",HR4)
    t1=time.time()
    t=t1-t0
 
    while t<temps1+temps2+temps3+temps4:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4)    
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp5, ser)   
    consigneHR.envoi_consigne(HR5, ser) 
    print("Temp=",Temp5)
    print("HR=",HR5)
    t1=time.time()
    t=t1-t0

    while t<temps1+temps2+temps3+temps4+temps5:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5)   

    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp6, ser)   
    consigneHR.envoi_consigne(HR6, ser) 
    print("Temp=",Temp6)
    print("HR=",HR6)
    t1=time.time()
    t=t1-t0
  
    while t<temps1+temps2+temps3+temps4+temps5+temps6:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6)  
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp7, ser)   
    consigneHR.envoi_consigne(HR7, ser) 
    print("Temp=",Temp7)
    print("HR=",HR7)
    t1=time.time()
    t=t1-t0
  
    while t<temps1+temps2+temps3+temps4+temps5+temps6+temps7:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6+temps7)
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp8, ser)   
    consigneHR.envoi_consigne(HR8, ser) 
    print("Temp=",Temp8)
    print("HR=",HR8)
    t1=time.time()
    t=t1-t0
  
    while t<temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8)     
    
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp9, ser)   
    consigneHR.envoi_consigne(HR9, ser) 
    print("Temp=",Temp9)
    print("HR=",HR9)
    t1=time.time()
    t=t1-t0

    while t<temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8+temps9:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8+temps9)                 
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp10, ser)   
    consigneHR.envoi_consigne(HR10, ser) 
    print("Temp=",Temp10)
    print("HR=",HR10)
    t1=time.time()
    t=t1-t0

    while t<temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8+temps9+temps10:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8+temps9+temps10)     

if n/3==11:
    temps1=list_temps[0:1]
    temps2=list_temps[1:2]
    temps3=list_temps[2:3]
    temps4=list_temps[3:4]
    temps5=list_temps[4:5]
    temps6=list_temps[5:6]
    temps7=list_temps[6:7]
    temps8=list_temps[7:8]
    temps9=list_temps[8:9]
    temps10=list_temps[9:10]
    temps11=list_temps[10:11]
    Temp1=list_Temp[0:1]
    Temp2=list_Temp[1:2]
    Temp3=list_Temp[2:3]
    Temp4=list_Temp[3:4]
    Temp5=list_Temp[4:5]
    Temp6=list_Temp[5:6]
    Temp7=list_Temp[6:7]
    Temp8=list_Temp[7:8]
    Temp9=list_Temp[8:9]
    Temp10=list_Temp[9:10]
    Temp11=list_Temp[10:11]
    HR1=list_HR[0:1]
    HR2=list_HR[1:2]
    HR3=list_HR[2:3]
    HR4=list_HR[3:4]
    HR5=list_HR[4:5]
    HR6=list_HR[5:6]
    HR7=list_HR[6:7]
    HR8=list_HR[7:8]
    HR9=list_HR[8:9]
    HR10=list_HR[9:10]
    HR11=list_HR[10:11]
    temps1=str(temps1)
    temps1=temps1[1:-1]
    temps1=int(temps1)
    temps1=temps1*60   
    temps2=str(temps2)
    temps2=temps2[1:-1]
    temps2=int(temps2)
    temps2=temps2*60   
    temps3=str(temps3)
    temps3=temps3[1:-1]
    temps3=int(temps3)
    temps3=temps3*60   
    temps4=str(temps4)
    temps4=temps4[1:-1]
    temps4=int(temps4)
    temps4=temps4*60      
    temps5=str(temps5)
    temps5=temps5[1:-1]
    temps5=int(temps5)
    temps5=temps5*60      
    temps6=str(temps6)
    temps6=temps6[1:-1]
    temps6=int(temps6)
    temps6=temps6*60     
    temps7=str(temps7)
    temps7=temps7[1:-1]
    temps7=int(temps7)
    temps7=temps7*60       
    temps8=str(temps8)
    temps8=temps8[1:-1]
    temps8=int(temps8)
    temps8=temps8*60       
    temps9=str(temps9)
    temps9=temps9[1:-1]
    temps9=int(temps9)
    temps9=temps9*60        
    temps10=str(temps10)
    temps10=temps10[1:-1]
    temps10=int(temps10)
    temps10=temps10*60    
    temps11=str(temps11)
    temps11=temps11[1:-1]
    temps11=int(temps11)
    temps11=temps11*60            
    Temp1=str(Temp1)
    Temp1=Temp1[1:-1]
    Temp1=int(Temp1)
    Temp2=str(Temp2)
    Temp2=Temp2[1:-1]
    Temp2=int(Temp2)    
    Temp3=str(Temp3)
    Temp3=Temp3[1:-1]
    Temp3=int(Temp3)    
    Temp4=str(Temp4)
    Temp4=Temp4[1:-1]
    Temp4=int(Temp4)  
    Temp5=str(Temp5)
    Temp5=Temp5[1:-1]
    Temp5=int(Temp5)    
    Temp6=str(Temp6)
    Temp6=Temp6[1:-1]
    Temp6=int(Temp6)
    Temp7=str(Temp7)
    Temp7=Temp7[1:-1]
    Temp7=int(Temp7)       
    Temp8=str(Temp8)
    Temp8=Temp8[1:-1]
    Temp8=int(Temp8)        
    Temp9=str(Temp9)
    Temp9=Temp9[1:-1]
    Temp9=int(Temp9)       
    Temp10=str(Temp10)
    Temp10=Temp10[1:-1]
    Temp10=int(Temp10)   
    Temp11=str(Temp11)
    Temp11=Temp11[1:-1]
    Temp11=int(Temp11)         
    HR1=str(HR1)
    HR1=HR1[1:-1]
    HR1=int(HR1)
    HR2=str(HR2)
    HR2=HR2[1:-1]
    HR2=int(HR2)    
    HR3=str(HR3)
    HR3=HR3[1:-1]
    HR3=int(HR3)    
    HR4=str(HR4)
    HR4=HR4[1:-1]
    HR4=int(HR4)   
    HR5=str(HR5)
    HR5=HR5[1:-1]
    HR5=int(HR5)     
    HR6=str(HR6)
    HR6=HR6[1:-1]
    HR6=int(HR6)    
    HR7=str(HR7)
    HR7=HR7[1:-1]
    HR7=int(HR7)     
    HR8=str(HR8)
    HR8=HR8[1:-1]
    HR8=int(HR8)   
    HR9=str(HR9)
    HR9=HR9[1:-1]
    HR9=int(HR9)       
    HR10=str(HR10)
    HR10=HR10[1:-1]
    HR10=int(HR10)     
    HR11=str(HR11)
    HR11=HR11[1:-1]
    HR11=int(HR11)           
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp1, ser)   
    consigneHR.envoi_consigne(HR1, ser) 
    init_carte.init()
    print("Temp=",Temp1)
    print("HR=",HR1)
    t1=time.time()
    t=t1-t0
  
    while t<temps1:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1)    
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp2, ser)   
    consigneHR.envoi_consigne(HR2, ser)   
    print("Temp=",Temp2)
    print("HR=",HR2)
    while t<(temps1+temps2):
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, (temps1+temps2) )         
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp3, ser)   
    consigneHR.envoi_consigne(HR3, ser) 
    print("Temp=",Temp3)
    print("HR=",HR3)
    t1=time.time()
    t=t1-t0
 
    while t<temps1+temps2+temps3:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3)   
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp4, ser)   
    consigneHR.envoi_consigne(HR4, ser) 
    print("Temp=",Temp4)
    print("HR=",HR4)
    t1=time.time()
    t=t1-t0
 
    while t<temps1+temps2+temps3+temps4:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4)    
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp5, ser)   
    consigneHR.envoi_consigne(HR5, ser) 
    print("Temp=",Temp5)
    print("HR=",HR5)
    t1=time.time()
    t=t1-t0

    while t<temps1+temps2+temps3+temps4+temps5:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5)   

    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp6, ser)   
    consigneHR.envoi_consigne(HR6, ser) 
    print("Temp=",Temp6)
    print("HR=",HR6)
    t1=time.time()
    t=t1-t0
  
    while t<temps1+temps2+temps3+temps4+temps5+temps6:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6)  
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp7, ser)   
    consigneHR.envoi_consigne(HR7, ser) 
    print("Temp=",Temp7)
    print("HR=",HR7)
    t1=time.time()
    t=t1-t0
  
    while t<temps1+temps2+temps3+temps4+temps5+temps6+temps7:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6+temps7)
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp8, ser)   
    consigneHR.envoi_consigne(HR8, ser) 
    print("Temp=",Temp8)
    print("HR=",HR8)
    t1=time.time()
    t=t1-t0
  
    while t<temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8)     
    
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp9, ser)   
    consigneHR.envoi_consigne(HR9, ser) 
    print("Temp=",Temp9)
    print("HR=",HR9)
    t1=time.time()
    t=t1-t0

    while t<temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8+temps9:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8+temps9)                 
        
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp10, ser)   
    consigneHR.envoi_consigne(HR10, ser) 
    print("Temp=",Temp10)
    print("HR=",HR10)
    t1=time.time()
    t=t1-t0

    while t<temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8+temps9+temps10:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8+temps9+temps10)
    
    ser=consigne.parametrage_serie()
    ser=consigneHR.parametrage_serie()
    consigne.envoi_consigne(Temp11, ser)   
    consigneHR.envoi_consigne(HR11, ser) 
    print("Temp=",Temp11)
    print("HR=",HR11)
    t1=time.time()
    t=t1-t0

    while t<temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8+temps9+temps10+temps11:
        init_carte.lecture(fichier, nbj, t)
        consigne.boucle(fichier2, t0, ser)
        time.sleep(ta)
        t1=time.time()
        t=t1-t0        
        print(t, temps1+temps2+temps3+temps4+temps5+temps6+temps7+temps8+temps9+temps10+temps11)
 
#if n/2==12:

print("fini")
