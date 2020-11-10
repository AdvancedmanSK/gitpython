import random




D1=[False,False,False]
D2=[False,False,False]
D3=[False,False,False]
vyhra1 = 0   


def rozlozenie(D1,D2,D3):
    volba = random.randint(1,3)
    if volba == 1:
        D1[0]=True
        D2[0]=False
        D3[0]=False
    elif volba == 2:
        D1[0]=False
        D2[0]=True
        D3[0]=False
    else:
        D1[0]=False
        D2[0]=False
        D3[0]=True
    return D1[0],D2[0],D3[0]

def vybranie(D1,D2,D3):
    volba = random.randint(1,3)
    if volba == 1:
        D1[1]=True
        D2[1]=False
        D3[1]=False
    elif volba == 2:
        D1[1]=False
        D2[1]=True
        D3[1]=False
    else:
        D1[1]=False
        D2[1]=False
        D3[1]=True
    return D1[1],D2[1],D3[1]

def ukazanie(D1,D2,D3):
    if D1[0] == False and D1[1] == False:
        D1[2]=True
    elif D2[0] == False and D2[1] == False:
        D2[2]=True
    else:
        D3[2]=True
    return D1[2],D2[2],D3[2]

def zmena(D1,D2,D3):
    if D1[1] == True and D2[2] == True:
        D1[1] = False
        D3[1] = True
    if D1[1] == True and D3[2] == True:
        D1[1] = False
        D2[1] = True
    if D2[1] == True and D1[2] == True:
        D2[1] = False
        D3[1] = True
    if D2[1] == True and D3[2] == True:
        D2[1] = False
        D1[1] = True
    if D3[1] == True and D1[2] == True:
        D3[1] = False
        D2[1] = True
    if D3[1] == True and D2[2] == True:
        D3[1] = False
        D1[1] = True
    return (D1[1],D2[1],D3[1])

def vyhra(D1,D2,D3,vyhra1):
    if D1[0] == True and D1[1] == True:
        vyhra1 = vyhra1 + 1
        return vyhra1
    if D2[0] == True and D2[1] == True:
        vyhra1 = vyhra1 + 1
        return vyhra1    
    if D3[0] == True and D3[1] == True:
        vyhra1 = vyhra1 + 1
        return vyhra1
        




for i in range(100):
    rozlozenie(D1,D2,D3)
    vybranie(D1,D2,D3)
    ukazanie(D1,D2,D3)
    zmena(D1,D2,D3)
    print(vyhra(D1,D2,D3,vyhra1))
