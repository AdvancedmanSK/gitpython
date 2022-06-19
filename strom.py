a = int(input())
slovnik = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
strom = []
cislo = 0
obratene = []
b = 0
count = 0
c = -1
d = 0
rozdelenie = []
def split(word):
    return [char for char in word]

def pocitanie(test_str):
    global count
    for i in test_str:
        if i == 'o':
            count = count + 1
    return(count)



for x in range(a):
    s = input()
    strom.insert(0, s)



for x in range(len(strom)):
    rozdelenie = split(strom[x])
    for i in range(len(rozdelenie)):
        if rozdelenie[i] == "o":
            rozdelenie[i] = slovnik[b]
            b = b + 1
            strom[x] = "".join(rozdelenie)
        else:
            continue

            
strom.reverse()
for i in strom:
    print(i)
