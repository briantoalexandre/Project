#Exercice 6
"""
primes = [0,0,0]
salaire = int(input("salaire : "))
n_ventes = int(input("Nombre de ventes : "))
anciennete = int(input("ancienneté : "))
poste_cadre = bool(input("Poste de cadre (True/ False) : "))

if 100<n_ventes:
    primes[0] = (10/100)

if 5<=anciennete<=10:
    primes[1] = (5/100)

elif 10<anciennete:
    primes[1] = (10/100)


if poste_cadre is True:
    primes[2] = (5/100)

if salaire<2000:
    taxes=20
elif 2000<=salaire<5000:
    taxes=30
else:
    taxes=40

salaire_brut = salaire+(salaire*sum(primes))
montant_taxes = (salaire+(salaire*sum(primes)))*(taxes/100)
salaire_net = salaire_brut-montant_taxes

print("\nSalaire brut {} euros".format(salaire_brut))
print("montant des taxes {} euros".format(montant_taxes))
print("salaire net : {} euros".format(salaire_net))
"""

#Exercice 7
"""
mdp = str(input("Mot de passe : "))

if len(mdp) >= 8:
    None
else:
    print("Le mot de passe doit contenir au moins 8 caractères.")


found=0
for letter in list(chr(i) for i in range(65,91)):
    if letter in mdp:
        found=1
        break
    else:
        None
if found==0:
    print("Le mot de passe doit contenir au moins une majuscule.")
else:
    None

found=0
for number in list(chr(k) for k in range(48, 58)):
    if number in mdp:
        found=1
        break
    else:
        None

if found==0:
    print("Le mot de passe doit contenir au moins un nombre.")
else:
    None

for spec_characters in ("@","#","!","$","%","&","*"):
    if spec_characters in mdp:
        found=1
        break
    else:
        None

if found==0:
    print("Le mot de passe doit contenir au moins un caractère spécial.")
else:
    None
"""

#Exercice 8

revenu = 43200#int(input("Revenu : "))

if revenu<=10000:
    print("L'impot à payer est de 0 €")
elif 10001<=revenu<=25000:
    print(f"L'impot à payer est de {(revenu-10000)*(10/100)} €")
elif 25001<=revenu<=50000:
    print(f"L'impot à payer est de {(revenu-25000)*(15/100)} €")
elif revenu>50000:
    print(f"L'impot à payer est de {(revenu-50000)*(20/100)} €")