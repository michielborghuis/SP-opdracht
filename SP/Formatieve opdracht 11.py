alfa='abcdefghijklmnopqrstuvwxyz'
tekst=input('Geef een tekst: ')
cijfer=int(input('Geef een rotatie: '))
code=''
while cijfer > 26:
    cijfer -= 26

for i in tekst:
    lower=0
    if i not in alfa:
        try:
            i=i.lower()
            lower=1
            x = alfa.index(i)
            z = x + cijfer
            y = alfa[z]
            if lower == 1:
                code = code + y.upper()
            else:
                code = code + y
            lower = 0
        except ValueError:
            code=code+i
    else:
        x = alfa.index(i)
        z = x + cijfer
        y = alfa[z]
        if lower == 1:
            code = code + y.upper()
        else:
            code = code + y
        lower = 0
print('Ceadercode: '+str(code))