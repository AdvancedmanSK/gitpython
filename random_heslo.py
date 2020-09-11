import random
import string


def heslo(n):
    pismena = list(string.ascii_letters+string.digits)
    random.shuffle(pismena)
    hotovka = str()
    for i in range(n):
        hotovka = hotovka + pismena[(random.randint(0, len(pismena)))]
    print(hotovka)

bruh = int(input("Zadaj počet znakov: "))
heslo(bruh)