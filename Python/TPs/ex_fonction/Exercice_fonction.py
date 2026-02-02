#Exercice TP 04 Fonctions


#ex 1
def ma_fonction():
    return "Hello World!"
#print(ma_fonction())

#ex 2
def dire_bonjour(nom : str):
    return f"Bonjour {nom}!"
#print(dire_bonjour("Alexandre"))

#ex 3
def min_max(obj : list):
    return min(obj), max(obj)
#print(min_max(["pomme", "banane", "abricot", "orange"]))

#ex 4
def somme(x, y):
    return x+y
#print(somme(5, 7)) # 12
#print(somme("cinq", "deux")) # cinqdeux

#
def examen(fr : float, math : float, ang : float, info : float):
    coefficients = (1,2,2,3)
    notes = (fr, math, ang, info)
    moyenne = sum((lambda x=[]: ([x.append(note*coefficient) for coefficient, note in zip(coefficients, notes)], x)[-1])())/sum(coefficients)

    yield moyenne
    if moyenne < 8:
        yield "Refusé"
        yield ""
    elif moyenne < 10:
        yield "Rattrapage"
        yield ""
    else:
        if 10<=moyenne<12:
            yield "Admis"
            yield "Passable"
        elif 12<=moyenne<14:
            yield "Admis"
            yield "Assez bien"
        elif 14<=moyenne<16:
            yield "Admis"
            yield "Bien"
        elif 16<=moyenne<18:
            yield "Admis"
            yield "Très bien"
        elif 18<=moyenne:
            yield "Admis"
            yield "Félicitation du jury"


print(*list(examen(10,10.5,12,10)))

#print(examen(1,2,3,4))             [2.75, 'Refusé']
#print(examen(7,8,9,10))            [8.75, 'Rattrapage']
#print(examen(10,11.5,12,10))       [10.6875, 'Admis', 'Passable']
#print(examen(10,12,13,14))         [12.5, 'Admis', 'Mention Assez Bien']
#print(examen(18.5,13,15.5,16))     [16.125, 'Admis', 'Mention Très Bien']
#print(examen(19,18.5,19.5,20))     [19.4375, 'Admis', 'Mention Félicitations du jury'
