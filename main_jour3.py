#Job 1

import re


def job1(valeur1,valeur2):
    if valeur1 == valeur2:
        return "Valeur1 est égal à Valeur2"
    else:
        return "Valeur1 est différent de Valeur2"
    
#Job 2

def job2(age):
    if age < 18:
        return "Tu ne peux pas voter"
    else:
        return "Tu peux voter"

#Job 3

def job3():
    for i in range(1,101):
        if i != 26 or i != 37 or i != 88:
            print(i)

#Job 4

def job4():
    for i in range(1,101):
        if i%3 == 0 or i%5 == 0:
            if not i%3 == 0:
                print("Buzz")
            elif not i%5 == 0:
                print("Fizz")
            else:
                print("FizzBuzz")
        else:
            print(i)

#Job 5

def est_premier(nb):
    if nb <= 1:
        return False
    for i in range(2, int(nb**0.5) +1):
        if nb%i==0:
            return False
    return True

def job5():
    for i in range(1,1001):
        if est_premier(i):
            print(i)

#Job 6

def job6():
    nb=int(input("Votre nombre\n"))
    if nb%2==0:
        return f"Le nombre {nb} est pair"
    else :
        return f"Le nombre {nb} est impair"

#Job 7

def job7():
    list_lettre="abcdefghijklmnopqrstuvwxyz"*10
    chaine=""
    for lettre in list_lettre:
        chaine+=lettre
        print(chaine)

#job 8:

def est_rectangle(a,b,c):
    if a**2==b**2+c**2:
        return True
    elif a**2+b**2==c**2:
        return True
    elif b**2==a**2+c**2:
        return True
    else:
        return False

def est_equilateral(a,b,c):
    if a==b==c:
        return True
    else:
        return False
    
def est_isocele(a,b,c):
    if a == b or b == c or a == c:
        return True
    else :
        return False
    
def job8(a,b,c):
    if est_rectangle(a,b,c):
        if est_isocele(a,b,c):
            return "Le triangle est rectangle et isocéle"
        else:
            return "Le triangle est rectangle"
    elif est_equilateral(a,b,c):
        return "Le triangle est équilatéral"
    elif est_isocele(a,b,c):
        return "Le triangle est isocéle"
    else:
        return "Le triangle est quelconque"
    
print(job8(6,8,10)) #Triangle Rectangle
print(job8(5,5,5*(2**0.5))) #Triangle Rectange et isocele
print(job8(7,7,6)) #Triangle isocele non rectangle
print(job8(5,5,5)) #triangle equilateral
print(job8(6,7,8)) #Triangle quelconque