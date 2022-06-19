
j, e = list(map(int,input().split()))
cisla = int,input()
znacky = list(map(int,input().split()))

if j and e in znacky:
    ema = znacky.count(e)
    jegor = znacky.count(j)
    if jegor > ema:
        print("Jergus")
    elif ema > jegor:
        print("Ema")
    else:
        print("remiza")
elif e in znacky:
    print("Ema")
else:
    print("Jergus")