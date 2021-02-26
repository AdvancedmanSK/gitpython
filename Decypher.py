main_row = []
sifra_row = []
main_int = int()
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

      
precitanie()
rozdelenie_sifry()
print(main_row)
print(sifra_row)

