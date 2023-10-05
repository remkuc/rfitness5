import os 
import time 
import sys
os.system('cls')

print("Ce programme permet de compter vos pulsations du coeur")

input("Entrez sur enter pour continuer: ")


duree = 15
debut = time.time()
nbrs_battements = 0

while time.time() - debut < duree:
    nbrs = input("A chaque pulsations cliqué sur enter : ")
    if nbrs == "":
        nbrs_battements += 1 
    temps_ecoule = time.time() - debut
    if temps_ecoule >= duree:
        print("Temps écoulé")
        nbrs_battements = nbrs_battements*4
        print("Vous avez un rythme de ",nbrs_battements," battements par minutes")
        sys.exit()  

