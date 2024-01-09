# Écrire un algorithme qui demande successivement 20 nombres à l’utilisateur, et qui lui dise ensuite
# quel était le plus grand parmi ces 20 nombres.
# SANS TABLEAUX !!!

print("\nRecherche du nombre le plus grand.\n\nVeuillez saisir successivement 20 nombres !\n")


request = 20
greater_number = 0
seizure = 0


for i in range(request):
    seizure = seizure + 1
    while True:
        try:
            number = float(input(f"Nombre {seizure} : "))
            break
        except ValueError:
            print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
    if number > greater_number:
        greater_number = number
     

print(f"\nLe plus grand nombre de votre saisie est {greater_number}.\n")