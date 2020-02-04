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

space=int(input)
for i in range(int(input)):
    space-=1
    print(' '*space+'*'*(i+1))
x=int(input)
space=0
for i in range(int(input)):
    space+=1
    x-=1
    print(' '*space+'*'*x)