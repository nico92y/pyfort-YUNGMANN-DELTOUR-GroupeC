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