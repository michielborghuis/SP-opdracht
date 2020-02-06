ch=1011000
n= 3
def verschuiven(ch,n):
    x=ch[n:]
    y=ch[:n]
    return x+y
print(verschuiven(str(ch), n))