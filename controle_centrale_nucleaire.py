# Le contrôle d’une centrale nucléaire se fait par l’examen de températures.
# Si la différence entre la température ambiante et la température des bassins de refroidissement est
# inférieure à 20 °C ou si elle dépasse 40 °C, affichez une alarme. 

temp_ambiante = float(input("Veuillez saisir la température ambiante (°C) : "))
temp_bassins = float(input("Veuillez saisir la température des bassins de refroidissement (°C) : "))

if abs(temp_ambiante-temp_bassins) < 20 or abs(temp_ambiante-temp_bassins) > 40:
    print("Alarme")
else:
    print("La température est normal.")