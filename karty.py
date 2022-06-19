a = input()

karty = input()
karty = karty.split()

karty = sorted(karty, reverse=True)

j = []
f = []

for i in range(0, len(karty)):
    if (i % 2) == 0:
        f.append(karty[i])
    else:
        j.append(karty[i])



j = [int(i) for i in j]
f = [int(i) for i in f]

j = sum(j)
f = sum(f)
print(str(f) + " " + str(j))



