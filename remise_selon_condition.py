# Permet d'appliquer une remise selon des conditions

montant_ttc=float(input("Veuillez saisir un montant TTC (€)"))

remise = 0
   
if montant_ttc >= 500 and montant_ttc < 1000:
    remise = 2
    
elif montant_ttc >= 1000 and montant_ttc < 2000:
    remise = 5
   
elif montant_ttc >= 2000:
    remise = 10

else:
    remise = 0

print(f"Vous bénéficiez d'une remise de {remise}%, le montant TTC est donc de {round(montant_ttc*(1-remise/100))} €.")

