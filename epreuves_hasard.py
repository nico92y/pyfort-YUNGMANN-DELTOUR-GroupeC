import random

def bonneteau():
    bonneteaux = ['A', 'B', 'C']
    cle_sous_bonneteau = random.choice(bonneteaux)

    print("Bienvenue au jeu du bonneteau! \n Vous avez 2 essais pour retrouver la clé cachée. \n")

    for tentative in range(1,3):
        choix_joueur = input("Tentative " + str(tentative) +": Choisissez un bonneteau parmi A, B, C: ")
        while choix_joueur not in bonneteaux:
            choix_joueur = input("Mauvais choix! Choisissez un bonneteau parmi A, B, C: ")
        if choix_joueur == cle_sous_bonneteau:
            print("Bravo! Vous avez retrouvé la clé sous le bonneteau.")
            return True
        else:
            print("Dommage! La clé n'est pas sous ce bonneteau.\n")

    print("Vous avez perdu! La clé se trouvait sous le bonneteau", cle_sous_bonneteau, ".")
    return False
#print(bonneteau())

def jeu_lance_des():
    print("Bienvenue au jeu des dés! \n Le premier à faire un 6 gagne. \n")
    for i in range(3,0,-1):
        print("il reste ",i,"essais")
        input("Appuyez sur la touche 'Entrée' pour lancer les dés. \n")
        joueur1 = (random.randint(1,6),random.randint(1,6))(())
        print("vous avez obtenu ",joueur1,".")
        if joueur1[0]==6 or joueur1[1]==6:
            print("Bravo! Vous gagnez une clé.")
            return True
        joueur_m = (random.randint(1,6),random.randint(1,6))
        print("Le maitre du jeu a obtenu ", joueur_m, ".\n")
        if joueur_m[0]==6 or joueur_m[1]==6:
            print("Le Maitre du jeu a gagné")
            return False
        if i > 1:
            print("Personne n'a gagné, on passe au tour suivant!! \n")
    print("C'est un match nul!!")
    return False
#print(jeu_lance_des())



def epreuve_hasard():
    epreuves = [bonneteau,jeu_lance_des]
    epreuve_choisie = random.choice(epreuves)
    epreuve_choisie()
print(epreuve_hasard())
