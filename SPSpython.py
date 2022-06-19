meno = []
priezvisko = []
row = []
char = ('"')
n = ("\n")

email = open("SPS.txt", 'r')    #otvorí súbor SPS.txt
for line in email.readlines():
    for i in line.split(","):
        row.append(i)
row = [x.lower() for x in row]   #precíta riadky

for i in range(0, len(row), 2):
    meno.append(row[i])


for i in range(1, len(row), 2):
    priezvisko.append(row[i])

for idx, ele in enumerate(priezvisko):
        priezvisko[idx] = ele.replace(char, '')

priezvisko = list(map(lambda x:x.strip(),priezvisko))
with open("spsfinal.txt","w") as finall:   #vytvorí spsfinal.txt
    for i in range(0, len(priezvisko)):
        finall.write(meno[i]+(",")+(priezvisko[i])+(",")+meno[i]+(".")+(priezvisko[i])+("@spsnmnv.sk")+(",SK")+"\n")   

