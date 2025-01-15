fruits=["pomme","cerise","orange"]

def job01():
    return fruits

def job02():
    return fruits[2]

def job03():
    fruits.append("Melon")
    return fruits

def job04():
    fruits.insert(2,"mangue")
    return fruits

def job05():
    L=[1,2,3,4,5]
    print(L)
    print(L[2])
    L[3]=L[2]+L[4]
    print(L)
    print(L[len(L)-1])

def job06(L):
    print(L)
    val_temp=L[0]
    L[0]=L[len(L)-1]
    L[len(L)-1]=val_temp
    print(L)

def job07():
    L=[8, 24,48,2,16]
    cpt=0
    for nb in L:
        if nb%3 == 0:
            cpt+=1
    return cpt

def job08():
    L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
    cpt=0
    for nb in L:
        if nb%2 == 0:
            cpt+=nb
    return cpt

def max(nb1,nb2):
    if nb1>nb2:
        return True
    else: 
        return False

def min(nb1,nb2):
    if nb1<nb2:
        return True
    else:
        return False

def job09():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    if max(L[0],L[1]):
        mini=L[1]
        maxi=L[0]
    else:
        mini=L[0]
        maxi=L[1]
    for i in range(2,len(L)):
        if max(L[i],maxi):
            maxi=L[i]
        elif min(L[i],mini):
            mini=L[i]
    print(f"La valeur max est : {maxi}")
    print(f"La valeur max est : {mini}")

def job10():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    cpt=1
    for nb in L:
        if 8<=nb<=90 :
            cpt*=nb
    return cpt

def job11():
    L = [7, 11, 42, 39, 2]
    for i in range(len(L)):
        L[i]=L[i]+1
    print(L)

def job13():
    L=[10, 20,30, 20, 10, 50, 60, 40, 80, 50, 40]
    L_temp=[]
    for i in L:
        if i not in L_temp:
            L_temp.append(i)
    print(L_temp)

job13()