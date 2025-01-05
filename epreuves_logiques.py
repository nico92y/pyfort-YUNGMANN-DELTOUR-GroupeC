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
    valide = False      # 2 bateaux à placer
    while not valide:
        position = input("Entrez la position (ligne,colonne) entre 1 et 3 (ex: 1,2) : ")
        if ',' in position:
            ligne, colonne = position.split(',')
            if ligne.isdigit() and colonne.isdigit():
                ligne, colonne = int(ligne), int(colonne)
                if 1 <= ligne <= 3 and 1 <= colonne <= 3:
                    return ligne - 1, colonne - 1       #Retourne la position adaptée (indices de 0 à 2)
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
    if joueur == 0:         #Tour du joueur
        print("C'est à votre tour de faire feu! :")
        affiche_grille(grille_tirs_joueur,"Rappel de l'historique des tirs que vous avez effectués :")
        position = demande_position()
        if grille_adversaire[position[0]][position[1]] == "B":  #Vérifie si le tir est touché
            print("Touché coulé !")
            grille_tirs_joueur[position[0]][position[1]] = "X"  #Marque le bateau touché
        else:
            print("Dans l'eau...")
            grille_tirs_joueur[position[0]][position[1]] = "."  #Marque un tir manqué

    else:
        position = ((random.randint(0, 2) + 1),(random.randint(0, 2) + 1))  #Cette ligne sert à prendre les attaques du Maitre du jeu, "+ 1" sert lors du print
        print("Le maître du jeu tire en position", position)                            #(Exemple : ne pas écrire 0, lorsque c'est la première ligne)
        if grille_adversaire[position[0]-1][position[1]-1] == "B":
            print("Touché coulé !")
            grille_tirs_joueur[position[0]-1][position[1]-1] = "X"                      #Avec les lignes 62 et 67, Les "-1" servent à bien positionner les attaques du Maitre du jeu.
        else:           #Tour du maître du jeu
            print("Dans l'eau...")
            grille_tirs_joueur[position[0]-1][position[1]-1] = "."

def gagne(grille_tirs_joueur):
    compteur = 0
    for ligne in grille_tirs_joueur:
        for case in ligne:
            if case == "X":
                compteur += 1       # Compte les touches
    return compteur == 2

def jeu_bataille_navale():
    print("Chaque joueur doit placer 2 bateaux sur une grille de 3x3.\nLes bateaux sont représentés par 'B' et les tirs manqués par '.'.\nLes bateaux coulés sont marqués par 'X'.\n")
    grille_joueur = init()
    grille_tirs_joueur = grille_vide()
    grille_tirs_adversaire = grille_vide()
    grille_adversaire = grille_vide()
    for i in range(2):
        valide = True
        while valide:
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
#print(jeu_bataille_navale())
