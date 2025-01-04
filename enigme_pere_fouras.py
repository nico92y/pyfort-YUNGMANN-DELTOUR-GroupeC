import json
import random


def charger_enigmes(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        enigmes = json.load(f)
    return enigmes

print(charger_enigmes('data\\enigmesPF.json'))

def enigme_pere_fouras():
    enigmes = charger_enigmes("data\\enigmesPF.json")

    enigme = random.choice(enigmes)
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


#print(enigme_pere_fouras())