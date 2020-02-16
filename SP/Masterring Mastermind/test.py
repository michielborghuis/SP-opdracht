from Mastermind import *

gekozenkleuren = ['zwart', 'blauw', 'groen', 'wit']
print(gekozenkleuren)

def abcdefghijklmnopqrstuvwxyz(kleuren, gekozenkleuren):
    poging = 0
    combo = []
    for i in kleuren:
        for x in kleuren:
            for y in kleuren:
                for z in kleuren:
                    combo.append([i, x, y, z])
    combo.sort()
    while len(combo) > 1:
        antwoorden = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(3,0),(4,0)]
        bestworstcase = [1000,'combo']
        for i in combo:
            uitkomst = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for y in combo:
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

        terug = feedback(gekozenkleuren, eerstegok)

        for code in combo:
            x = feedback(eerstegok, code)
            if x == terug:
                opslag.append(code)

        combo = opslag
        poging += 1
    print('De computer heeft je code: '+str(combo[0])+' geraden in '+str(poging)+' pogingen')
abcdefghijklmnopqrstuvwxyz(kleuren, gekozenkleuren)