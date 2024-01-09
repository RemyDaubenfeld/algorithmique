#  Permet d'affichez une table de multiplication
x=int(input("Veuillez saisir un nombre pour la table de multiplication : "))

print(f"Table de {x}")
for i in range(1,11):
    print(f"{i} x {x} = {i*x}")