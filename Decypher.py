from string import ascii_letters

main_row = []
sifra_row = []
main_int = int()
pismena = list(ascii_letters[:26])
dve_pismena_sifrovane = []
dve_pismena_slovnik = []
jedna_dlzka_slovnik = []
jedna_dlzka_sifra = []
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
    global sifra_row, main_row, jedna_dlzka_slovnik, jedna_dlzka_sifra
    sifra_slova = (sifra_row[0].split())
    sifra_pocet = []
    slovnik_pocet = []
    kontrola_sifra = int(-1)
    kontrola = int(-1)
    pocet_opakovani_sifra = int(-1)
    pocet_opakovani = int()

    for i in range (len(sifra_slova)):
        sifra_pocet.append(len(sifra_slova[i]))

    for j in range (len(main_row)):
        slovnik_pocet.append(len(main_row[j]))

    for x in sifra_pocet:
        pocet_opakovani_sifra=sifra_pocet.count(x)
        if pocet_opakovani_sifra ==1:
            kontrola_sifra = kontrola_sifra + 1
            jedna_dlzka_sifra.append(sifra_slova[kontrola_sifra])
        else:
            kontrola_sifra = kontrola_sifra + 1

    for x in slovnik_pocet:
        pocet_opakovani=slovnik_pocet.count(x)
        if pocet_opakovani ==1:
            kontrola = kontrola + 1
            jedna_dlzka_slovnik.append(main_row[kontrola])
        else:
            kontrola = kontrola + 1

def split(word):
    return [char for char in word] 

def get_index_positions(list_of_elems, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from indexPos to the end of list
            index_pos = list_of_elems.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break
    return index_pos_list

def globalne():
    global dve_pismena_sifrovane, dve_pismena_slovnik
    usporiadanie(dve_pismena_slovnik)
    usporiadanie(dve_pismena_sifrovane)
    rozdelenie = []
    rozdelenie_slovnik = []
    iste_pismena_sifra = []
    iste_pismena_slovnik = []
    kontrola = []
    for x in dve_pismena_sifrovane:
        rozdelenie = split(x)
        for i in rozdelenie:
            if rozdelenie.count(i) >= 2:
                iste_pismena_sifra.append(get_index_positions(rozdelenie,i))
        if iste_pismena_sifra[0] == iste_pismena_sifra[1]:
            iste_pismena_sifra.pop(0)
        print(iste_pismena_sifra)

    
    for j in dve_pismena_slovnik:
        rozdelenie_slovnik = split(j)
        for x in rozdelenie_slovnik:
            if rozdelenie_slovnik.count(x) >=2:
                iste_pismena_slovnik.append(get_index_positions(rozdelenie_slovnik, x))




precitanie()
rozdelenie_sifry()
usporiadanie(main_row)
dvojica_pismen_sifrovania()
dvojica_pismen_slovnik()
usporiadanie(dve_pismena_slovnik)
usporiadanie(dve_pismena_sifrovane)
jedno_slovo()
globalne()
print(dve_pismena_slovnik)
print(dve_pismena_sifrovane)
print(jedna_dlzka_sifra)
print(jedna_dlzka_slovnik)
print(main_row)
print(sifra_row)

