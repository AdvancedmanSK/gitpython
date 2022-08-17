row = []
crimefile = open("XD.txt", 'r')
for line in crimefile.readlines():
    for i in line.split(","):
        row.append(i)

def meno():
    for i in range(0, len(row), 3):
        print(row[i])
meno()

def povolanie():
    for i in range(1, len(row), 3):
        print(row[i])
povolanie()

def age():
    for i in range(2, len(row), 3):
        print(row[i])
age()
    