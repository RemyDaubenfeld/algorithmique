# Ecrire un programme qui intègre les fonctionnalités suivantes :
#   demander le nombre de matières à saisir
#   stocker le nom des matières
#   demander le nombre d'élève à ajouter et stocker leur nom et prénom
#   pour chaque élève saisir la note par matière
#   afficher tous les élèves avec leur moyenne générales et leurs notes par matières
#   afficher la moyenne de la classe par matière
#   donner le nom du meilleur élève
#   donner le nom du pire élève

print()

# Définition des fonctions
def nombre_matieres_eleves(nombre): #nombre de matieres et nombre d'élèves
    while True:
        try:
            n = int(input(f"Veuillez saisir le nombre {nombre} : "))
            if 0 < n:
                return n
            print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
        except ValueError:
            print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")


# début du programme
print()

# Saisie du nombre de matière
nombre_matiere = nombre_matieres_eleves("de matière(s)")
# print(nombre_matiere)

print()

# Saisie des matières dans un tableau
tab_matiere = []
for i in range (nombre_matiere):
    tab_matiere += [input(f"Veuillez saisir la matière {i + 1} : ")]

print()

# Saisie du nombre d'élève
nombre_eleve = nombre_matieres_eleves("d'élève(s)")
#print(nombre_eleve)

# Saisie du nom et prénom des élèves dans des tableaux
tab_nom = []
tab_prenom = []
for eleve in range (nombre_eleve):
    tab_nom += [input(f"\nVeuillez saisir le nom de l'élève {eleve + 1}: ")]
    tab_prenom += [input(f"Veuillez saisir le prénom de l'élève {eleve + 1}: ")]

# création des tableaux de notes par élève et de la moyenne générale de chaque élève
tab_notes_eleve = []
tab_moyennes_generales = []
# Saisie des notes des matières par élèves et calcul de la moyenne général
for i in range (nombre_eleve) :
    tab_notes_eleve.append([])
    moyenne = 0
    note = 0
    print()
    for j in range (nombre_matiere):
        while True:
            try:
                notes_eleve = float(input(f"Veuillez saisir la note de {tab_matiere[j]} de {tab_nom[i]} {tab_prenom[i]} : "))
                if 0 <= notes_eleve <= 20:
                    break
                print("\nVotre note doit être comprise entre 0 et 20.")
            except ValueError:
                print("\nVotre saisie est invalide. SVP RECOMMENCEZ !")
        moyenne += notes_eleve
        note += 1
        tab_notes_eleve [i] += [notes_eleve] # Les notes sont stockées par élèves, dans l'ordre des matières
    tab_moyennes_generales += [moyenne/note]

print(tab_notes_eleve)
print(tab_moyennes_generales)

print()

# Affichage des élèves avec leur moyenne générale et leur note par matière
tab_notes_par_matiere = []

for i in range (nombre_eleve):
    tab_notes_par_matiere.append([])
    matiere_note=[]
    for j in range(len(tab_notes_eleve[i])):
        matiere_note = str(tab_matiere[j]) + ": " + str(tab_notes_eleve[i][j]) + " "
        tab_notes_par_matiere[i] += [matiere_note]

    print(f'{tab_nom[i]} {tab_prenom[i]} à {round(tab_moyennes_generales[i],2)} de moyenne. Voici ses notes par matière: {"".join(tab_notes_par_matiere[i])}')

print()

# Affichage de la moyenne de la classe par matière
tab_moyennes_matieres = [] 

for i in range (nombre_matiere):
    notes = 0
    moyenne = 0
    for j in range (len(tab_notes_eleve)):
        notes += tab_notes_eleve[j][i]
        moyenne +=1
    tab_moyennes_matieres += [notes/moyenne]
    
    print(f"La moyenne de la classe en {tab_matiere[i]} est {round(tab_moyennes_matieres[i],2)}.")

# Affichage du meilleur et du pire élève
meilleur_eleve = tab_moyennes_generales[0]
nom_meilleur_eleve = tab_prenom[0] + " " + tab_nom[0]
pire_eleve = tab_moyennes_generales
nom_pire_eleve = tab_prenom[0] + " " + tab_nom[0]

for i in range (nombre_eleve):
    if tab_moyennes_generales[i] > meilleur_eleve:
        meilleur_eleve = tab_moyennes_generales [i]
        nom_meilleur_eleve = tab_prenom [i] + " " + tab_nom [i]
    elif tab_moyennes_generales[i] < tab_moyennes_generales[0]:
        pire_eleve = tab_moyennes_generales [i]
        nom_pire_eleve = tab_prenom [i] + " " + tab_nom [i]

print(f"\nDans la classe, le meilleur élève est {nom_meilleur_eleve} 👍 et le pire élève est {nom_pire_eleve} 👎.\n")