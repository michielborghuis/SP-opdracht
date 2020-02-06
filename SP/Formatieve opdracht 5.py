lijst=[10,9,8,6,7,5,4,3,2,1,0]
def sorteren(lijst):
    x = 0
    while x == 0:
        x = 1
        for i in range(len(lijst) - 1):
            if lijst[i] > lijst[i + 1]:
                lijst[i], lijst[i + 1] = lijst[i + 1], lijst[i]
                x = 0
    return print(lijst)
sorteren(lijst)

#Bron: practicum_4_algoritmiek_student.py (deel van mijn aks opdracht van practicum 4)