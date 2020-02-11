print('Welkom bij het spel Mastermind')

def gespeeld():
    J=['j', 'n']
    spel = input('Het je het spel al eerder gespeeld? J/N: ').lower()
    if spel not in J:
        print('Dit is geen geldig antwoord. Probeer nog eens')
        return gespeeld()
    elif spel == 'n':
        spelregels=input('Wil je de spelregels weten? J/N: ').lower()
        if spelregels == 'j':
            print('Dit zijn de spelregels van Mastermind:')
gespeeld()