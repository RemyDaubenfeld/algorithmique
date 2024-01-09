# Saisissez un nombre compris entre 1 et 10. En cas d’erreur de saisie, il y a affichage d’un message «
# Valeur non permise ». Si le nombre est égal au nombre magique connu du programme, il affiche «
# Gagné » sinon il affiche un message « Trop petit » ou « Trop grand » suivant la valeur saisie.
# (reprise de « Chiffre magique 1 » pour utiliser des boucles)


import random

chiffre_magique = random.randint(1,10)
nombre = 0

print()

while True:
    try:
        nombre = int (input("Veuillez saisir un nombre entre 1 et 10 : "))
        if 1 <= nombre <=10:    
            break
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
    except ValueError:
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")



while nombre != chiffre_magique:
    if nombre < chiffre_magique:
        print("\nTrop petit !")
        while True:
            try:
                nombre = int(input("Veuillez saisir un nombre entre 1 et 10 : "))
                if 1 <= nombre <=10:    
                    break
                print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
            except ValueError:
                print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")



    elif nombre > chiffre_magique:
        print("\nTrop grand !")
        while True:
            try:
                nombre = int(input("Veuillez saisir un nombre entre 1 et 10 : "))
                if 1 <= nombre <=10:    
                    break
                print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
            except ValueError:
                print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")

print("\nBravo, vous avez gagné\n")