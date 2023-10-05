import os 
os.system('cls')


#application fitness


#gestion des aliments 


#liste aliments fruits


liste_aliments = []
liste_quantite = []
is_repeter_fruits = True 

while is_repeter_fruits:
    aliment = input("Choisissez un aliment : ")

    if aliment == "banane":
        quantite = float(input("Entrez la quantité en grammes (une banane fait envirion 128g) : "))
        liste_quantite.append(quantite)
    else:
        quantite = float(input("Entrez la quantité en grammes : "))
        liste_quantite.append(quantite)

    if aliment in liste_aliments:
        print("Cet éléments est deja dans la liste")

    else:
        liste_aliments.append(aliment)
    suite = input("Voulez-vous ajouter un autre aliment ? (n/y)")
    if suite == "n":
        is_repeter_fruits = False



kcal = 0
proteine = 0
vitamine_c = 0
vitamine_b6 = 0 
calcium = 0
magnesium = 0


aliment = liste_aliments[0]
nombre_elements = len(liste_aliments)



for aliments in liste_aliments:

    
   

    if aliments == "banane":
        kcal += 105/100*quantite
        proteine += 1/100*quantite
        vitamine_c += 10/100*quantite
        vitamine_b6 += 0.4/100*quantite
        calcium += 6/100*quantite
        magnesium += 32/100*quantite

    elif aliments == "fraise":
        kcal = kcal + 32/100*quantite
        proteine = proteine + 0.7/100*quantite
        vitamine_c = vitamine_c + 58.8/100*quantite
        vitamine_b6 = vitamine_b6 + 0.1/100*quantite
        calcium = calcium + 16/100*quantite
        magnesium = magnesium + 13/100*quantite

    elif aliments == "myrtille":
        kcal += 57/100*quantite
        proteine += 0.7/100*quantite
        vitamine_c += 9.7/100*quantite
        
        calcium += 6/100*quantite
        magnesium += 6/100*quantite

    elif aliments == "framboise":
        kcal += 52/100*quantite
        proteine += 1.2/100*quantite
        vitamine_c += 26.2/100*quantite
        
        calcium += 25/100*quantite
        magnesium += 22/100*quantite

    elif aliments == "mangue":
        kcal += 60/100*quantite
        proteine += 0.82/100*quantite
        vitamine_c += 36,4/100*quantite
        vitamine_b6 += 0.1/100*quantite
        calcium += 10/100*quantite
        magnesium += 9/100*quantite
    
    elif aliments == "ananas":
        kcal += 50/100*quantite
        proteine += 0.54/100*quantite
        vitamine_c += 39.7/100*quantite
        vitamine_b6 += 0.1/100*quantite
        calcium += 13/100*quantite
        magnesium += 12/100*quantite

    elif aliments == "kiwi":
        kcal += 61/100*quantite
        proteine += 1.14/100*quantite
        vitamine_c += 92.7/100*quantite
        vitamine_b6 += 0.1/100*quantite
        calcium += 34/100*quantite
        magnesium += 17/100*quantite

    elif aliments =="pomme":
        kcal += 52/100*quantite
        proteine += 0.3/100*quantite
        vitamine_c += 4.6/100*quantite
        
        calcium += 6/100*quantite
        magnesium += 5/100*quantite

    elif aliments == "poire":
        kcal += 57/100*quantite
        proteine += 0.4/100*quantite
        vitamine_c += 4/100*quantite
        
        calcium += 9/100*quantite
        magnesium += 9/100*quantite

    elif aliments == "peche":
        kcal += 39/100*quantite
        proteine += 0.91/100*quantite
        vitamine_c += 6.6/100*quantite
        
        calcium += 6/100*quantite
        magnesium += 9/100*quantite

    elif aliments == "orange":
        kcal += 43/100*quantite
        proteine += 0.9/100*quantite
        vitamine_c += 53.2/100*quantite
        vitamine_b6 += 0.06/100*quantite
        calcium += 43/100*quantite
        magnesium += 10/100*quantite

print("Il y a\n",kcal," kcal\n",proteine,"g protéines\n",vitamine_c,"mg vitamines c\n",vitamine_b6,"mg vitamines b6\n",calcium,"mg calcium\n",magnesium,"mg magnésium")
        


    



