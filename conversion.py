# Écrivez un algorithme qui convertisse un nombre de la base 10 vers la base 2 (en binaire).
# Le principe utilisé est celui de la division entière.
# Prenons le chiffre 19 pour le convertir en base 2.
# La division entière de 19 par 2 donne un quotient de 9 et un reste de 1.
# La division entière de 9 par 2 donne un quotient de 4 et un reste de 1.
# Plaçons les restes dans l’ordre inverse de leur apparition, nous obtenons « 11 ».
# La division de 4 par 2 donne un quotient de 2 et un reste de 0.
# L’accumulation des restes donne « 011 ».
# La division de 2 par 2 donne un quotient de 1 et un reste de 0.
# L’accumulation des restes donne « 0011 ».
# La division de 1 par 2 donne un quotient de 0 et un reste de 1.
# L’accumulation des restes donne « 10011 ».
# La conversion s’arrête là et le chiffre 19 converti en base 2 est « 10011 »

print("\nConversion d'un nombre de la base 10 vers la base 2\n")

while True:
    try:
        nombre = int(input("Veuillez entrer un nombre : "))
        if nombre >= 0:
            break
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
    except ValueError:
        print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")

quotient = 1
chiffre_binaire = ""

while quotient != 0:
    quotient = nombre // 2
    reste = nombre % 2
    nombre = quotient
    if reste == 0:
        i = "0"
    elif reste == 1:
        i = "1"
    chiffre_binaire = i + chiffre_binaire

print(f"\n{chiffre_binaire}\n")
