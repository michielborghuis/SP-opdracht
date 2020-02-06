import random
def gok():
    x=int(input('Geef getal tussen 1 en 10: '))
    z= random.randint(0, 10)
    if x!=z:
        print('Helaas, het getal was '+str(z)+'. Probeer maar opnieuw')
        gok()
    else:
        return print('Goedzo!')
gok()
a