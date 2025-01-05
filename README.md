1) Presentation générale du projet :
   FORT BOYARD SIMULATOR
   Contributeurs : Thomas Deltour et Nicolas Yungmann, repartition des taches équitablement
   Description : Fort Boyard Simulator : Un jeu Python qui simule les épreuves de l'émission Fort Boyard.
                 Les joueurs résolvent des énigmes, collectent des clés et indices, puis devinent un mot-code pour accéder au trésor.
   Fonctionnalités Principales : Jeux de hasard : épreuves basées sur la chance.
                                 Jeux mathématiques : réflexion sur des problèmes numériques.
                                 Épreuves logiques : résolution de casse-têtes.
                                 Enigmes du Père Fouras : devinettes intellectuelles.
                                 Accès à la salle du trésor après réussite des épreuves.
   Technologies Utilisées : Le projet a été totalement réalisé en python, nous nous sommes servis des bibliothèques random et json,
                            et comme outils de l'application PyCharm.
   Installation : Clonage du dépôt Git
                  Clonez le dépôt sur votre machine locale
                  git clone <URL_DU_DEPOT>
                  cd pyfort-thomas-nicolas-C-main
                  Configuration de l'environnement
                  Assurez-vous d'avoir Python 3.8 ou une version supérieure installée.
                  Installez les dépendances requises (si applicable).
   utlisation : Exécution de l'application
                Exécutez simplement le fichier principal :
                python main.py
                Exemples d'utilisation
                Lancez une partie et choisissez une épreuve.
                Suivez les instructions affichées pour chaque épreuve et amusez vous !
   
   2) documentation technique:
      Algorithme du jeu : Pour l'algorithme nous avons d'abord :
                          Initialisation des variables (joueurs, score, clés).
                          Affichage des options pour les épreuves.
                          Choix aléatoire ou sélection de l’épreuve.
                          Résolution de l’épreuve par le joueur.
                          Calcul des résultats : clé gagnée ou perdue.
                          Répétition jusqu'à obtention des 3 clés.
                          Accès à la salle du trésor si obtention des 3 clés
      Détails des fonctions implémentées :
                          def enigme_pere_fouras(): Gère les énigmes et vérifie les réponses si elles sont bonnes ou mauvaises.
                          def epreuves_logiques(): Implémente les jeux logiques.
                          def epreuves_mathematiques(): Fournit des problèmes mathématiques avec 4 épreuves différentes
                          def fonctions_utiles(): Contient des fonctions auxiliaires comme le calcul des scores qui est très utile.
      Gestion des Entrées et Erreurs :
                          Validation des entrées utilisateur : vérifie les types et les plages de valeurs.
                          Gestion des exceptions : le programme n'affiche pas d'erreurs en cas d'entrées invalides
                          Liste des bugs connus : rien pour l'instant
      3. Journal de Bord :
  Chronologie du Projet : 
                          Alors Le 6 décembre nous nous sommes chacun attribuer les différentes épreuves.
                          Le 23 décembre nous avons fais un premier débriefing en appel. Et on a discuté des epreuves sur lesquels on a eu le plus de difficultés
                          et nous avons reussi à trouver les différentes solutions.
                          Et le 3 janvier nous avons tous mis en commun afin de tester les progammes de l'autre et nous étions très fiers de notre projet
Répartition des Tâches : nous avons divisés le projet de manière équitable :
                         thomas : mathématiques, logique, pere fourras
                         nicolas : hasar, utile, epreuve finale

         

   
   
   
