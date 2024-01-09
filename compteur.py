# Réalisez un compteur qui affiche toutes les valeurs comprises entre une borne de départ et une
# borne d’arrivée en tenant compte d’un pas d’incrément.
# Exemple :
# Borne de départ = 3
# Borne d’arrivée = 12
# Pas = 2
# Affichage de 3 5 7 9 11 

print()
while True:
    try:
        borne_depart = int(input("Veuillez saisir une valeur de départ : "))
        if borne_depart >= 0:
            break
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
    except ValueError:
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")

print()

while True:
    try:
        borne_arrivee = int(input("Veuillez saisir une valeur d'arrivée : "))
        if borne_arrivee >= borne_depart:
            break
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
    except ValueError:
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")

print()

while True:
    try:
        pas = int(input("Veuillez saisir un pas d'incrément : "))
        break
    except ValueError:
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")


while borne_depart <= borne_arrivee:
    print(borne_depart)
    borne_depart += pas