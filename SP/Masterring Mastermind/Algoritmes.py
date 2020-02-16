import time
def algoritme1(kleuren, gekozenkleuren, feedback):
    combo = []
    poging = 1

    for i in kleuren:
        for x in kleuren:
            for y in kleuren:
                for z in kleuren:
                    combo.append([i, x, y, z])
    combo.sort()

    while len(combo) > 1:
        eerstegok = combo[0]
        print('In poging '+str(poging)+' gokt de computer dat de code '+str(eerstegok[0])+', '+str(eerstegok[1])+', '+str(eerstegok[2])+', '+str(eerstegok[3])+' is')
        if eerstegok == gekozenkleuren:
            break
        else:
            terug = feedback(gekozenkleuren, eerstegok)

            opslag = []

            for code in combo:
                x = feedback(eerstegok, code)
                if x == terug:
                    opslag.append(code)

            combo = opslag
            poging += 1
        time.sleep(3)
    return combo[0], poging