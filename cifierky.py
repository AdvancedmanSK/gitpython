riadky = int(input())
for i in range(riadky):
    cislo = int(input())
    digits = list(int(x) for x in str(cislo))
    spravne = list(([int(x) for x in digits]))
    spravne.sort()
    print(spravne[0])