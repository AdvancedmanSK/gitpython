from string import ascii_letters


main_row = []
sifra_row = []
main_int = int()
pismena = list(ascii_letters[:26])
def precitanie():
    global main_int, main_row
    sifra = open("sifra.txt")
    for lines in sifra.read().splitlines():
        try:
            int(lines)
            main_int = int(lines)   
        except:
            main_row.append(lines)

def rozdelenie_sifry():
    global main_row, sifra_row, main_int
    sifra_row = main_row[main_int:]
    main_row = main_row[0:main_int]

def usporiadanie():
    global main_row
    main_row.sort(key=len)

def sifrovanie():
    global main_row, sifra_row, pismena
    prva_sifra = []
    cislo_slova = int(-1)
    prva_sifra = (sifra_row[0].split()) 
    for i in (prva_sifra):  
        cislo_slova = cislo_slova + 1
        for j in i:
            docasne_ulozenie = j
            j = "/"
            if any(docasne_ulozenie in s for s in prva_sifra[cislo_slova]):
                print("mam slovo"+" "+j)
                "/" = j   #Toto treba dorobiť
            else:
                print("nemam slovo")

      
precitanie()
rozdelenie_sifry()
usporiadanie()
sifrovanie()
print(pismena)
print(main_row)
print(sifra_row)

