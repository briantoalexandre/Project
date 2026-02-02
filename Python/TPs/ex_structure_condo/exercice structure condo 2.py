#Exercice 1
"""
dividende = int(input("dividende : "))
diviseur = int(input("diviseur : "))

try:
    if dividende%diviseur == 0:
        print(f"{dividende} est divisible par {diviseur}.")
    else:
        print(f"{dividende} n'est divisible par {diviseur}.")
except ZeroDivisionError:
    print("Erreur : division par zéro impossible")
"""

#Exercice 2
"""
n_eleve = int(input("Nombre d'eleve : "))
duree = int(input("Durée du voyage en jours : "))
nourriture = 3.5 * n_eleve * duree

if 0<n_eleve<= 25:
    transport = 110*n_eleve
else:
    transport = 100*n_eleve

if 1<n_eleve < 20:
    hebergement = 4.2*duree*n_eleve
elif 20<n_eleve<35:
    hebergement = 3.8*duree*n_eleve
else:
    hebergement = 4*duree*n_eleve

total = [transport, nourriture, hebergement]
print(f"Le prix du voyage revient à {sum(total)/n_eleve} euros à par élève")
"""
#Exercice 3
"""
n_seance = int(input("Nombre de séances : "))
tarif_a = 145+ 10.5*n_seance
tarif_b = 15.5*n_seance
if tarif_a<tarif_b:
    print(f"Pour {n_seance} séances, le tarif A est le plus avantageux.")
elif tarif_a==tarif_b:
    print(f"Pour {n_seance} séances, aucun tarif n'est plus avantageux que l'autre.")
else:
    print(f"Pour {n_seance} séances, le tarif B est le plus avantageux.")

if input("Souhaitez-vous plus de détails? (yes/no) : ").upper() == "YES":
    print(f"Tarif A : {tarif_a} euros\nTarif B : {tarif_b} euros")
else:
    None
"""

#Exercice 4
"""
side1 = int(input("Premier coté :"))
side2 = int(input("Deuxième coté :"))
side3 = int(input("Troisième coté :"))

if side1+side2>side3:
    print("triangle non valide")
elif side1==side2==side3:
    print("C\'est  un triangle equilateral")
elif side1!=side2!=side3:
    print("C\'est un triangle scalène")
elif side1==side2 or side2==side3 or side1==side3:
    print("C\'est isocèle")
else:
    print("erreur")
"""

#Exercice 5
"""
reduction = 0
match input("client fidèle (1)\nnouveau client (2)\nautre (laisser vide)\n"):
    case "fidèle":
        reduction+=10
    cas:
        reduction+e "nouveau"=5
    case _:
        reduction=0

n_prix = int(input("montant du panier : "))
solde = str(input("solde? (oui ou non) : "))

if solde == "oui":
    reduction+=20

if n_prix<100:
    None
elif 100<=n_prix<=250:
    reduction+=5
elif 250<n_prix:
    reduction+=15

if n_prix<150:
    n_prix+=10

total = n_prix-(n_prix*(reduction/100))
if total<150:
    total+=10

print(f"le prix total est à {total} euros")
"""

