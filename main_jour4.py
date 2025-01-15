#Job 01
from calendar import c


def My_print_hello():
    print("Hello world")

#Job 02:

def My_print_name(name):
    print(f"Voila la valeur de name : {name}")

def Add(a,b):
    print(a+b)

def GetHello():
    print("Hello la Plateforme")

def calcule(num1,operator,num2):
    if operator == "+":
        return num1+num2
    elif operator == "-":
        return num1-num2
    elif operator == "*":
        return num1*num2
    elif operator == "/":
        return num1/num2
    elif operator == "%":
        return num1%num2
    else:
        return "Aucun signe compatible"

def positif_negatif(nombre):
    if nombre<0:
        print("positif")
    elif nombre>0:
        print("négatif")
    else:
        print("0")

def who_s_that_developpeur(langage):
    if langage == "JavaScript":
        print("Tu est un développeur Web")
    elif langage == "python":
        print("Tu es un développeur IA")
    elif langage == "java":
        print("Tu es un développeur logiciel")
    elif langage == "reactjs":
        print("Tu es un développeur mobile")
    else:
        print("Un jour, je serai le meilleur développeur...")

def de_saison(type,saison):
    if type == "fruits":
        if saison == "hiver" :
            print("orange, mandarine et kiwi")
        elif saison == "été":
            print("Poire,fraise,cassis")
    elif type == "légume":
        if saison == "hiver":
            print("carotte, topinambour, endive")
        elif saison == "été":
            print("artichaut, aubergine,navet")

def moyenne(note1,note2,note3):
    moyenne_etudiant=(note1+note2+note3)/3
    if moyenne_etudiant >= 15:
        print(f"Trés bon élève, moyenne : {moyenne_etudiant}")
    elif moyenne_etudiant >= 11:
        print(f"Bon élève, moyenne : {moyenne_etudiant}")
    elif moyenne_etudiant >= 8:
        print(f"elève moyen, moyenne : {moyenne_etudiant}")
    else :
        print(f"Eleve devant faire des efforts, moyenne : {moyenne_etudiant}")

def pair_impaire_possitif(nb):
    if nb>0:
        if nb%2 == 0:
            return True
        else :
            return False
    else :
        return False
        
def time_to_text(temps):
    minutes=int(temps%60)
    heure=int((temps-minutes)/60)
    print(f"{heure} heures et {minutes} minutes")

def reversed_string(string):
    return string[::-1]

print(reversed_string("totalement"))