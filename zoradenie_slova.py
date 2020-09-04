from typing import final

pismeno = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
slovo = input(str("zadaj solov: "))
cislo_pismen = []
cislo_pismen_upravene = []
cislo_pismen_upravene_pismeno = []


def premena_index():
    tocenie = int(0)
    for i in (slovo): #rozloženie slova po pismenach
        for j in range(27): #porovnavanie pismena(slovo) s listom pismeno a udavania indexu pismena
            if i==pismeno[tocenie]:
                cislo_pismen.insert(0, tocenie)
                tocenie = int(0)
                break
            tocenie = tocenie + 1
premena_index()

def zoradenie(zaklad, postupne):
    for i in range(len(zaklad)):    #pridanie stareho kodu na zoradenie čísel
        postupne.append(min(zaklad))
        zaklad.remove(min(zaklad))

zoradenie(cislo_pismen, cislo_pismen_upravene)

def finnal():
    global final
    final = str()
    n = int(0)
    for i in range (len(cislo_pismen_upravene)):    #premena čísla na písmená
        cislo_pismen_upravene_pismeno.append(pismeno[cislo_pismen_upravene[n]])
        n = n + 1
    final = ("").join(cislo_pismen_upravene_pismeno)
        
    
finnal()        
        

print(final)




    