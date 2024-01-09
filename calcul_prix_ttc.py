# Calculer le prix TTC d'un prix HT en sélectionnant le taux de TVA

prix_HT = float(input("Saisissez le prix HT (€) : "))
print("Pour une TVA de 5,5 %, saisissez 1")
print("Pour une TVA de 19,6 %, saisissez 2")
print("Pour une TVA de 33 %, saisissez 3")
tva = int(input("Saisissez le code du taux de TVA voulu : "))

while tva != 1 and tva !=2 and tva !=3 :
    print("Pour une TVA de 5,5 %, saisissez 1")
    print("Pour une TVA de 19,6 %, saisissez 2")
    print("Pour une TVA de 33 %, saisissez 3")
    tva = int(input("Saisissez le code du taux de TVA voulu :  "))

if tva == 1 :
    print(f"Le prix HT est de {prix_HT} €, la TVA est de 5,5 % et le prix TTC est de {round(prix_HT*1.055,2)} €.")

elif tva == 2 :
    print(f"Le prix HT est de {prix_HT} €, la TVA est de 19,6 % et le prix TTC est de {round(prix_HT*1.196,2)} €.")

elif tva == 3 :
    print(f"Le prix HT est de {prix_HT} €, la TVA est de 33 % et le prix TTC est de {round(prix_HT*1.33,2)} €.") 
    