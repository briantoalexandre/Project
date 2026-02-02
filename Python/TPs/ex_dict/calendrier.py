def afficher_mois(mois):
    return ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"][mois-1]

def est_bissextile(annee):
     return True if (annee%4==0 and annee%100!=0) or annee%400==0 else False

def nb_de_jours(mois, annee):
    if mois == 2:
        if est_bissextile(annee):
            return 29
        else:
            return 28
    elif mois in [4, 6, 9, 11]:
        return 30
    elif mois in [1, 3, 5, 7, 8, 10, 12]:
        return 31

def premier_jour_mois(mois, annee):
    if mois in [1, 2]:
        mois+=12
        annee-=1
    k = annee%100
    j = annee//100
    return (1 + (13 * (mois + 1)) // 5 + k + k // 4 + j // 4 - 2 * j) % 7

def afficher_calendrier(mois : int, annee : int):
    jours_semaine = ["Lun","Mar","Mer","Jeu","Ven","Sam","Dim"]
    total_jours = nb_de_jours(mois, annee)
    premier_jour = premier_jour_mois(mois, annee)
    pj = [5, 6, 0, 1, 2, 3, 4]
    #print(f"{afficher_mois(mois)} {annee}")
    """
    for k in range(pj[premier_jour]):
        print("     ", end="")
    for i in range(1, total_jours+1):
        print(f"{i:>3}  ", end="" if i not in tuple(range(7-pj[premier_jour], 31, 7)) else "\n")
    print()
    """
    return afficher_mois(mois)+"\n"+"  ".join(jours_semaine)+"\n"+"     "*(pj[premier_jour])+ "".join([f"{i:>3}  {"" if i not in tuple(range(7-pj[premier_jour], 31, 7)) else "\n"}" for i in range(1, total_jours+1)])

def afficher_calendrier_annee(annee):
    calendrier = [afficher_calendrier(mois, annee).splitlines() for mois in range(1, 13)]
    s = 5
    for j in range(0, 12+s, s):
        print(*["".join([f"{k:<{37}}" for k in i]) for i in zip(*calendrier[j-s:j])], sep="\n")

afficher_calendrier_annee(2024)