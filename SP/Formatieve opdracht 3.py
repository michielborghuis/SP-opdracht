#a.
lijst = [1, 5, 5, 5, 3, 6, 7, 9, 0]
def count(lijst):
    getal=int(input('Van welk getal wil jij weten hoe vaak het voorkomt in de lijst? '))
    hoeveel=0
    for i in lijst:
        if getal == i:
            hoeveel+=1
    print('Het getal '+str(getal)+' komt '+str(hoeveel)+' keer voor in de lijst')

#b.
lijst=[5,5,7,3,8,5,8,9,4,8,1,2,6,0]
def verschil(lijst):
    x=0
    for i in lijst:
        z=lijst[i]-lijst[i+1]
        if z>x:
            x=z
    print(x)
verschil(lijst)