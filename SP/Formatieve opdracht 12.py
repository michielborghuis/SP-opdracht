for i in range(1,101):
    if i%3==0 and i%5!=0:
        print('Fizz')
    elif i%5==0 and i%3!=0:
        print('Bizz')
    elif i%5==0 and i%3==0:
        print('FizzBizz')
    else:
        print(i)