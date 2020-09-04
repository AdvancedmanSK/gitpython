pismeno = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","x","y","z"]
slovo = input(str("zadaj solov: "))
cislo_pismen = []
cislo_pismen_upravene = []
def premena_index():
    tocenie = int(0)
    for i in (slovo): #rozloženie slova po pismenach
        for j in range(24): #porovnavanie pismena(slovo) s listom pismeno a udavania indexu pismena
            if i==pismeno[tocenie]:
                cislo_pismen.insert(0, tocenie)
                tocenie = int(0)
                break
            tocenie = tocenie + 1
premena_index()

def zoradenie(zaklad, postupne):
    for i in range(len(zaklad)):
        postupne.append(max(zaklad))
        zaklad.remove(max(zaklad))
    print(postupne)

print(cislo_pismen)




    