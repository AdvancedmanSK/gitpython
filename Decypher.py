from string import ascii_letters


main_row = []
sifra_row = []
main_int = int()
pismena = list(ascii_letters[:26])
dve_pismena_sifrovane = []
dve_pismena_slovnik = []
jedna_dlzka_slovnik = []
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

def usporiadanie(zoznam):
    zoznam.sort(key=len)

def dvojica_pismen_sifrovania():
    global sifra_row,dve_pismena_sifrovane
    prva_sifra = []
    cislo_slova = int(-1)
    pocet_pismen = int(0)
    dve_pismena_sifrovane = []
    prva_sifra = (sifra_row[0].split()) 
    for i in (prva_sifra): 
        cislo_slova = cislo_slova + 1
        for j in i:
            pocet_pismen=prva_sifra[cislo_slova].count(j)
            if pocet_pismen >= 2:
                dve_pismena_sifrovane.append(prva_sifra[cislo_slova])
                dve_pismena_sifrovane = list(set(dve_pismena_sifrovane))
            else:
                continue


def dvojica_pismen_slovnik():
    global main_row, dve_pismena_slovnik
    prva_sifra = []
    cislo_slova = int(-1)
    pocet_pismen = int(0)
    dve_pismena_slovnik = []
    prva_sifra = main_row 
    for i in (prva_sifra): 
        cislo_slova = cislo_slova + 1
        for j in i:
            pocet_pismen=prva_sifra[cislo_slova].count(j)
            if pocet_pismen >= 2:
                dve_pismena_slovnik.append(prva_sifra[cislo_slova])
                dve_pismena_slovnik = list(set(dve_pismena_slovnik))
            else:
                continue    
      

def jedno_slovo():
    global sifra_row, main_row, jedna_dlzka_slovnik
    sifra_slova = (sifra_row[0].split())
    sifra_pocet = []
    slovnik_pocet = []
    cislo = int(-1)
    pocet_opakovani = int()
    for i in range (len(sifra_slova)):
        sifra_pocet.append(len(sifra_slova[i]))
        print(sifra_pocet)
    for j in range (len(main_row)):
        slovnik_pocet.append(len(main_row[j]))
        print(slovnik_pocet)
    for x in slovnik_pocet:
        pocet_opakovani=slovnik_pocet.count(x)
        if pocet_opakovani == 1:
            cislo = cislo + 1
            jedna_dlzka_slovnik.append(main_row[cislo])
        else:
            cislo = cislo + 1
            continue





precitanie()
rozdelenie_sifry()
usporiadanie(main_row)
dvojica_pismen_sifrovania()
dvojica_pismen_slovnik()
usporiadanie(dve_pismena_slovnik)
usporiadanie(dve_pismena_sifrovane)
jedno_slovo()
print(dve_pismena_slovnik)
print(dve_pismena_sifrovane)
print(jedna_dlzka_slovnik)
print(main_row)
print(sifra_row)

