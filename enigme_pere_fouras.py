import json
import random

def charger_enigmes(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        enigmes = json.load(f)      #Charge les énigmes dans un dictionnaire
    return enigmes
#print(charger_enigmes(''))

def enigme_pere_fouras():
    liste_enigmes = charger_enigmes("data\\enigmesPF.json")

    enigme = random.choice(liste_enigmes)
    question_enigme = enigme["question"]        #Choisit une énigme aléatoire
    vraie_reponse = enigme["reponse"].lower()   #La réponse est remise tout en minuscules
    nb_essais_restants = 3

    print("Père Fouras : Voici ton énigme !\n")
    print(question_enigme)

    while nb_essais_restants > 0:
        reponse_joueur = input("\nVotre réponse : ").strip().lower()

        if reponse_joueur == vraie_reponse: #Si la réponse est correcte
            print("\nBravo ! C'est la bonne réponse. Vous gagnez la clé !")
            return True
        else:
            nb_essais_restants -= 1     #Réduit le nombre d'essais restants

            if nb_essais_restants > 0:      #Si il reste des essais
                print("Mauvaise réponse. Il vous reste", nb_essais_restants, "essai(s). Essayez encore !")
            else:                       #Si tous les essais sont épuisés
                print("\nDommage ! Vous avez épuisé tous vos essais. La réponse correcte était :", vraie_reponse)
                return False
#print(enigme_pere_fouras())