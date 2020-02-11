def palindroom(woord):
    x = ''
    for i in woord:
        x = i + x
    if (woord == x):
        return print('Dit woord is een palindroom')
    else:
        return print('Dit woord is geen palindroom')
palindroom('racecar')

def palindroom2(woord):
    x = ''.join(reversed(woord))
    if woord == x:
        print('Dit woord is een palindroom')
    else:
        print('Dit woord is geen palindroom')
palindroom2('reinier')

#Bron: https://www.geeksforgeeks.org/python-program-check-string-palindrome-not/