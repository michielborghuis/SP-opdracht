input=input('Hoe groot? ')
for i in range(int(input)):
    print('*'*(i+1))
x=int(input)
for i in range(int(input)):
    x-=1
    print('*'*x)

i=0
while i!=int(input):
    i+=1
    print('*'*i)
while i!=0:
    i-=1
    print('*'*i)