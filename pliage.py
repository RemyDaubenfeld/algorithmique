# L’élève placé au fond de la classe, près du radiateur, est le meilleur de la classe. Pour tuer le temps,
# il décide de plier une feuille en deux puis en deux, puis… en deux, puis… Écrivez un algorithme
# qui calcule l’épaisseur du pliage final à partir du nombre de plis et de l’épaisseur initiale de la
# feuille.

print()

while True:
    try:
        nombre_plis = int(input("Veuillez rentrer un nombre de plis à faire : "))
        if nombre_plis >= 0:
            break
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
    except ValueError:
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")

print()

while True:
    try:
        epaisseur_initiale = int(input("Veuillez rentrer un nombre de plis à faire : "))
        if epaisseur_initiale > 0:
            break
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
    except ValueError:
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")

for i in range (nombre_plis):
    epaisseur_initiale *= 2

print(f"\nAprès {nombre_plis} pliage, la feuille à une épaisseur de {epaisseur_initiale}.\n")
