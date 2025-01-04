import random
def suiv(joueur):
    return 1 if joueur == 0 else 0

def grille_vide():
    return [[" "," "," "],
            [" "," "," "],
            [" "," "," "]]

def affiche_grille(grille, message):
    print(message)
    for ligne in grille:
        ligne_texte = "| " + " | ".join(ligne) + " |"
        print(ligne_texte)
    print("--------------")
    return grille

def demande_position():
    valide = False
    while not valide:
        position = input("Entrez la position (ligne,colonne) entre 1 et 3 (ex: 1,2) : ")
        if ',' in position:
            ligne, colonne = position.split(',')
            if ligne.isdigit() and colonne.isdigit():
                ligne, colonne = int(ligne), int(colonne)
                if 1 <= ligne <= 3 and 1 <= colonne <= 3:
                    valide = True
                    return ligne - 1, colonne - 1
        print("Entrée invalide. Entrez une position valide.")

def init():
    grille = grille_vide()
    print("Positionnez vos bateaux :")
    for i in range(2):
        valide = False
        while not valide:
            print("Bateau", i)
            position = demande_position()
            if grille[position[0]][position[1]] == " ":
                valide = True
            else:
                print("Vous avez déjà placé un bateau à cette position.")
            grille[position[0]][position[1]] = "B"
    return affiche_grille(grille,"Voici où sont placés vos bateaux :")
#print(init())

def tour(joueur, grille_tirs_joueur, grille_adversaire):
    if joueur == 0:
        print("C'est à votre tour de faire feu! :")
        affiche_grille(grille_tirs_joueur,"Rappel de l'historique des tirs que vous avez effectués :")
        position = demande_position()
        if grille_adversaire[position[0]][position[1]] == "B":
            print("Touché coulé !")
            grille_tirs_joueur[position[0]][position[1]] = "X"
        else:
            print("Dans l'eau...")
            grille_tirs_joueur[position[0]][position[1]] = "."

    else:
        position = ((random.randint(0, 2)),(random.randint(0, 2)))
        print("Le maître du jeu tire en position", position)
        if grille_adversaire[position[0]][position[1]] == "B":
            print("Touché coulé !")
            grille_tirs_joueur[position[0]][position[1]] = "X"
        else:
            print("Dans l'eau...")
            grille_tirs_joueur[position[0]][position[1]] = "."

def gagne(grille_tirs_joueur):
    compteur = sum(ligne.count("X") for ligne in grille_tirs_joueur)
    return compteur == 2

def jeu_bataille_navale():
    print("Chaque joueur doit placer 2 bateaux sur une grille de 3x3.\nLes bateaux sont représentés par 'B' et les tirs manqués par '.'.\nLes bateaux coulés sont marqués par 'x'.\n")
    grille_joueur = init()
    grille_tirs_joueur = grille_vide()
    grille_tirs_adversaire = grille_vide()
    grille_adversaire = grille_vide()
    for i in range(2):
        valide = True
        while valide == True:
            ligne = random.randint(0, 2)
            colonne = random.randint(0, 2)
            if grille_adversaire[ligne][colonne] == " ":
                grille_adversaire[ligne][colonne] = "B"
                valide = False
    joueur = 0
    while True:
        if joueur == 0:
            tour(joueur, grille_tirs_joueur, grille_adversaire)
            if gagne(grille_tirs_joueur):
                print("Le joueur a gagné !")
                return True
        else:
            tour(joueur, grille_tirs_adversaire, grille_joueur)
            if gagne(grille_tirs_adversaire):
                print("Le maître du jeu a gagné. Vous avez perdu.")
                return False
        joueur = suiv(joueur)

print(jeu_bataille_navale())

