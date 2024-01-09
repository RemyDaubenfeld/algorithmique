n = int(input("Veuillez saisir un nombre : "))

# Calcul le reste de la division euclidienne de n par 2
reste = n % 2 # donne 0 ou 1

# On teste la valeur de reste
# Si reste vaut 0 alors n est pair
if reste == 0:
    print(f"{n} est un nombre pair.") # Cette instruction est exécutée seulement si la condition est vérifiée

# Si reste vaut 1 alors n est impair
if reste == 1:
    print(f"{n} est un nombre impair.") 