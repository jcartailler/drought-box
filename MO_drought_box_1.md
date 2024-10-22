1.	Objet et domaine d’application
Mesure de la transpiration résiduelle de branches ou feuilles dans la Drought-Box 1.
2.	Documents de référence 

3.	Liste de diffusion et si nécessaire niveau de confidentialité
Toute personne souhaitant utiliser la Drought-Box 1. 
4.	Hygiène et sécurité
Attention aux coupures dues à la découpe des végétaux (sécateur ou lame de rasoir).
Attention aux brulures avec les résistances chauffantes.

5.	Principe de la méthode
Le dispositif permet de mesurer les cinétiques de transpiration résiduelle des arbres.
Ces pertes en eau seront mesurées grâce à des jauges de contraintes de 100g dans une boîte hermétique régulée en température et humidité 
relative. La vulnérabilité à la cavitation est une variable connue et mesurée sur un grand nombre d’espèces ligneuses, cependant il a été
remarqué que deux espèces/variétés ayant une même vulnérabilité à la cavitation pouvaient répondre différemment à des mêmes conditions 
environnementales stressantes en termes cinétique d’apparition de la cavitation. Cette cinétique devient donc une problématique majeure
dans la compréhension des réponses des végétaux à un stress hydrique. 
Le dispositif est composé d’une boite hermétique en isolant de 40 mm épaisseur (L=650 mm, l=650 mm, H=700 mm), de deux résistances 
chauffante (2x75W) au milieu et en bas de la boite, un capteur de température et d’humidité relative, un ventilateur, 8 jauges de 
contraintes de 100g reliées à deux cartes d’acquisition avec pont de Wheatstone (PhidgetBridge 4-Input), deux capteurs de déplacement 
LVDT (Linear Variable Differential Transformer) avec une carte d’acquisition (MCP3424), un système de régulation d’humidité (un 
débitmètre, deux électrovannes, des tuyaux à air comprimé), un Raspberry-pi (nano-ordinateur), et un Arduino (microcontrôleur) (Figure 1). 
Le Raspberry-Pi est relié aux cartes d’acquisitions des jauges et sert à l’acquisition des données de masse, il pilote tout le système et
enregistre les données de tous les capteurs (masse, température, humidité relative, déplacement) sur sa carte SD, mais ces données sont 
aussi disponibles via le web et peuvent être envoyées par mails à l’utilisateur. 
L’Arduino effectue la régulation de température et d’humidité relative, la lecture du capteur température / humidité relative et des 
capteurs LVDT. La régulation d’humidité se fait avec l’air comprimé sec pour diminuer la quantité d’eau dans l’air et au contraire l’air
comprimé passe dans un bulleur pour augmenter la quantité d’eau dans l’air.
Le capteur LVDT est un capteur de déplacement qui nous permet de mettre en parallèle la perte de masse et la variation de diamètre de la
branche. 
Les jauges de contraintes et leur carte d’acquisition donnent une réponse en ratio de tension (V/V), pour avoir une réponse en g nous 
avons fait un étalonnage avec des poids certifiés M1 (1, 2, 5, 10, 20, 35, 50, 70, 100).
La résolution de la carte de 119 nV/V (ce qui correspond à environ 20mg).
Plusieurs programme en langage Python ont été crée pour l’acquisition et le traitement des données. Les programmes d’acquisition sont de
deux types, le premier permet un pilotage en temps réel c'est-à-dire que l’utilisateur peut modifier la température de consigne, le temps
entre chaque mesure, faire des pauses et arrêter l’expérience, le deuxième est totalement automatique à l’aide d’un fichier de 
configuration et peut même réaliser des rampes de températures et d’humidité relative.
Le dispositif permet de mettre 8 branches en parallèle, vu que les cinétiques sont assez longues et cela permet d’avoir des répétitions 
dans les mêmes conditions.
![alt tag](https://user-images.githubusercontent.com/62540471/77655310-86fe7780-6f72-11ea-9544-c7b5917dc7ed.png)

 
Figure 1 : Schéma du dispositif.

6.	Matériels nécessaires
7.	Contraintes de la méthode

 
8.	Contenu du mode opératoire
a)	Utilisation de la box en mode température et humidité fixe tout au long de l’expérience :

1. Allumage du Raspberry pi (ordinateur) si besoin.
2. Ouvrir un terminal en haut à gauche de l’écran (Figure 3).
3. Aller dans le dossier Downloads (cd Downloads).
4. Modifier le fichier de configuration (scite config.txt)
Le fichier est composé d’une ligne avec toutes les consignes, l’ordre est le suivant : température, humidité relative, temps 
d’acquisition en seconde (temps entre chaque mesure), nombre d’échantillons (1 à 8), nombre de capteurs LVDT (0 à 2). 
(Exemple : 30,45,300,8,1).
5. Enregistrer le ficher (control+s) et fermer la fenêtre.
6. Accrocher les échantillons sur les jauges suivant le plan (Figure 2)
6. Lancer le programme (./exec) 
Les données brutes des jauges, des températures et de l’humidité relative s’affichent.
7. Allumer l’armoire électrique et l’éclairage (si besoin).
8. Pour arrêter le programme il faut appuyer sur ‘‘control+c’’.
9. Eteindre l'armoire electrique.

b)	Utilisation de la box en mode température et humidité variable :

1. Allumage du Raspberry pi (ordinateur) si besoin.
2. Ouvrir un terminal en haut à gauche de l’écran (Figure 3).
3. Aller dans le dossier Downloads (taper cd Downloads).
4. Modifier le fichier de configuration (taper scite rampeT_HR.txt)
Le fichier est composé d’une ligne avec toutes les consignes, l’ordre est le suivant : temps de la rampe en minutes, température et 
humidité relative et répéter suivant le nombre de rampe (Exemple pour trois rampes : 60,40,60,60,45,40,60,50,25). 
Nous sommes limités à 11 rampes. Pour que la box refroidisse en fin de manip mettre un derniere rampe à 25°C 40%.
5. Enregistrer le ficher (control+s) et fermer la fenêtre.
6. Lancer le programme (taper ./exec_rampe). Les données brutes des jauges, des températures et de l’humidité relative s’affichent.
7. Allumer l’armoire électrique et l’éclairage (si besoin).
8. Le programme s'arrete tous seul quand toute les rampes sont effectuer.
9. Arreter l'armoire electrique.



c)	Traiter les données pendant et après l’expérience :

Les données sont accessibles via un navigateur web avec l’adresse ‘‘147.99.146.253/resultats/’’ pour voir les dernières cliquer deux 
fois sur ‘‘last modified’’
Deux fichiers sont disponibles, le premier est le fichier des valeurs de jauges (le nom du fichier est composé de la date et l’heure de
lancement du programme exemple A_20180530_105022.don), le deuxième regroupe la température, l’humidité relative et les valeurs des 
capteurs LVDT s’ils sont branchés). Le nom du 2ème fichier est temp+ date et l’heure de lancement (exemple : A_temp20180530_105022.don).
Pour traiter les données deux programmes python sont disponible, ‘‘traitement_T_HR_X.py’’ pour la température et HR, et
‘‘traitement_masse1.5.py’’ pour les masses des branches ou feuilles.
Pour utiliser ces programmes :
•	Il faut installer python et les librairies utilisés, 
•	Lancer le programme python dans un éditeur de texte, 
•	Modifier la ligne fichier=("20180712_095308.csv") avec le nom du fichier, 
•	Mettre le fichier récupéré sur le web dans le même dossier que le programme, 
•	Lancer le programme python avec F5
Le programme de jauge génère un fichier résultats avec les données traitées des masses et un fichier image avec les cinétiques de chaque
capteur.
Pour le programme des températures, il ne génère qu’un fichier image avec les cinétiques de température, humidité relative et la teneur
en eau de l’air de la box.

 ![alt tag](https://user-images.githubusercontent.com/62540471/77655649-ff653880-6f72-11ea-979a-e6711fffa688.png)
Figure 2 : Placement des jauges de contrainte


  ![alt tag](https://user-images.githubusercontent.com/62540471/77656162-c1b4df80-6f73-11ea-8974-539dc7abb183.png)
