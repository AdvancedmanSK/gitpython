import random
global n,spravne
n = int(input("zadaj číslo :"))
spravne = int(0)
for i in range (100):
    dni = []
    def zaklad():
        for i in range(n):
            dni.append(random.randint(1,357))
            dni.sort()
        
    def porovnanie():
        global spravne
        bruh = bool(False)
        for i in range(n-1):
            if dni[i] == dni[i+1]:
                print("Toto číslo je rovnaké: "+ str(dni[i]))
                bruh = True
        if bruh == True:
            spravne = spravne + 1

        



    zaklad()
    porovnanie()
    print(dni)
print(str(spravne))



