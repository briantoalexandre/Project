#<>
# Vous pouvez choisir un exercice avec un nombre allant de 1 à 9
class Exercice():
    def __init__(self):
        pass

    def Pin_Code(self, code : int):
        Marc_code = 4567
        return (lambda : "code correct" if code == Marc_code else "code incorrect")()
        
    def Signe(self, num : int): #d'un nombre
        return (lambda : "Negatif" if num  < 0 else "positif" if num > 0 else "Nul")()
        
    #Parité
    def Parite(self, num : int):
        return (lambda : f"{num} est pair" if num%2 == 0 else f"{num} est impair")() 

    #Age
    def Age(self, age : int):
        return (lambda : f"A {age} ans, vous etes un enfant" if 6<=age<12 else f"A {age} ans, vous etes un adolescent" if 12<=age<18 else f"A {age} ans, vous etes un adulte" if 18<=age else f"A {age} ans (?), vous etes soit mort, n'exister pas encore ou analphabète" )()
        
    def Perte_ou_profit(self, manu_pri : float, sell_pri : float):
        return (lambda : f"perte de {int((sell_pri-manu_pri)/-1) if ((sell_pri-manu_pri)/-1).is_integer() else (sell_pri-manu_pri)/-1} €" if sell_pri-manu_pri<0 else f"profit de {int(sell_pri-manu_pri) if (sell_pri-manu_pri).is_integer() else sell_pri-manu_pri} €" if sell_pri-manu_pri>=0 else None)()

    #Maximum
    def Maximum(self, f_num : float, s_num : float, t_num : float): #first number, second number, third number
        return (lambda x=list() : (x.extend([f_num, s_num, t_num]) ,f"Le max est le premier nombre {int(f_num) if f_num.is_integer() else f_num}" if x[0] == max(x) else f"Le max est le second nombre {int(s_num) if s_num.is_integer() else s_num}" if x[1] == max(x) else f"Le max est le troisieme nombre {int(t_num) if t_num.is_integer() else t_num}" if x[2] == max(x) else "IndexError")[1])()

    #Triangle rectangle
    def Triangle_rectangle(self, s_1 : float, s_2 : float, s_3 : float):
        return (lambda : "Erreur, ordre pas respecté" if not s_1<s_2<s_3 else "Triangle rectangle" if s_1**2+s_2**2 == s_3**2 else "Triangle non rectangle" if s_1**2+s_2 != s_3**2 else "Autre erreur")()

    #annee bissextile
    def Annee_bissextile(self, annee : int):
        return (lambda x=annee : f"{x} est une année bissextile" if (x/4-int(x/4)) == 0.0 and (x/100-int(x/100)) != 0.0 or (x/4-int(x/4)) == 0.0 and (x/400-int(x/400)) == 0.0 else f"{x} n'est pas une année bissextile")()

    #Société de transport
    def Societe_de_transport(self, age : int):
        return (lambda tarif=10, : f"tarif à {int(tarif*0.0)} €" if age<=5 else f"tarif à {int(tarif*0.5)} €" if 5<age<16 else f"tarif à {int(tarif*0.6)} €" if 16<=age<=21 else f"tarif à {int(tarif*1)} €" if 21<age<51 else f"tarif à {int(tarif*0.9)} €" if 51<=age else None)()

ex = Exercice()
print(ex.Societe_de_transport(62))