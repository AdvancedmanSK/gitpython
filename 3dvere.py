import random




D1=[False,False]
D2=[False,False]
D3=[False,False]
    
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
