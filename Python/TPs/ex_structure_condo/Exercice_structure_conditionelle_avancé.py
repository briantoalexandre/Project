# ------------------------- EXERCICE 01 --------------------------------------------
# Exercice Python : Gestion de données pour une entreprise tech

# CONTEXTE :
# La société TechNova gère une liste de produits technologiques avec leurs prix et leur disponibilité.
# Vous allez manipuler ces données à travers plusieurs parties, en utilisant des variables, des listes et des conditions.

# PARTIE 1 : Initialisation des données
# On dispose de trois listes : noms des produits, prix, et disponibilité (True = en stock, False = rupture).

# produits: "Clavier sans fil", "Souris ergonomique", "Écran 27 pouces", "Webcam HD"
# prix : 49.99, 35.50, 229.90, 59.99
# disponibilite

# PARTIE 2 : Affichage d'informations sur un produit donné
# Choisissez un produit (par son indice) et affichez son nom, son prix et sa disponibilité.

# On choisit la souris ergonomique

# PARTIE 3 : Vérification d'un panier client
# Un client souhaite acheter un écran et une webcam.
# Vérifiez si les deux produits sont disponibles et affichez le montant total si c'est possible.


# PARTIE 4 : Application d'une remise spéciale
# Si le prix total du panier dépasse 250 euros, appliquez une remise de 10% et affichez le nouveau montant.
from random import choice as c
randomness = ["stock", "rupture"]

products = ["Clavier sans fil", "Souris ergonomique", "Écran 27 pouces", "Webcam HD"]
prices = [49.99, 35.50, 229.90, 59.99]
availability = [c(randomness), c(randomness), c(randomness), c(randomness)]
article = [products, prices, availability]
ziparticle = list(zip(*article))

_v = "le produit {0[0]} coûte {0[1]} € et est en {0[2]}\nle produit {1[0]} coûte {1[1]} € et est en {1[2]}\nle produit {2[0]} coûte {2[1]} € et est en {2[2]}\nle produit {3[0]} coûte {3[1]} € et est en {3[2]}\n".format(*ziparticle)
shop = "\n".join(obj+f"({i})".zfill(71-len(obj)-3).replace("0", " ") if i<5 else "" for obj, i in zip(_v.split("\n"), range(1, len(_v)+1)))
print(shop)
finite = [1]

print((lambda cart=[int(input("Choisissé un ou plusieurs article : ")) for i in range(4)], cost=[]: ([cost.append(ziparticle[index-1][1]) for index in cart], f"cout total : {sum(cost)*0.9 if sum(cost)>250 else sum(cost)} €")[1])())


# ----------------------------- EXERCICE 02 -----------------------------------------
# Exercice Python : Gestion d'une bibliothèque en ligne (version sans boucles ni fonctions)

# CONTEXTE :
# La bibliothèque BookWorld souhaite gérer ses livres, leurs auteurs, leur disponibilité et permettre aux clients d'emprunter ou de rendre des livres.
# Vous allez manipuler des listes, des dictionnaires et des conditions, mais sans utiliser de boucles ni de fonctions.

# PARTIE 1 : Initialisation des données
# "1984", "Le Petit Prince", "Python pour les Nuls", "L'Étranger", "Le Seigneur des Anneaux"
# "George Orwell", "Antoine de Saint-Exupéry", "John Paul Mueller", "Albert Camus", "J.R.R. Tolkien"
# disponibilite des livres

# PARTIE 2 : Affichage de tous les livres disponibles (sans boucle)


# PARTIE 3 : Emprunt d'un livre par un client


# PARTIE 4 : Retour d'un livre


# PARTIE 5 : Affichage du catalogue complet avec statut (sans boucle)


# PARTIE 6 : Recherche de livres par auteur (exemple avec "George Orwell")


# PARTIE 7 : Statistiques (sans boucle)


