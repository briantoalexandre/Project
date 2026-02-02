''' TP6 Python : Les boucles '''


''' Exercice 1 
La fonction serie() prend comme argument un nombre entier n et renvoie un tuple contenant tous les nombres entiers allant de 1 à n.  
'''
# en utilisant une boucle for
def serie(n:int) -> tuple:
    res = []
    for i in range(1, n+1):
        res.append(i)
    res = tuple(res)
    return res
# print(serie(5))

# en utilisant une boucle while (pas de tuple en retour)
def serie(n:int):
    a=1
    while a<=n:
        print(a, end=" ")
        a=a+1
# serie(5)

# en utilisant uniquement les fonctions tuple() et range()
def serie(n : int) -> tuple :
    return tuple(range(1, n+1))
# print(serie(5))



''' Exercice 2 
La fonction serie-inverse() prend comme argument un nombre entier n et renvoie un tuple contenant tous les nombres entiers allant de n à 1.
'''
# en utilisant une boucle for
def serie_inverse(n:int) -> tuple:
    res = []
    for i in range(1, n+1):
        res.append(i)
        res.sort(reverse=True) 
    res = tuple(res)
    return res
# print(serie_inverse(5))

# en utilisant une boucle while (pas de tuple en retour)
def serie_inverse(n:int):
    while n>=1:
        print(n, end=" ")
        n=n-1
# serie_inverse(5)

# en utilisant uniquement les fonctions tuple() et range()
def serie_inverse(n : int) -> tuple :
    return tuple(range(n, 0, -1))
# print(serie_inverse(5))



''' Exercice 3
La fonction somme() prend comme argument un nombre entier n et renvoie la somme des nombres entiers allant de 1 à n.
'''
# en utilisant une boucle for
def somme(n : int) -> int :
    s = 0
    for i in range(1, n+1):
        s += i       # s = s + i
    return s
# print(somme(5))

# en utilisant une boucle while
def somme(n:int) -> int:
    a=1
    s=0
    while a<=n:
        s=s+a
        a=a+1
    return s
# print(somme(5))

# en utilisant uniquement les fonctions sum() et range()
def somme(n:int) -> int:
    return sum(range(1, n+1))
# print(somme(5))



''' Exercice 4
La fonction somme_cube() prend comme argument un entier n et renvoie la somme des nombres entiers au cube allant de 1 à n.
'''
# en utilisant une boucle for
def somme_cube(n : int) -> int :
    s = 0
    for i in range(1, n+1):
        s += i**3
    return s
print("somme_cube(5) :", somme_cube(5))

# en utilisant une boucle while
def somme_cube(n:int) -> int:
    a=1
    s=0
    while a<=n:
        s=s+a**3
        a=a+1
    return s
print("somme_cube(5) :", somme_cube(5))

# en utilisant sum() et range()
def somme_cube(n: int) -> int:
    return sum(i**3 for i in range(1, n+1))
print("somme_cube(5) :", somme_cube(5))



''' Exercice 5
La fonction produit() prend comme argument un entier n et renvoie la factorielle de n.
'''
# en utilisant une boucle for
def produit(n:int) -> int:
    p = 1
    for i in range(1, n+1):
        p *= i       # p = p * i
    return p
print("produit(5) :", produit(5))

# en utilisant une boucle while
def produit(n:int) -> int:
    a=1
    p=1
    while a<=n:
        p=p*a
        a=a+1
    return p
print("produit(5) :", produit(5))



''' Exercice 6
La fonction produit_pair() prend comme argument un nombre entier n et renvoie le produit de tous les nombres entiers pairs compris entre 1 et n. 
'''
# en utilisant une boucle for et la fonction range()
def produit_pair(n:int) -> int:
    p = 1
    for i in range(2, n+1, 2):
        p *= i       # p = p * i
    return p
print("produit_pair(5) :", produit_pair(5))

# en utilisant une boucle for et une structure conditionnelle (if)
def produit_pair(n:int) -> int:
    p = 1
    for i in range(1, n+1):
        if i%2 == 0:
            p *= i       # p = p * i
    return p
print("produit_pair(5) :", produit_pair(5))

# en utilisant une boucle while et une structure conditionnelle (if)
def produit_pair(n: int) -> int:
    a=1
    res=1
    while a<=n:
        if a%2==0:
            res=res*a
        a=a+1
    print(res)
print("produit_pair(5) :")
produit_pair(5)
