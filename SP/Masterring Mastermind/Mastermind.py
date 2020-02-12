import random
print('Welkom bij het spel Mastermind')

def gespeeld():
    J=['j', 'n']
    spel = input('Heb je het spel al eerder gespeeld? J/N: ').lower()
    opnieuw(J, spel, 'Heb je het spel al eerder gespeel? J/N: ')
    if spel == 'n':
        spelregels=input('Wil je de spelregels weten? J/N: ').lower()
        opnieuw(J, spelregels, 'Wil je de spelregels weten? J/N: ')
        if spelregels == 'j':
            print('Dit zijn de spelregels van Mastermind:')

def gamemode():
    mode=['m','r']
    keuze= input('Wil je een code maken of een code raden? M/R: ').lower()
    opnieuw(mode, keuze, 'Wil je een code maken of een code raden? M/R: ')
    if keuze == 'm':
        print('Je hebt gekozen om een code te maken. De computer gaat de code proberen te raden.')
        return 'maken'
    else:
        print('Je hebt gekozen om de code (die de computer heeft gegenereerd) te raden.')
        return 'raden'

def gamemode_keuze():
    if gamemode() == 'maken':
        code_maken()
    else:
        code_raden()

def code_maken():
    kleuren = ['zwart', 'wit', 'rood', 'geel', 'blauw', 'groen']
    print('\nKies een code van 4 kleuren. De kleuren waar je uit kunt kiezen is: zwart, wit, rood, geel, blauw en groen.')
    kleur1 = input('Voer kleur 1 in: ').lower()
    opnieuw(kleuren, kleur1, 'Voer kleur 1 in: ')
    kleur2 = input('Voer kleur 2 in: ').lower()
    opnieuw(kleuren, kleur2, 'Voer kleur 2 in: ')
    kleur3 = input('Voer kleur 3 in: ').lower()
    opnieuw(kleuren, kleur3, 'Voer kleur 3 in: ')
    kleur4 = input('Voer kleur 4 in: ').lower()
    opnieuw(kleuren, kleur4, 'Voer kleur 4 in: ')

def code_raden():
    input('Klik op enter om het spel te beginnen.')
    kleuren = ['zwart', 'wit', 'rood', 'geel', 'blauw', 'groen']
    kleur1 = kleuren[random.randint(0,5)]
    kleur2 = kleuren[random.randint(0,5)]
    kleur3 = kleuren[random.randint(0,5)]
    kleur4 = kleuren[random.randint(0,5)]
    gekozenkleuren = [kleur1, kleur2, kleur3, kleur4]
    print(gekozenkleuren)

    print('\nDe computer heeft een code gegenereerd.\nDoe je eerste poging. De kleuren waar je uit kunt kiezen is: zwart, wit, rood, geel, blauw en groen.')

    goed = ['zwarte pion', 'zwarte pion', 'zwarte pion', 'zwarte pion']
    poging = 1
    pogingen(poging, gekozenkleuren, kleuren, goed)

def pogingen(poging, gekozenkleuren, kleuren, goed):
    terug = opnieuw_raden(gekozenkleuren, kleuren)
    if terug[1] == goed:
        return print('Gefeliciteerd! Je heb de code goed geraden in '+str(poging)+' poging(en).')
    else:
        print(str(terug[1]))
        print('\nJe hebt '+str(poging)+' poging(en) gedaan. Je hebt nog '+str(10-poging)+' poging(en) om de code goed te raden.')
        poging+=1
        return pogingen(poging, gekozenkleuren, kleuren, goed)

def opnieuw_raden(gekozenkleuren, kleuren):
    keuze = raden_keuze(kleuren)
    lijst=[]
    back = feedback(gekozenkleuren, keuze, lijst)
    return keuze, back

def feedback(gekozenkleuren, keuze, lijst):
    kleuren = gekozenkleuren
    index=0
    for i in kleuren:
        if i == keuze[index]:
            lijst.append('zwarte pion')
            index+=1
        elif keuze[index] in gekozenkleuren:
            lijst.append('witte pion')
            index+=1
        else:
            index+=1
    random.shuffle(lijst)
    return lijst

def raden_keuze(lijst):
    keuze1 = input('Voer kleur 1 in: ').lower()
    opnieuw(lijst, keuze1, 'Voer kleur 1 in: ')
    keuze2 = input('Voer kleur 2 in: ').lower()
    opnieuw(lijst, keuze2, 'Voer kleur 2 in: ')
    keuze3 = input('Voer kleur 3 in: ').lower()
    opnieuw(lijst, keuze3, 'Voer kleur 3 in: ')
    keuze4 = input('Voer kleur 4 in: ').lower()
    opnieuw(lijst, keuze4, 'Voer kleur 4 in: ')
    return keuze1, keuze2, keuze3, keuze4

def opnieuw(lijst, test, Input):
    while test not in lijst:
        print('Dit is geen geldig antwoord. Probeer nog eens')
        test=input(Input).lower()
    return test

def go():
    gespeeld()
    gamemode_keuze()

code_raden()