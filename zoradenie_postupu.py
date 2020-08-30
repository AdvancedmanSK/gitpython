zaklad = [12,5,848,165,2,4,36,16,852,8,]
postupne = []

def zoradenie():
    for i in range(len(zaklad)):
        postupne.append(max(zaklad))
        zaklad.remove(max(zaklad))
    print(postupne)

zoradenie()