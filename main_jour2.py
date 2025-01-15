#Job 01

def job01():
    for i in range(21):
        print(i)

# job01()

#Job 02
def job02():
    for i in range(0,21,2):
        print(i)

#job02()

#Job 03
def job03():
    for i in range(21):
        print(i**2)

#Job 04

def job04():
    entier = int(input("Entrez un entier:"))
    print(f"Table de multiplication de {entier}")
    for i in range(1,11):
        print(f"{entier} x {i} = {entier*i}")

# Job 05

def job05():
    i=1
    while i < 13:
        print(i)
        i+=1

# Job 06:

def job06():
    entier = int(input("Entrez un entier:"))
    print(f"Table de multiplication de {entier}")
    i=1
    while i < 11:
        print(f"{entier} x {i} = {entier*i}")
        i+=1

# Job 07

def job07():
    for i in range(1,13):
        print(f"Tour {i} : {i*3-2}")


# Job 08

def job08():
    result=0
    for i in range(1,13):
        result+=2
        print(f"Tour {i} : {result}")

# Job 09
def job09():
    print(f"Voici les nombre impaire entre 1 et 30")
    for i in range(1,31):
        if i%2 != 0:
            print(i)
    print(f"Voici les nombre paire entre 1 et 30")
    for i in range(1,31):
        if i%2 == 0:
            print(i)

job09()