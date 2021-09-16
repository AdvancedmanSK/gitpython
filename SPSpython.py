meno = []
priezvisko = []
row = []
char = ('"')


email = open("SPS.txt", 'r')
for line in email.readlines():
    for i in line.split(","):
        row.append(i)

def meno():
    for i in range(0, len(row), 2):
        print(row[i])
meno()

for i in range(1, len(row), 2):
    priezvisko.append(row[i])

for idx, ele in enumerate(priezvisko):
        priezvisko[idx] = ele.replace(char, '')
        with open("spsfinall.txt", "w") as f:
            for line in priezvisko[idx]:
                f.write(line)

