import random

def epreuve_math():
    epreuves = [epreuve_math_factorielle, resoudre_equation_lineaire, epreuve_math_premier]
    epreuve_choisie = random.choice(epreuves)
    epreuve_choisie()
#print(epreuve_math())

def factorielle(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def epreuve_math_factorielle():
    n = random.randint(1, 10)
    print("Épreuve de Mathématiques: Calculer la factorielle de",n,".")
    rep = int(input("Votre réponse: "))
    if rep == factorielle(n):
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Gros looser, la valeur était",factorielle(n))
        return False
#print(epreuve_math_factorielle())


def resoudre_equation_lineaire():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    x=-b/a
    print("Épreuve de Mathématiques: Résoudre l'équation ",a,"x +",b,"= 0.")
    rep = int(input("Quelle est la valeur de x: "))
    if rep == x:
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Gros looser la valeur était",x)
        return False
print(resoudre_equation_lineaire())

def est_premier(n) :
  for i in range(2,n) :
    if (n%i) == 0 :
        return False
  return True

def premier_plus_proche(n):
    while est_premier(n) != True:
        n+=1
    return n

def epreuve_math_premier():
    n = random.randint(10, 20)
    print("Épreuve de Mathématiques: Trouver le nombre premier le plus proche de", n,".")
    rep = int(input("Votre réponse: "))
    if rep == premier_plus_proche(n):
        print("Correct! Vous gagnez une clé.")
        return True
    else:
        print("Gros looser la valeur était", premier_plus_proche(n))
        return False
#print(epreuve_math_premier())

