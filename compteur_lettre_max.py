# Faire un programme permettant de trouver la lettre qui est la plus présente dans un texte et afficher le nombre de fois

texte = input("Veuillez tapez votre texte : ").lower() # .lower() transforme les majuscules en minuscule

cpt_max = 0
letter_max = ""
# On parcours chaque lettre du texte
for letter in texte:
    cpt = 0
    for letter_to_compare in texte:
        if letter == letter_to_compare and letter != " ":
            cpt += 1
    if cpt > cpt_max:
        cpt_max = cpt
        letter_max = letter

print(f"\nLa lettre la plus présente est '{letter_max}' avec {cpt_max} occurences.")



    







