# Permet de calculer l'âge d'une personne
import datetime

today = datetime.date.today()
current_year = today.year
birth_year=int(input("Veuillez saisir votre année de naissance : "))

print(f"Si vous êtes né(e) en {birth_year} vous avez {current_year-birth_year} ans.")