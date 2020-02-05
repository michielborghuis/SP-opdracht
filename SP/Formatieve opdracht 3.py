#a.
lijst1 = [1, 5, 5, 5, 3, 6, 7, 9, 0]
def count(lijst,getal):
    hoeveel=0
    for i in lijst:
        if getal == i:
            hoeveel+=1
    return hoeveel

#b.
lijst2=[5,5,7,3,8,5,8,9,4,8,1,2,6,0]
def verschil(lijst):
    x=0
    for i in lijst:
        z=lijst[i]-lijst[i+1]
        if z>x:
            x=z
    print(x)
verschil(lijst2)

#c.
lijst3=[0,1,1,1,0,0,0,1,1,1,0]
def goed(lijst):
    x=int(count(lijst,1))
    y=int(count(lijst,0))
    z=int(count(lijst,0))
    if x < y:
        return print('De lijst voldoet niet aan de eis: Het aantal enen is groter dan aan het aantal nullen')
    elif z > 12:
        return print('De lijst voldoet niet aan de eis: Er mogen niet meer dan 12 nullen zijn')
    else:
        return print('De lijst voldoet aan alle eisen')
goed(lijst3)
a