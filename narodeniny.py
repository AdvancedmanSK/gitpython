import random

dni = [1,1]
n = int(input("zadaj číslo :"))

def zaklad():
    for i in range(n):
        dni.append(random.randint(1,356))
    
def porovnanie():
    for i in range(n):
        if dni[i] in dni:
            print("2 rovnaké dni sú: "+ str(dni[i]))
        else:
            continue
zaklad()
porovnanie()


