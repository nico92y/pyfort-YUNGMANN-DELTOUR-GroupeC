def introduction():
    print("Bienvenue dans Fort-Boyard !\n"
          "Pour réussir ce jeu, vous devrez accomplir au moins 3 épreuves qui vous seront proposés.\n"
          "Lorsque vous réussissez un jeu, vous gagnez une clé! 3 clés permettent d'accéder à la salle du trésor.\n"
          "Bonne chance !")
#print(introduction())

def composer_equipe():
    liste = []
    c=0
    nombre_joueurs = int(input("Rentrez le nombre de joueurs dans votre équipe : "))
    while nombre_joueurs > 3:
        print("Vos équipe doit être composé de 3joueurs maximum.")
        nombre_joueurs = int(input("Rentrez le nombre de joueurs dans votre équipe : "))

    #Collecte des informations des joueurs
    for i in range(nombre_joueurs):
        nom = input(f"Rentrez le nom du joueur {i+1} : ")
        profession = input(f"Rentrez la profession du joueur {i+1} : ")
        leader = input(f"Est-ce que le joueur {i+1} est le leader (Ecrivez sans faute soit 'Oui' soit 'Non'): ")
        joueur ={"nom": nom, "profession": profession, "leader": leader, "cles_gagnees": 0}
        liste.append(joueur)

    #si aucun leader n'a été défini
    for joueur in liste:
        if joueur["leader"] != 'Oui' and joueur["leader"] != 'Non':
            joueur["leader"] = 'Non'
            c += 1 #incrémenter le compteur si le joueur n'est pas leader
    if c == nombre_joueurs:  #Aucun leader défini
        print("Aucun leader désigné, le joueur 1 sera automatiquement défini comme leader.")
        liste[0]["leader"] = 'Oui'
    return liste
#print(composer_equipe())


def menu_epreuves():
    print("Choisissez le numéro de l'épreuve que vous voulez choisir")
    numero = input("1. Épreuve de Mathématiques\n2. Épreuve de Logique\n3. Épreuve du hasard\n4. Énigme du Père Fouras\nChoix: ")
    while not numero.isdigit():
        print("Veuillez entrer un nombre valide entre 1 et 4.")
        numero = input("1. Épreuve de Mathématiques\n2. Épreuve de Logique\n3. Épreuve du hasard\n4. Énigme du Père Fouras\nChoix: ")
    numero = int(numero)
    return numero
#print(menu_epreuves())

def choisir_joueur(equipe):
    index = 1
    for personne in equipe:
        # Garder le statut "Leader" ou "Membre" sans le modifier à chaque appel
        print(f"{index}. {personne['nom']} ({personne['profession']}) - {'Leader' if personne['leader'] == 'Oui' else 'Membre'}")
        index += 1

    if index == 2:  # Si une seule personne dans l'équipe
        return 1
    num = int(input("Entrez le numéro du joueur: "))

    # Vérification de la validité du choix
    while num >= index or num < 1:
        print("Rentrez une valeur entre 1 et ", index-1)
        num = int(input("Entrez le numéro du joueur: "))
    return num
#print(choisir_joueur([{'nom': 'Nico Yungmann', 'profession': 'prof', 'leader': 'Non', 'cles_gagnees': 0},{'nom': 'Thomas Deltour', 'profession': 'élève', 'leader': 'Oui', 'cles_gagnees': 0}]))

def enregistrer_historique(epreuve, joueur, result, cle, historique_file='output/historique.txt'):
    with open(historique_file, 'a') as fichier:
        # Structure les données de manière lisible et claire
        fichier.write(f'-------------------------------\n')
        fichier.write(f'Nom de l\'épreuve: {epreuve}\n')
        fichier.write(f'Joueur: {joueur["nom"]} - Profession: {joueur["profession"]} - Leader: {joueur["leader"]}\n')
        fichier.write(f'Résultat: {"Gagné" if result else "Perdu"}\n')
        fichier.write(f'Clés obtenues: {cle} clé(s)\n')
        fichier.write(f'-------------------------------\n\n')
    print(f"Historique enregistré pour {joueur['nom']} dans l'épreuve {epreuve}.")