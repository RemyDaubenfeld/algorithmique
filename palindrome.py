# Definir si un mot est palindrome ou non

mot = input("veuillez saisir un mot : ")
mot_inverse = ""

for i in range(0, len(mot)):
    mot_inverse = mot[i] + mot_inverse

if mot == mot_inverse:
    print("palindrome")
else:
    print("non")
     