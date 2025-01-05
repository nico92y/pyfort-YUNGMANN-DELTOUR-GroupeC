import random

def bonneteau():
    bonneteaux = ['A', 'B', 'C']
    cle_sous_bonneteau = random.choice(bonneteaux)  #Choisit aléatoirement où se cache la clé

    print("Bienvenue au jeu du bonneteau! \nVous avez 2 essais pour retrouver la clé cachée. \n")

    for tentative in range(1,3):
        choix_joueur = input("Tentative " + str(tentative) +": Choisissez un bonneteau parmi A, B, C: ")
        while choix_joueur not in bonneteaux:       #Vérifie que l'entrée est valide
            choix_joueur = input("Mauvais choix! Choisissez un bonneteau parmi A, B, C: ")
        if choix_joueur == cle_sous_bonneteau:      #Vérifie si la réponse est correcte
            print("Bravo! Vous avez retrouvé la clé sous le bonneteau.")
            return True
        else:
            print("Dommage! La clé n'est pas sous ce bonneteau.\n")
    print("Vous avez perdu! La clé se trouvait sous le bonneteau", cle_sous_bonneteau, ".")
    return False
#print(bonneteau())

def jeu_lance_des():
    print("Bienvenue au jeu des dés! \nLe premier à faire un 6 gagne. \n")
    for i in range(3, 0, -1):                       #3 essais pour lancer les dés
        print("Il reste", i, "essais.")
        input("Appuyez sur la touche 'Entrée' pour lancer les dés. \n")
        joueur1 = (random.randint(1, 6), random.randint(1, 6))      #Lance 2 dés pour le joueur
        print("Vous avez obtenu", joueur1, ".")
        if joueur1[0] == 6 or joueur1[1] == 6:      #Vérifie si le joueur à gagner
            print("Bravo! Vous gagnez une clé.")
            return True
        joueur_m = (random.randint(1, 6), random.randint(1, 6))     #Lance 2 dés pour le maître du jeu
        print("Le maître du jeu a obtenu", joueur_m, ".\n")
        if joueur_m[0] == 6 or joueur_m[1] == 6:    #Vérifie si le maître à gagner
            print("Le Maître du jeu a gagné")
            return False
        if i > 1:
            print("Personne n'a gagné, on passe au tour suivant!\n")
    print("C'est un match nul!")
    return False
#print(jeu_lance_des())


def epreuve_hasard():
    epreuves = [bonneteau,jeu_lance_des]
    epreuve_choisie = random.choice(epreuves)
    return epreuve_choisie()
#print(epreuve_hasard())
