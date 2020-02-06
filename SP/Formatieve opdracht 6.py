lijst=[1,6,3,7,9,6,4,6,8,6,4,5,10,9,6,6,9,5,5,3,4,5]
lijst2=[[1,2,4,3],[6,2,6,5,6],[6,3,5,7,4]]
def gemiddelde(lijst):
    aantal=len(lijst)
    som=sum(lijst)
    gem= som/aantal
    return print(gem)
gemiddelde(lijst)

#bron: practicum_2_statistiek_student.py (mijn ask opdracht voor practicum 2)

def gemlist(lijst):
    for i in lijst:
        gemiddelde(i)
gemlist(lijst2)