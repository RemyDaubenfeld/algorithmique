# Réécrire l’algorithme précédent, mais cette fois-ci on ne connaît pas d’avance combien l’utilisateur
# souhaite saisir de nombres. La saisie des nombres s’arrête lorsque l’utilisateur entre un zéro.
number = ()
greater_number = 0
seizure = 0

print("\nRecherche du nombre le plus grand\n\nPour terminer la saisie, tapez '0' \n")

while number != 0:
    seizure = seizure + 1
    while True:
        try:
            number = float(input(f"Nombre {seizure} : "))
            if number == 0:
                break
            elif number > greater_number:
                greater_number = number
            break
        except ValueError:
            print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")

print(f"\nLe nombre le plus grand de votre saisie est {greater_number}.\n")