import random
import json

def salle_De_Tresor():
    #Charger le fichier JSON contenant les données de indicesSalle.json
    with open("data\\indicesSalle.json", "r", encoding='utf-8') as fichier:
        jeu_tv = json.load(fichier)

    print("Bienvenue dans la salle de tresor, l'ultime épreuve de Fort Boyard!"
          "\nLes règles sont simples, plusieurs indices vous seront proposés et vous devrez trouve le mot qui s'y rapporte."
          "\n\nAttention!\nAprès trois erreurs consécutives, vous aurez perdu\nBonne Chance !")

    #Sélectionner aléatoirement une année et une émission
    fort_boyard = jeu_tv["Fort Boyard"]
    annee = random.choice(list(fort_boyard.keys()))
    emission = random.choice(list(fort_boyard[annee].values()))

    #Extraire les indices et le mot-code pour l'émission sélectionnée
    indices = emission["Indices"]
    mot_code = emission["MOT-CODE"]

    print("Indices:", ", ".join(indices[:3]))

    essais = 3
    reponse_correcte = False
    j = 3 #compteur pour les indices supplémentaires

    while essais > 0:
        reponse_joueur = input("Saisir la réponse : ").lower()

        if reponse_joueur == mot_code.lower():
            reponse_correcte = True
            essais = 0
        else:
            essais -= 1
            if essais > 0 and j < len(indices):
                print(f"Il vous reste {essais} essais")
                print(f"Le prochain indice est : {indices[j]}")
                j += 1

        #Affiche si il a gagné ou perdu
    if reponse_correcte:
        print("Vous avez gagné !")
        return True
    else:
        print(f"Vous avez perdu, la réponse était {mot_code} !")
        return False

#print(salle_De_Tresor())