import random

dni = [1,1,356,356]
n = int(input("zadaj číslo :"))
def zaklad():
    for i in range(n):
        dni.append(random.randint(1,357))
        dni.sort()
    
def porovnanie():
    for i in range(0,n+3):
        if dni[i] == dni[i+1]:
            print("Toto číslo je rovnaké: "+ str(dni[i]))


zaklad()
porovnanie()
print(dni)



