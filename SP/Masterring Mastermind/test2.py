import random
kleuren = ['zwart', 'wit', 'rood', 'geel', 'blauw', 'groen']
combo = []

for i in kleuren:
    for x in kleuren:
        for y in kleuren:
            for z in kleuren:
                combo.append([i, x, y, z])

def feedback(code, gok):
    kleuren=[]
    for i in code:
        kleuren.append(i)
    keuze=[]
    for i in gok:
        keuze.append(i)

    index=0
    goed = 0
    nietgoedeplek = 0
    for i in kleuren:
        if i == keuze[index]:
            goed+=1
            kleuren[kleuren.index(keuze[index])] = 'niks'
            keuze[index] = 'nope'
            index += 1
        else:
            index += 1
    index=0
    for i in range(len(kleuren)):
        if keuze[index] in kleuren:
            nietgoedeplek += 1
            kleuren[kleuren.index(keuze[index])] = 'nada'
            keuze[index] = 'doei'
            index += 1
        else:
            index+=1
    return goed, nietgoedeplek

index=0
aantal=0
for i in combo:
    eerstegok = i
    gekozenkleuren = combo[random.randint(0,len(combo)-1)]
    if feedback(eerstegok, gekozenkleuren) != feedback(gekozenkleuren, eerstegok):
        print(eerstegok, gekozenkleuren)
        aantal+=1
        print(aantal)
        index+=1
    else:
        index+=1