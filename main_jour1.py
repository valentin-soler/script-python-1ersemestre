from tabulate import tabulate

#Job 02
def job2():
    print(10+3)

#Job 04:

lettre=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def job4():
    for i in lettre:
        print(i)

#Job 05:
def job5():
    for i in reversed(lettre):
        print(i)

# Job 06:

def job06():
    ma_string="Je suis une string"
    return ma_string

# Job 07:

def job07():
    num1=40
    num2=2
    return num1+num2

# Job 08:

def job08():
    num1=1
    num2=14
    return num1*num2

# Job 09:
#Je veux faire ça jolie
article=[["Banane", 4, 6],["Pomme", 2, 8],["Poire", 3, 4],["Ananas", 5, 2],["Fraise", 6, 10]]
def affichage_inventaire():
    tab_titre=["Nom","Quantité","Prix Unitaire"]
    return tabulate(article, headers=tab_titre, tablefmt="grid")
def aled_caaugmente(pourcentage,articleaaugmenter):
    for i in articleaaugmenter:
        i[2]=i[2]+i[2]*pourcentage/100
def job09():
    print(f"Prix des articles avant inflation:\n{affichage_inventaire()}")
    aled_caaugmente(10,article)
    print(f"Prix des articles aprés inflation:\n{affichage_inventaire()}")
    
# Job 10:

def calcul_gain(prix,rendement):
    return prix*(rendement/100)

def job10(argent, rendement):
    print(f"Argent investi: {argent} avec un rendement de {rendement}%")
    argent+=calcul_gain(argent,rendement)
    print(f"Argent aprés un an: {argent}")
    argent+=5000
    rendement+=2
    print(f"Argent aprés deux ans: {argent} avec un rendement de {rendement}% pour la 2nd années")
    argent+=calcul_gain(argent,rendement)
    print(f"Argent aprés deux ans: {argent}")
    argent-=argent*0.1
    rendement-=1
    argent+=calcul_gain(argent,rendement)
    print(f"Argent aprés trois ans: {argent} avec un rendement de {rendement}% pour la 3nd années")

#job10(10000,5)

# Job 11:
def job11(mot):
    for lettre in mot:
        if lettre =="e":
            return True
    return False

print(job09())