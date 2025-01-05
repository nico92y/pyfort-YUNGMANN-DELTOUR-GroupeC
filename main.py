import fonctions_utiles
import epreuve_finale
import epreuves_hasard
import epreuves_logiques
import epreuves_mathematiques
import enigme_pere_fouras

def jeu():
    fonctions_utiles.introduction()
    equipe = fonctions_utiles.composer_equipe()
    cle = 0

    while cle < 3:
        epreuve = fonctions_utiles.menu_epreuves()
        joueur_index = fonctions_utiles.choisir_joueur(equipe)
        joueur = equipe[joueur_index - 1]
        result = False
        if epreuve == 1:
            result = epreuves_mathematiques.epreuve_math()
        elif epreuve == 2:
            result = epreuves_logiques.jeu_bataille_navale()
        elif epreuve == 3:
            result = epreuves_hasard.epreuve_hasard()
        elif epreuve == 4:
            result = enigme_pere_fouras.enigme_pere_fouras()
        else:
            print("Vous avez rentrez une mauvaise valeur. Réessayez.")

        if result:
            cle += 1
            print(f"Bravo! Vous avez gagné une clé. Vous avez maintenant {cle} clés.")
        else:
            print("Dommage, vous n'avez pas gagné cette épreuve.")

    print("Félicitations! Vous avez obtenu 3 clés.")
    if epreuve_finale.salle_De_Tresor():
        print("L'équipe a gagné le jeu!")
    else:
        print("L'équipe a perdu le jeu.")
print(jeu())