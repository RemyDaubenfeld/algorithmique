#  Demandez à saisir une date de la forme AAAA/MM/JJ (par exemple 2011/10/17) et afficher « Le
# 17 octobre 2011 est un lundi. » Pour connaitre le nom du jour, on part de la date avec :
# • A = année complète (dans l’exemple 2011),
# • M = numéro du mois (dans l’exemple 10),
# • J = numéro du jour (dans l’exemple 17).
# Si MM vaut 1 ou 2, il faut :
# • retrancher 1 à A,
# • ajouter 12 à M.
# Avec ces valeurs, on calcule un nombre N
# • N = J + ENT((13 * M + 3) / 5) + ENT(5 * A / 4) — ENT(A / 100) + ENT(A / 400)
# • N = MOD(N ; 7)
# N donne le nom du jour avec : 0 pour lundi, 1 pour mardi, ..., 6 pour dimanche 



date = input("\nVeuillez saisir la date sous la forme AAAA/MM/JJ : ")
annee = int(date[0] + date[1] + date[2] + date[3])
mois = int(date[5] + date[6])
jour = int(date[8] + date[9])


#print(f"\n{jour}/{mois}/{annee}\n")


if mois == 1 or mois == 2:
    annee = annee - 1
    mois = mois + 12


#print(f"\n{annee},{mois}\n")

n = jour + int((13*mois+3)/5) + int(5*annee/4) - int(annee/100) + int(annee/400)

n = (n % 7)

tab_jour = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
tab_mois = ["janvier", "février", "mars", "avril", "mai", "juin","juillet", "août", "septembre", "octobre", "décembre"]


print(f"\nLe {jour} {tab_mois[(int(mois)-1)]} {annee} est un {tab_jour[n]}.\n")