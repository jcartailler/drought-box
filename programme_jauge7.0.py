# -*-coding:Utf-8 -*
import time 
import csv
import serial
import consigne
import consigne2
import consigne3
import consigneHR
import init_carte


def init():
    fichier=time.strftime("%Y%m%d_%H%M%S"+".csv")
    z=input("Rentrer le nom de l'espece:") #demande Ã  l'utilisateur en quelle valeur faire la moyenne des conductances
    fichier=z+"_"+fichier
    fichier2=fichier
    file=open("/var/www/html/resultats/C_"+fichier,"w")
    file2=open("/var/www/html/resultats/C_temp_"+fichier,"w")
    file.close()
    file2.close()
    config = open("config.txt","r") #ouvert le fichier configuration
    reader = config.read() #lit le fichier en .txt
    list_Temp=list()
    list_temps=list()
    list_HR=list()
    list_jauges=list()
    list_LVDT=list()
    reader=reader.split(",")
    config.close()
    n=len(reader)
    n1=n/5
    n2=n
    while n1>0:
        a=n-n2
        b=n-n2+1
        T=reader[a:b]
        T=str(T)
        T=T[2:-2]
        T=int(T)
        HR=reader[a+1:b+1]
        HR=str(HR)
        HR=HR[2:-2]
        HR=int(HR)
        temps=reader[a+2:b+2]
        temps=str(temps)
        temps=temps[2:-2]
        temps=int(temps)    
        Nb_jauges=reader[a+3:b+3]
        Nb_jauges=str(Nb_jauges)
        Nb_jauges=Nb_jauges[2:-2]
        Nb_jauges=int(Nb_jauges)    
        LVDT=reader[a+4:b+4]
        LVDT=str(LVDT)
        LVDT=LVDT[2:-2]
        LVDT=int(LVDT)  
        n1=n1-1
        n2=n2-2
        list_Temp.append(T)
        list_HR.append(HR)
        list_temps.append(temps)
        list_jauges.append(Nb_jauges)
        list_LVDT.append(LVDT)
    
    print(list_Temp, list_HR, list_temps, list_jauges, list_LVDT)
    
    #print(n/2)
    t0=time.time()
    
    if n/5==1:
        Consigne=list_Temp[0:1]
        HR=list_HR[0:1]
        temps=list_temps[0:1]
        Nb_jauges=list_jauges[0:1]
        LVDT=list_LVDT[0:1]
        
        Consigne=str(Consigne)
        Consigne=Consigne[1:-1]
        Consigne=int(Consigne)
        HR=str(HR)
        HR=HR[1:-1]
        HR=int(HR)    
        temps=str(temps)
        temps=temps[1:-1]
        temps=int(temps)
        Nb_jauges=str(Nb_jauges)
        Nb_jauges=Nb_jauges[1:-1]
        Nb_jauges=int(Nb_jauges)
        LVDT=str(LVDT)
        LVDT=LVDT[1:-1]
        LVDT=int(LVDT)    
        
        if LVDT==0:
            ser=consigne.parametrage_serie()
            consigne.envoi_consigne(Consigne, ser)   
            ser=consigneHR.parametrage_serie()
            consigneHR.envoi_consigne(HR, ser)
            init_carte.init()
            #time.sleep(2)
            print("Temp=",Consigne)
            time.sleep(1)
            print("HR=",HR)    
            print("temps acquisition",temps)
            print("Nombre de jauges",Nb_jauges)
            print("Nombre de LDVT",LVDT)
            t0=time.time()
            t2=time.time()
            #time.sleep(10)

            a=0
            while a==0:
                t3 =time.time()-t2
                while t3< (temps):

                       t3=time.time()-t2
                t1=time.time() -t0
                t2=time.time()
                init_carte.lecture(fichier, Nb_jauges, t1)
                consigne.boucle(fichier2, t0, ser)
             
                        
            
        if LVDT==1:
            ser=consigne2.parametrage_serie()
            consigne2.envoi_consigne(Consigne, ser)   
            ser=consigneHR.parametrage_serie()
            consigneHR.envoi_consigne(HR, ser)
            init_carte.init()
            #time.sleep(2)
            print("Temp=",Consigne)
            time.sleep(1)
            print("HR=",HR)    
            print("temps acquisition",temps)
            print("Nombre de jauges",Nb_jauges)
            print("Nombre de LDVT",LVDT)
            t0=time.time()
            t2=time.time()
            #time.sleep(10)

            a=0
            while a==0:
                t3 =time.time()-t2
                while t3< (temps):

                       t3=time.time()-t2
                t1=time.time() -t0
                t2=time.time()
                init_carte.lecture(fichier, Nb_jauges, t1)
                consigne.boucle(fichier2, t0, ser)
             
            
            
        if LVDT==2:
            
            ser=consigne3.parametrage_serie()
            consigne3.envoi_consigne(Consigne, ser)   
            ser=consigneHR.parametrage_serie()
            consigneHR.envoi_consigne(HR, ser)
            init_carte.init()
          #  time.sleep(2)
            print("Temp=",Consigne)
            time.sleep(1)
            print("HR=",HR)    
            print("temps acquisition",temps)
            print("Nombre de jauges",Nb_jauges)
            print("Nombre de LDVT",LVDT)
            t0=time.time()
            t2=time.time()
            #time.sleep(10)

            a=0
            while a==0:
                t3 =time.time()-t2
                while t3< (temps):

                       t3=time.time()-t2
                t1=time.time() -t0
                t2=time.time()
                init_carte.lecture(fichier, Nb_jauges, t1)
                consigne.boucle(fichier2, t0, ser)

    
    if n/5 !=1:
        print("erreur")
        
init()
