#Exercices : les boucles

from math import sqrt as s
from random import randint as r

LF = "\n" #LF stand for Line Feed

#Exercice 1 :

Exercice1 = """
def serie(n : int):
    for i in range(1, n+1):
        yield i

def serie2(n : int):
    i = 1
    while i < n+1:
        yield i
        i += 1

def serie3(n : int):
    return tuple(range(1, n+1))

print(tuple(serie(5)))
print(*serie2(5))
print(tuple(serie3(5)))
"""

#Exercice 2 :

Exercice2 = """
def serie(n : int):
    for i in range(n, 0, -1):
        yield i

def serie2(n : int):
    i = n
    while i > 0:
        yield i
        i-=1

def serie3(n : int):
    return tuple(range(n, 0, -1))

print(tuple(serie(5)))
print(*serie2(5))
print(tuple(serie3(5)))
"""

#Exercice 3 :

Exercice3 = """
def somme(n : int):
    for i in range(1, n):
        yield i

def somme2(n : int):
    i = 1
    while i < n:
        yield i
        i+=1 

def somme3(n : int):
    return sum(range(1, n))

print(sum(somme(3)),sum(somme(5)),sum(somme(14)))
print(sum(somme2(3)),sum(somme2(5)),sum(somme2(14)))
print(somme3(3),somme3(5),somme3(14))
"""

#Exercice 4 :

Exercice4 = """
def somme_cube(n : int):
    for i in range(1, n+1):
        yield i**3

def somme_cube2(n : int):
    i = 1
    while i < n+1:
        yield i**3
        i+=1

print(sum(somme_cube(3)))
print(sum(somme_cube2(14)))
"""

#Exercice 5 :

Exercice5 = """
def produit(n : int):
    k = 1
    for i in range(1, n):
        k+=k*i
    return k 

def produit2(n : int):
    k = 1
    i = 0
    for i in range(1, n):
        k+=k*i
    return k


print(produit(5))
print(produit2(14))
"""

#Exercice 6 :

Exercice6 = """
def produit_pair(n : int):
    k = 1
    for i in range(1, n, 2):
        k+= k*i
    return k

def produit_pair2(n : int):
    k = 1
    for i in range(1, n):
        if i%2!=0:
            k+= k*i
    return k

def produit_pair3(n : int):
    k = 1
    i = 1
    while i < n:
        if i%2!=0:
            k+= k*i
        i+=1
    return k

print(produit_pair(3))
print(produit_pair2(5))
print(produit_pair3(14))
"""


#Exercice 7 :

Exercice7 = """
def inverse(n : int):
    return sum([(1/i) if i%2!=0 else -(1/i) for i in range(1, n+1)])

print(inverse(3))
print(inverse(5))
print(inverse(14))
"""

#Exercice 8 :

Exercice8 = """
def liste_parite(n : list):
    return (lambda x =([],[]) : ([x[0].append(obj) if obj%2 ==0 else x[1].append(obj) for obj in n], x)[-1])()


print(liste_parite([6, 5, 8, 1, 3, 4, 7, 2]))
"""

#Exercice 9 :

Exercice9 = """
def occurence(n : list):
    print(n)
    bl = []
    rl = []
    for value in n:
        if value in bl:
            continue
        for item in n:
            if item == value:
                rl.append(1)
        yield value, sum(list(rl))
        rl.clear()
        bl.append(value)

print(list(sorted(occurence([6, 5, 8, 6, 2, 7, 6, 5, 2]))))
"""

#Exercice 10 :

Exercice10="""
def del_occurence(n : list):
    return (lambda n=list(reversed(n)): ([n.remove(obj) if n.count(obj) > 1 else "" for obj in n],list(reversed(n)))[-1])()

print(del_occurence([ 6, 5, 8, 6, 2, 7, 6, 5, 2 ]))
"""

#Exercice 11 :

Exercice11 = """
def premier(n : int):
    limit = s(n)
    if n > 1:
        for i in range(2, int(limit)+10):
            if (n/i).is_integer() and (n in  [4, 6, 8, 9] or n not in [2, 3, 5, 7]):
                return f"{n} n'est pas un nombre premier"

        else:
            return f"{n} est un nombre premier"
    else:
        return "n doit être strictement superieur à 1"

print(premier(37))
print(premier(357))
"""

#Exercice 12 :

Exercice12 = """
def premier(n : int):
    limit = s(n)
    if n > 1:
        for i in range(2, int(limit)+10):
            if (n/i).is_integer() and (n in  [4, 6, 8, 9] or n not in [2, 3, 5, 7]):
                return  False

        else:
            return True
    else:
        return False

def premier_jumeau(n : int):
    for i in range(n):
        if premier(i): #seek out the first prime number
            for k in range(i+1, n):
                if premier(k): #seek out the second prime number
                    if k-i == 2: #do the math
                        yield i, k

print(tuple(premier_jumeau(33)))
"""

#Exercice 13 :


Exercice13 = """
def tirage(n : int):
    tries = 0
    while True:
        if r(1, 100) == n:
            break
        tries+=1
    return tries

print(tirage(36))
"""

#Exercice 14 :

Exercice14 = """
def table_multiplication(n : int):
    return [f"{n} * {i} = {n*i}" for i in range(1, 11)]

print(*table_multiplication(6), sep=LF)
"""

#Exercice 15 :

Exercice15 = """
def triangle():
    return [f"O"*i for i in range(1, 10)]

def triangle2():
    return [f"{i}"*(10-i) for i in range(0, 11)]

def pillier(n : int):
    a = "  |  |  "
    b = "--------"
    for i in range(n):
        print(a)
        if i < n-1:
            print(b)

print(*triangle(), LF, sep=LF)
print(*triangle2(), sep=LF)
pillier(5)
"""

#Exercice 16 :

Exercice16 = """
def sapin(n : int):
    return [" "*((n+(1 if i == 1 else 0))-i)+ "*"*i + "*"*(i-1) + LF for i in range(1, n+1)]+[" "*(n-2)+"|"*3 + LF for i in range(2)]

print(*sapin(9))
"""