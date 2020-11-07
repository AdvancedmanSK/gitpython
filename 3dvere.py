import random



class Paradox_dvery:
    def __init__(self):
        self.D1=[]
        self.D2=[]
        self.D3=[]
        
    def rozlozenie(self,D1,D2,D3):
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
