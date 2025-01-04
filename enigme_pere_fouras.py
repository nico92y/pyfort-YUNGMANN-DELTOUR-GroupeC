'''
import json
import random


def charger_enigmes(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        enigmes = json.load(f)
    return enigmes


def enigme_pere_fouras():
    l_enigmes = charger_enigmes("enigmesPF.json")
    enigme = random.choice(l_enigmes)
    question_enigme = enigme["question"]
    vraie_reponse = enigme["reponse"].lower()
    nb_essais_restants = 3

    print("Père Fouras : Voici ton énigme !\n")
    print(question_enigme)

    while nb_essais_restants > 0:
        reponse_joueur = input("\nVotre réponse : ").strip().lower()

        if reponse_joueur == vraie_reponse:
            print("\nBravo ! C'est la bonne réponse. Vous gagnez la clé !")
            return True
        else:
            nb_essais_restants -= 1

            if nb_essais_restants > 0:
                print("Mauvaise réponse. Il vous reste", nb_essais_restants, "essai(s). Essayez encore !")
            else:
                print("\nDommage ! Vous avez épuisé tous vos essais. La réponse correcte était :", vraie_reponse)
                return False




print(enigme_pere_fouras())'''




















import json
import random

def charger_enigmes(fichier):
    """
    Charge les énigmes depuis un fichier JSON.
    :param fichier: Chemin du fichier contenant les énigmes.
    :return: Liste des énigmes.
    """
    fichier_ouvert = open(fichier, 'r', encoding='utf-8')
    enigmes = json.load(fichier_ouvert)
    fichier_ouvert.close()
    return enigmes

def verifier_format_enigme(enigme):
    """
    Vérifie que l'énigme contient bien les clés 'question' et 'reponse'.
    :param enigme: Dictionnaire représentant une énigme.
    :return: True si le format est correct, False sinon.
    """
    return 'question' in enigme and 'reponse' in enigme

def enigme_pere_fouras():
    """
    Fonction principale pour jouer une énigme du Père Fouras.
    :return: True si le joueur répond correctement, sinon False.
    """
    l_enigmes = charger_enigmes("enigmesPF.json")

    if l_enigmes is None:
        print("Erreur : Impossible de charger les énigmes.")
        return False

    enigme = random.choice(l_enigmes)

    if not verifier_format_enigme(enigme):
        print("Erreur : une énigme dans le fichier est mal formatée.")
        return False

    question_enigme = enigme["question"]
    vraie_reponse = enigme["reponse"].strip().lower()
    nb_essais_restants = 3

    print("Père Fouras : Voici ton énigme !\n")
    print(question_enigme)

    while nb_essais_restants > 0:
        reponse_joueur = input("\nVotre réponse : ").strip().lower()

        if reponse_joueur == vraie_reponse:
            print("\nBravo ! C'est la bonne réponse. Vous gagnez la clé !")
            return True
        else:
            nb_essais_restants -= 1

            if nb_essais_restants > 0:
                print("Mauvaise réponse. Il vous reste", nb_essais_restants, "essai(s). Essayez encore !")
            else:
                print("\nDommage ! Vous avez épuisé tous vos essais. La réponse correcte était :", vraie_reponse)
                return False

# Exemple d'utilisation
if __name__ == "__main__":
    print(enigme_pere_fouras())
