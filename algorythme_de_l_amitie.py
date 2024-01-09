# reprendre l'algorithme de l'amitié de Sheldon COOPER dans TBBT


print("\nL'ALGORITHME DE L'AMITIE DE SHELDON\n\n")
print("Sheldon tente de nouer une amitié avec Kripke, il l'appel...\n")

message_fin = "MISSION REUSSI, UNE AMITIE COMMENCE"

reponse = ()
while reponse != "oui" and reponse != "non":
    reponse = input("Est-ce que Kripke répond?\n(Tapez oui ou non): ")
    

if reponse == "oui":
    print("\nAllo Kripke, c'est le docteur Sheldon COOPER, voudrais-tu partager un repas avec moi?")
    repas = ()
    while repas != "oui" and repas != "non":
        repas = input("(Si Kripke accepte , tapez oui, s'il refuse, tapez non) : ")

    if repas == "oui":
        print("\nSheldon dit: Très bien, alors dinons ensemble\n")
        print(f"{message_fin}\n")

    else:
        print("\nSheldon demande alors si Kripke apprécie les boissons chaudes")
        boisson = ()
        while boisson != "oui" and boisson != "non":
            boisson = input("Si Kripket aime les boissons chaude tapez oui, sinon tapez non : ")
        
        if boisson == "oui":
            print("\nSheldon demande à Kripke s'il préfère un thé, un café ou un chocolat chaud.")
            have_boisson = ()
            while have_boisson!= "thé" and have_boisson != "café" and have_boisson != "chocolat chaud":
                have_boisson = input("Si Kripke préfère un thé, tapez : thé\nSi Kripke préfère un café, tapez : café\nSi Kripke préfère un chocolat chaud tapez : chocolat chaud\nVotre choix : ")
            print(f"\n{message_fin}\n")
        
        else:
            for n in range (1,8):
                if n <= 6:
                    print("\nSheldon demande ensuite à Kripke de lui indiquer une activité récréative qu'il aime faire\n")
                    activite = input("Quelle activité Kripke aime faire? : ")
                    interet = ()
                    while interet !="oui" and interet != "non":
                        interet = input(f"\nEst-ce que Sheldon partage cet intérêt pour l'activité n°{n} '{activite}'?\nSi Sheldon partage cet intérêt, tapez oui\nSi Sheldon ne partage pas cet intérêt, tapez non : ")
                    
                    if interet == "oui":
                        print(f"\nSheldon partage également cet intérêt. Il lui demande : fantastique, pourquoi ne pas la pratiquer ensemble?\n\n{message_fin}\n")
                        break
                        
                elif n > 6:
                    print(f"\nSheldon choisit alors la dernière option, qui finalement lui semble la plus acceptable et partage l'activité {activite} avec Kripke.\n\n{message_fin}\n")

else:
    print("\nKripke ne répond pas, Sheldon lui laisse alors un message et attend qu'il le rappel.\n\nKripke rappel Sheldon qui lui demande s'il voudrait partager un repas avec lui.")
    repas = ()
    while repas != "oui" and repas != "non":
        repas = input("Si Kripke accepte, tapez oui\nS'il refuse, tapez non : ")

    if repas == "oui":
            print("\nSheldon dit: Très bien, alors dinons ensemble\n")
            print(f"{message_fin}\n")
    
    else:
        print("\nSheldon demande alors si Kripke apprécie les boissons chaudes.")
        boisson = ()
        while boisson != "oui" and boisson != "non":
            boisson = input("\nSi Kripke aime les boissons chaude tapez oui\nSinon tapez non : ")

        if boisson == "oui":
            print("\nSheldon demande à Kripke s'il préfère un thé, un café ou un chocolat chaud.")
            have_boisson = ()
            while have_boisson != "thé" and have_boisson !="café" and have_boisson !="chocolat chaud":
                have_boisson = input("Si Kripke préfère un thé, tapez : thé\nSi Kripke préfère un café, tapez : café\nSi Kripke préfère un chocolat chaud tapez : chocolat chaud:\nVotre choix : ")
            print(f"\n{message_fin}\n")
        
        else:
            for n in range (1,8):
                if n <= 6:
                    print("\nSheldon demande ensuite à Kripke de lui indiquer une activité récréative qu'il aime faire\n")
                    activite = input("Quelle activité Kripke aime faire? : ")
                    interet = ()
                    while interet !="oui" and interet != "non":
                        interet = input(f"\nEst-ce que Sheldon partage cet l'intérêt pour l'activité n°{n} '{activite}'?\nSi Sheldon partage cet intérêt, tapez oui\nSi Sheldon ne partage pas cet intérêt, tapez non : ")
                    
                    if interet == "oui":
                        print(f"\nSheldon partage également cet intérêt. Il lui demande : fantastique, pourquoi ne pas la pratiquer ensemble?\n\n{message_fin}\n")
                        break
                        
                elif n > 6:
                    print(f"\nSheldon choisit alors la dernière option, qui finalement lui semble la plus acceptable et partage l'activité {activite} avec Kripke.\n\n{message_fin}\n")       