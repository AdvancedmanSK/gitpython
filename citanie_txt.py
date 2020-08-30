row = []
crimefile = open("marha.txt", 'r')
for line in crimefile.readlines():
    for i in line.split(","):
        row.append(i)


print(row[])