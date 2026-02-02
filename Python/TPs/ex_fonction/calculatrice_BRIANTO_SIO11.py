# Calculatrice Brianto Alexandre

from math import sqrt

def addition(a : float, b : float):
    return f"{a} + {b}  = {a+b}" #addition de a plus b
def soustraction(a : float, b : float):
    return f"{a} - {b}  = {a-b}" #soustraction de a moins b
def multiplication(a : float, b : float):
    return f"{a} * {b}  = {a*b}" #multipication de a fois b
def division(a : float, b : float):
    try: #gestion de l'erreur de division par zero
        return f"{a} / {b}  = {a/b}" #division de a par b
    except ZeroDivisionError: 
        return "Division par zero impossible"
def puissance(a : float, b : float): #puissance de a par b
    return f"{a} ^ {b}  = {a**b}"
def racine_carree(a : float): #racine carre de a
    try:
        return f"La racine carré de {a} = {sqrt(a)}"
    except ValueError:
        return f"Erreur {a} est négatif"
def modulo(a : float, b : float): #modulo de a par b
    return f"{a} % {b}  = {a%b}"

def est_pair(a : int):
    if not bool(a % 2):
        return f"{a} est pair"
    else:
        return f"{a} est impair"
    
def calculer_mediane(n : list):
    n.sort()
    if len(n) % 2 == 0:
        return f"la mediane de cette liste {", ".join(map(str,n))} est {(n[len(n)//2-1] +n[len(n)//2]) / 2}"
    else:
        return f"la mediane de cette liste {", ".join(map(str,n))} est {n[len(n)//2]}"

def afficher_parite():
    valeur = int(input("Entrez un nombre entier : "))
    return est_pair(valeur)
    
def calculer(calcul : str):
    if "+" in calcul: #structure conditionelle pour choisir le calcule
        return addition(*map(float, calcul.split("+")))
    elif "-" in calcul:
        return soustraction(*map(float, calcul.split("-")))
    elif "*" in calcul:
        return multiplication(*map(float, calcul.split("*")))
    elif "/" in calcul:
        return division(*map(float, calcul.split("/")))
    elif "^" in calcul:
        return puissance(*map(float, calcul.split("^")))
    #elif "sqrt" in calcul:
    #    return racine_carree(*calcul.split("sqrt"))
    elif "%" in calcul:
        return modulo(*map(float, calcul.split("%")))
    else:
        return "erreur"
    
def demander_calcul():
    a = str(float(input("Entrez le premier nombre : ")))
    b = input("Entrez le second nombre : ")
    signe = input("Entrez l'opération (+, -, *, /, ^, sqrt, %) : ")
    return calculer(a+signe+b)

#print(demander_calcul())
#print(calculer("1 ^ 5"))
#print(afficher_parite())
print(calculer_mediane([6,2,3,4,6,12,4]))
