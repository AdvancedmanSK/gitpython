def precitanie():
    sifra = open("sifra.txt","r")
    for lines in sifra.readlines():
        print(lines)
