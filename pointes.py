# Une pointe est constituée d’une tête symbolisée par le caractère « _ » et d’une tige symbolisée par le
# caractère « | ». La dimension d’une pointe est la longueur de sa tige, qui correspond au nombre de
# caractères « | » présents.
# Ainsi :
# _
# |
# |
# |
# |
# est une pointe de dimension 4.
# L’objectif est d’afficher des pointes d’une dimension donnée.
# Écrire un algorithme affichant p pointes (côte à côte) de dimension d.

print()

while True:
    try:
        p = int(input("Veuillez saisir le nombre de pointes : "))
        if p > 0:
            break
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
    except ValueError:
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")

print()

while True:
    try:
        d = int(input("Veuillez saisir la dimension des pointes : "))
        if d > 0:
            break
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
    except ValueError:
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")

objectif = "_  " * p

for i in range(d):
    objectif += "\n" + "|  " * p

print(objectif) 

print()