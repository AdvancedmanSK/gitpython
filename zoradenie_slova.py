pismeno = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","x","y","z"]
tocenie = int(0)
slovo = input(str("zadaj solov: "))
cislo_pismen = []
for i in (slovo): #rozloženie slova po pismenach
    for j in range(24): #porovnavanie pismena(slovo) s listom pismeno a udavania indexu pismena
        if i==pismeno[tocenie]:
            cislo_pismen.insert(0, tocenie)
            tocenie = int(0)
            break
        tocenie = tocenie + 1
print(cislo_pismen)




    