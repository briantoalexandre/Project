print("\"Non\" est un message d\'erreur")

class bibliotheque():
    def __init__(self):
        self.livre1 = self.creer_livre("etranger","Camus","1942")
        self.livre2 = self.creer_livre("Paroles","Prevert","1946")
        self.livre3 = self.creer_livre("Alcools","Apollinaire","1913")
        self.bibliotheque = [self.livre1, self.livre2, self.livre3]

        self.actions_bibliotheque()

    def creer_livre(self, titre : str, auteur : str, anne : str):
        return [titre, auteur, anne]

    def ajouter_livre(self, bl : list[list], livre : list):
        bl.append(livre)

    def afficher_livre(self, livre : list):
        print("Titre : <{0}>, Auteur : <{1}>, Année : <{2}>".format(*livre))

    def afficher_bibliotheque(self, bl : list[list]):
        for obj in bl:
            self.afficher_livre(obj)

    def rechercher_par_titre(self, bl : list[list], titre : str):
        for obj in bl:
            if titre == obj[0]:
                self.afficher_livre(obj)
            
    def supprimer_par_titre(self, bl : list[list], titre : str):
        for obj in bl:
            if titre == obj[0]:
                bl.pop(bl.index(obj))

    def modifier_un_livre(self, bl : list[list], titre : str, champ : str, n_valeur : str):
        for obj in bl:
            if obj[0] == titre:
                if champ == "titre":
                    obj[0] = n_valeur
                elif champ == "auteur":
                    obj[1] = n_valeur
                elif champ == "annee":
                    obj[2] = n_valeur

    def compter_livres_par_auteur(self, bl : list[list], auteur : str):
        for obj in bl:
            if obj[1].title() == auteur.title():
                self.afficher_livre(obj)

    def lister_auteurs(self, bl):
        auteurs = set()
        for obj in bl:
            auteurs.add(obj[1])
        print(list(auteurs))

    def nombre_total_de_livre(self, bl : list[list]):
        print(len(bl))

    def trier_bibliotheque(self, bl : list[list], critere : str):
        def ordre(eph_bl):
            if critere == "titre":
                for auteurs in list(sorted(list(zip(*bl))[0])):
                    for livres in eph_bl:
                        if auteurs in livres:
                            yield livres
                            eph_bl.remove(livres)
            if critere == "auteur":
                for auteurs in list(sorted(list(zip(*bl))[1])):
                    for livres in eph_bl:
                        if auteurs in livres:
                            yield livres
                            eph_bl.remove(livres)
            if critere == "annee":
                for auteurs in list(sorted(list(zip(*bl))[2])):
                    for livres in eph_bl:
                        if auteurs in livres:
                            yield livres
                            eph_bl.remove(livres)
        bl.extend(list(ordre(bl)))

    def liste_actions_bibliotheque(self):
        choix = int(input(f"Afficher le contenu de la bibliothèque (0)\nModifier la bibliothèque (1)\nRechercher un livre (2)\n : "))
        if choix == 0:
            self.afficher_bibliotheque(self.bibliotheque)
        elif choix == 1:
            self.modifier_bibliotheque(self.bibliotheque)
        elif choix == 2:
            self.rechercher_livre_utilisateur(self.bibliotheque)
        else:
            print("Non")

    def  afficher_contenu_bibliotheque(self, bl):
        choix = int(input(f"Nombre de livres (0)\nTrier la bibliothèque (1)\nLister les auteurs (2)\n : "))
        if choix == 0:
            self.nombre_total_de_livre(bl)
        elif choix == 1:
            choix2 = int(input(f"par titre (0) auteur (1) ou annee (2): "))
            if choix2 == 0:
                self.trier_bibliotheque(bl, "titre")
            elif choix2 == 1:
                self.trier_bibliotheque(bl, "auteur")
            elif choix2 == 2:
                self.trier_bibliotheque(bl,"annee")
            else:
                print("Non")
        elif choix == 2:
                self.lister_auteurs(bl)
        else:
            print("Non")

    def modifier_bibliotheque(self, bl):
        choix = int(input(f"Ajouter un livre (0)\nSupprimer un livre par son titre (1)\nModifier un livre (2)\n : "))
        if choix == 0:
            titre = input("titre : ")
            auteur = input("auteur : ")
            annee = input("annee : ")
            self.ajouter_livre(bl, creer_livre(titre, auteur, annee))
        elif choix == 1:
            titre = input("titre : ")
            self.supprimer_par_titre(bl, titre)
        elif choix == 2:
            titre = input("titre : ")
            champ = input("champ à modifier : ")
            n_valeur = input("nouvel valeur : ")
            self.modifier_un_livre(bl, titre, champ, n_valeur)
        else:
            print("Non")

    def rechercher_livre_utilisateur(self, bl):
        choix = int(input(f"rechercher par titre (0)\nAfficher les livres d'un auteur (1)\n : "))
        if choix == 0:
            titre = input("titre : ")
            self.rechercher_par_titre(bl, titre)
        elif choix == 1:
            auteur = input("auteur : ")
            self.compter_livres_par_auteur(bl, auteur)
        else:
            print("Non")

    def actions_bibliotheque(self):
        while True:
            self.liste_actions_bibliotheque()
            print()


bibliotheque1 = bibliotheque()

