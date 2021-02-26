main_row = []
main_int = int()
def precitanie():
    global main_int, main_row
    sifra = open("sifra.txt")
    for lines in sifra.read().splitlines():
        try:
            int(lines)
            main_int = lines
        except:
            main_row.append(lines)
            print(main_row)

        
        
precitanie()
print(main_int)
