import random

dni = [1,1,356,356]
n = int(input("zadaj číslo :"))
def zaklad():
    for i in range(n):
        dni.append(random.randint(1,357))
        dni.sort()
    
def porovnanie():
    
zaklad()
porovnanie()
print(dni)



