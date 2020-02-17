import time
import math
def algoritme1(alle_kleuren, geheime_code, feedback):
    print('\nDe computer heeft gekozen voor algoritme 1.\n')
    combinaties = []
    poging = 1

    for i in alle_kleuren:
        for x in alle_kleuren:
            for y in alle_kleuren:
                for z in alle_kleuren:
                    combinaties.append([i, x, y, z])
    combinaties.sort()

    while len(combinaties) > 1:
        eerstegok = combinaties[0]

        print('In poging '+str(poging)+' gokt de computer dat de code '+str(eerstegok[0])+', '+str(eerstegok[1])+', '+str(eerstegok[2])+', '+str(eerstegok[3])+' is.')

        if eerstegok == geheime_code:
            break
        else:
            terug = feedback(geheime_code, eerstegok)

            opslag = []

            for code in combinaties:
                x = feedback(eerstegok, code)
                if x == terug:
                    opslag.append(code)

            combinaties = opslag
            poging += 1
        time.sleep(3)
    return combinaties[0], poging


def algoritme2(kleuren, geheime_code, feedback):
    print('\nDe computer heeft gekozen voor algoritme 2.\nDe computer is de code aan het raden. Even geduld aub.')

    poging = 1
    combinaties = []

    for i in kleuren:
        for x in kleuren:
            for y in kleuren:
                for z in kleuren:
                    combinaties.append([i, x, y, z])
    combinaties.sort()

    while len(combinaties) > 1:
        antwoorden = [(0,0), (0,1), (0,2), (0,3), (0,4), (1,0), (1,1), (1,2), (1,3), (2,0), (2,1), (2,2), (3,0), (4,0)]
        bestworstcase = [1000, 'combo']

        for i in combinaties:
            uitkomst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for y in combinaties:
                x = feedback(y,i)
                if x == antwoorden[0]:
                    uitkomst[0] += 1
                elif x == antwoorden[1]:
                    uitkomst[1] += 1
                elif x == antwoorden[2]:
                    uitkomst[2] += 1
                elif x == antwoorden[3]:
                    uitkomst[3] += 1
                elif x == antwoorden[4]:
                    uitkomst[4] += 1
                elif x == antwoorden[5]:
                    uitkomst[5] += 1
                elif x == antwoorden[6]:
                    uitkomst[6] += 1
                elif x == antwoorden[7]:
                    uitkomst[7] += 1
                elif x == antwoorden[8]:
                    uitkomst[8] += 1
                elif x == antwoorden[9]:
                    uitkomst[9] += 1
                elif x == antwoorden[10]:
                    uitkomst[10] += 1
                elif x == antwoorden[11]:
                    uitkomst[11] += 1
                elif x == antwoorden[12]:
                    uitkomst[12] += 1
                elif x == antwoorden[13]:
                    uitkomst[13] += 1

            if max(uitkomst) < bestworstcase[0]:
                bestworstcase = max(uitkomst), i

        opslag = []

        eerstegok = bestworstcase[1]

        print('In poging ' + str(poging) + ' gokt de computer dat de code ' + str(eerstegok[0]) + ', ' + str(eerstegok[1]) + ', ' + str(eerstegok[2]) + ', ' + str(eerstegok[3]) + ' is.')

        if eerstegok == geheime_code:
            return eerstegok, poging

        terug = feedback(geheime_code, eerstegok)

        for code in combinaties:
            x = feedback(eerstegok, code)
            if x == terug:
                opslag.append(code)

        combinaties = opslag
        poging += 1
        time.sleep(3)
    return combinaties[0], poging

def algoritme3(kleuren, geheime_code, feedback):
    print('\nDe computer heeft gekozen voor algoritme 3.\nDe computer is de code aan het raden. Even geduld aub.')
    poging = 1
    combinaties = []

    for i in kleuren:
        for x in kleuren:
            for y in kleuren:
                for z in kleuren:
                    combinaties.append([i, x, y, z])
    combinaties.sort()

    while len(combinaties) > 1:
        antwoorden = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (3, 0), (4, 0)]
        bestworstcase = [1000, 'combo']
        eindlijst = []
        for i in combinaties:
            uitkomst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            bestcaseaantal=0
            for y in combinaties:
                x = feedback(y, i)
                if x == antwoorden[0]:
                    uitkomst[0] += 1
                elif x == antwoorden[1]:
                    uitkomst[1] += 1
                elif x == antwoorden[2]:
                    uitkomst[2] += 1
                elif x == antwoorden[3]:
                    uitkomst[3] += 1
                elif x == antwoorden[4]:
                    uitkomst[4] += 1
                elif x == antwoorden[5]:
                    uitkomst[5] += 1
                elif x == antwoorden[6]:
                    uitkomst[6] += 1
                elif x == antwoorden[7]:
                    uitkomst[7] += 1
                elif x == antwoorden[8]:
                    uitkomst[8] += 1
                elif x == antwoorden[9]:
                    uitkomst[9] += 1
                elif x == antwoorden[10]:
                    uitkomst[10] += 1
                elif x == antwoorden[11]:
                    uitkomst[11] += 1
                elif x == antwoorden[12]:
                    uitkomst[12] += 1
                elif x == antwoorden[13]:
                    uitkomst[13] += 1
            uitkomst.sort()
            while 0 in uitkomst:
                uitkomst.remove(0)
            if len(uitkomst) % 2 != 0:
                middelste = int((len(uitkomst)-1)/2)
                maxi = uitkomst[middelste]
            else:
                middelste = (len(uitkomst)-1)/2
                mid = uitkomst[math.floor(middelste)], uitkomst[math.ceil(middelste)]
                maxi = max(mid)
            if maxi <= bestworstcase[0]:
                bestworstcase = maxi, i
                bestcaseaantal+=1
                eindlijst.append(i)
        if bestcaseaantal == len(combinaties)-1:
            for code in eindlijst:
                if code == geheime_code:
                    poging+=1
                    print('In poging ' + str(poging) + ' gokt de computer dat de code ' + str(code[0]) + ', ' + str(code[1]) + ', ' + str(code[2]) + ', ' + str(code[3]) + ' is.')
                    return code, poging

        opslag = []

        eerstegok = bestworstcase[1]

        print('In poging ' + str(poging) + ' gokt de computer dat de code ' + str(eerstegok[0]) + ', ' + str(eerstegok[1]) + ', ' + str(eerstegok[2]) + ', ' + str(eerstegok[3]) + ' is.')

        terug = feedback(geheime_code, eerstegok)

        for code in combinaties:
            x = feedback(eerstegok, code)
            if x == terug:
                opslag.append(code)

        combinaties = opslag
        poging += 1
        time.sleep(3)
    return combinaties[0], poging