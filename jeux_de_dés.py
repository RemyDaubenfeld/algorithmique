#Réalisez un jeu de dés utilisant les aiguillages conditionnels et affichant les faces du dé

import random

nombre = random.randint (1,6)

if nombre == 1:
    de = "un"
    face = "\n 0 \n"    

elif nombre == 2:
    de = "deux"
    face = "  0\n\n0  "

elif nombre == 3:
    de = "trois"
    face = "  0\n 0 \n0  "
    
elif nombre == 4:
    de = "quatre"
    face = "0 0\n\n0 0"

elif nombre == 5:
    de = "cinq"
    face = "0 0\n 0 \n0 0"

else:
    de = "six"
    face = "0 0\n0 0\n0 0"

print("\nJeux de dé\n")  
print(f"Vous avez fait un {de}.")
print(f"\n{face}\n")