# Permet d'indiquer si des nombres sont triés en ordre coissant ou non

nombre_1=float(input("Veuillez saisir un premier nombre : "))
nombre_2=float(input("Veuillez saisir un deuxième nombre : ") )
nombre_3=float(input("Veuillez saisir un troisième nombre : "))

if nombre_1 < nombre_2 and nombre_2 < nombre_3:
    print("Les 3 nombres sont triés en ordre croissant.")
elif nombre_1 > nombre_2 and nombre_2 > nombre_3:
    print("Les 3 nombres sont triés en ordre décroissant.")
else:
    print("Les 3 nombres ne sont pas triés en ordre croissant.")