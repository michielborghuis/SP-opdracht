n=int(input('f'))
x=[0,1]
def fibonaci(n,x):
    if n!=0:
        y=sum(x)
        x=x[1],y
        n-=1
    else:
        return x[0]
    return fibonaci(n,x)
print(fibonaci(n,x))