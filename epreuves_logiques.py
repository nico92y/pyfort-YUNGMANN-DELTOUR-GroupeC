import random
def suiv(joueur):
    if joueur == 0:
        joueur = 1
    else:
        joueur = 0
    return joueur

def grille_vide():
    return [[" "," "," "],
            [" "," "," "],
            [" "," "," "]]

def affiche_grille(grille, message):
    print(message)
    for ligne in grille:
        ligne_texte = "| "
        for case in ligne:
            ligne_texte += f"{case} | "
        print(ligne_texte)
    print("--------------")

def demande_position():
    print("Placez votre bateau\n")
    ligne = int(input("Entrez la ligne (ex: 1 3) :"))
    colonne = int(input("Entrez la colonne (ex: 1 3) :"))
    while ligne < 1 or ligne > 3:
        ligne = int(input("Entrez une position pour la ligne valide (ex: 1 3) :"))
    while colonne < 1 or colonne > 3:
        colonne = int(input("Entrez une position pour la colonne valide (ex: 1 3) :"))
    resultat = (ligne-1,colonne-1)
    return resultat

def init():
    grille = grille_vide()
    for i in range(2):
        a = demande_position()
        grille[a[0]][a[1]] = "B"
    return affiche_grille(grille,"Voici où sont placés vos bateaux :")
#print(init())

def verifier_tir(grille_tirs, ligne, colonne):
    """Vérifie si la position a déjà été jouée"""
    if grille_tirs[ligne][colonne] != " ":
        return False
    return True

def tour(joueur, grille_tirs_joueur, grille_adversaire):
    print("C'est au tour de joueur",joueur,":")
    if joueur == 1:
        affiche_grille(grille_tirs_joueur, "Rappel de l'historique des tirs que vous avez effectués : ")
        print("Saisissez une position pour le tir :") 
        a = demande_position()
        if grille_adversaire[a[0]][a[1]] == "B":
            print("Touché !")
            grille_tirs_joueur[a[0]][a[1]],grille_adversaire[a[0]][a[1]] = "X","X"
        else:
            print("Manqué !")
            grille_tirs_joueur[a[0]][a[1]],grille_adversaire[a[0]][a[1]] = ".","."
    else:
        ligne = random.randint(0,2)
        colonne = random.randint(0,2)
        while verifier_tir(grille_adversaire, ligne, colonne) == False:
            ligne = random.randint(0,2)
            colonne = random.randint(0,2)
        if grille_adversaire[ligne][colonne] == "B":
            grille_tirs_joueur[ligne][colonne],grille_adversaire[ligne][colonne] = "X","X"
        else:
            grille_tirs_joueur[ligne][colonne],grille_adversaire[ligne][colonne] = ".","."
print(tour(1,init(),init()))


