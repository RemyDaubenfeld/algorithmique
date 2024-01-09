# Permet de résoudre une équation

print("Cherchons à résoudre l'équation 'ax + b = 0'")

a = float(input("Veuillez saisir un nombre a : "))
b = float(input("Veuillez saisir un nombre b : "))

if a == 0 and b == 0:
    print("L'ensemble des solutions de x est les nombres réelles (ensemble R).")

elif a == 0 and b != 0:
    print("L'ensemble des solutions de x est l'ensemble Vide.")

else:
    print("x = -b/a")