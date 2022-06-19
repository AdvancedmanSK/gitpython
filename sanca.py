n, k, p = [float(x) for x in input().split()]

odpoved = 0
z = 0

if k == 1:
    if p > 0.5:
        odpoved = (2*n)*p
    else:
        odpoved = n
else:
    if p > 0.5:
        while z != k:
            odpoved = (2*n)*p
            n = odpoved
            z += 1
    else:
        pass

def okruhlost(q, w):
    nasobit = 10 ** w
    return int(q * nasobit) / nasobit 


if odpoved > n:
    print(okruhlost(odpoved, 6))
else:
    print(okruhlost(n, 6))