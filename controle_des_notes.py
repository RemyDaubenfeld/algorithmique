# On se propose de calculer la moyenne des notes d’un élève pour certaines matières ; français,
# maths, géographie et informatique.
# Pour chacune de ces matières, il faudra saisir un coefficient de pondération compris entre 1 et 10.
# Calculez la moyenne en tenant compte des coefficients de pondération.
# Affichez une appréciation :
# Si la moyenne est comprise entre 16 et 20, la mention est « Très bien ».
# Si la moyenne est comprise entre 12 et 16, la mention est « Bien ».
# Si la moyenne est comprise entre 8 et 12, la mention est « Assez bien ».
# Si la moyenne est comprise entre 4 et 8, la mention est « Insuffisant ».
# Si la moyenne est comprise entre 0 et 4, la mention est « Nul ».

# Il faut contrôler que les notes sont comprises entre 0 et 20 et que les coefficients sont compris
# entre 1 et 10. (reprise de l’exercice 9 feuille niveau II pour utiliser des boucles) 

print()

while True:
    try:
        note_fra=float(input("Veuillez saisir la note de français (/20) : "))
        if 0 <= note_fra <= 20:
            break
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
    except ValueError:
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")

print()

while True:
    try:
        coef_fra=float(input("Veuillez saisir le coefficient de la note de français (entre 1 et 10): ") )
        if 0 <= coef_fra <= 10:
            break
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
    except ValueError:
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")

print()

while True:
    try:
        note_math=float(input("Veuillez saisir la note de math (/20) : "))
        if 0 <= note_math <= 20:
            break
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
    except ValueError:
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")

print()

while True:
    try:
        coef_math=float(input("Veuillez saisir le coefficient de la note de math (entre 1 et 10): "))
        if 0 <= coef_math <= 10:
            break
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
    except ValueError:
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")

print()

while True:
    try:
        note_geom=float(input("Veuillez saisir la note de géométrie (/20) : "))
        if 0 <= note_geom <= 20:
            break
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
    except ValueError:
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")

print()

while True:
    try:
        coef_geom=float(input("Veuillez saisir le coefficient de la note de géométrie (entre 1 et 10): "))
        if 0 <= coef_geom <= 10:
            break
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
    except ValueError:
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")

print()

while True:
    try:
        note_info=float(input("Veuillez saisir la note d'informatique (/20) : "))
        if 0 <= note_info <= 20:
            break
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
    except ValueError:
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")

print()

while True:
    try:
        coef_info=float(input("Veuillez saisir le coefficient de la note d'informatique (entre 1 et 10): "))
        if 0 <= coef_info <= 10:
            break
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
    except ValueError:
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")

moy=round((note_fra*coef_fra+note_math*coef_math+note_geom*coef_geom+note_info*coef_info)/(coef_fra+coef_math+coef_geom+coef_info),1)

print()

if moy > 20:
    print("Bravo JB, bon courage...!")
elif moy >= 16 and moy <= 20:
    print(f'Votre moyenne est de {moy}/20, vous avez la mention "Très bien".')
elif moy >= 12 and moy < 16:
    print(f'Votre moyenne est de {moy}/20, vous avez la mention "Bien".')
elif moy >= 8 and moy < 12:
    print(f'Votre moyenne est de {moy}/20, vous avez la mention "Assez bien".')
elif moy >= 4 and moy < 8:
    print(f'Votre moyenne est de {moy}/20, vous avez la mention "Insuffisant".')
elif moy >= 0  and moy < 4:
    print(f'Votre moyenne est de {moy}/20, vous avez la mention "Nul".')

print()