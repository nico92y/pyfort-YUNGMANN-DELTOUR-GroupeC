import random

def factorielle(n):
    a = 1
    for i in range(1,n+1):
        a = a * i
    return a

def epreuve_math_factorielle():
    n = random.randint(1,10)
    print("Épreuve de Mathématiques: Calculer la factorielle de",n,".")
    reponse = int(input("Votre réponse :"))
    if reponse == factorielle(n) :
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Echec ! La valeur etait :", factorielle(n))
        return False
#print(epreuve_math_factorielle())



def resoudre_equation_lineaire():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    x = -b / a
    return a, b, x

def epreuve_math_equation():
    a, b, solution = resoudre_equation_lineaire()
    print("Épreuve de Mathématiques: Résoudre l'équation", a, "x +", b, "= 0.")
    reponse = float(input("Quelle est la valeur de x: "))
    if abs(reponse - solution) < 0.0001:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Echec ! La valeur était :", solution)
        return False
#print(epreuve_math_equation())



def est_premier(n) :
  for i in range(2,n) :
    if (n%i) == 0 :
        return False
  return True

def premier_plus_proche(n):
    while not est_premier(n):
        n+=1
    return n

def epreuve_math_premier():
    n = random.randint(10, 20)
    print("Épreuve de Mathématiques: Trouver le nombre premier le plus proche de", n, ".")
    reponse = int(input("Votre réponse: "))
    correct_answer = premier_plus_proche(n)
    if reponse == correct_answer:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Echec ! La valeur etait :", correct_answer)
        return False
#print(epreuve_math_premier())




def epreuve_roulette_mathematique():
    nombres = [random.randint(1,20 ) for _ in range(5)]
    operation = random.choice(["addition", "soustraction", "multiplication",])

    if operation =="addition":
        resultat = sum(nombres)
    elif operation == "soustraction":
        resultat = nombres[0]
        for num in nombres[1:]:
            resultat -= num
    else:
        resultat = 1
        for num in nombres:
            resultat *= num
    print("Nombres sur la roulette :", nombres)
    print("Calculez le résultat en combinant ces nombres avec une", operation)
    reponse = float(input("Votre réponse :"))
    if reponse == resultat:
        print("Bonne réponse! Vous avez gagné une clé.")
        return True
    else:
        print("Echec !La valeur etait :",resultat)
        return False
#print(epreuve_roulette_mathematique())



def epreuve_math():
    epreuves = [epreuve_math_factorielle, epreuve_math_equation, epreuve_math_premier, epreuve_roulette_mathematique]
    epreuve = random.choice(epreuves)
    return epreuve()
#print(epreuve_math())