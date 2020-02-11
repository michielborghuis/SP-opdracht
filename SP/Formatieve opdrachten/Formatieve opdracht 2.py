string1=input('Geef een string: ')
string2=input('Geef een string: ')
index=0
def verschil(index):
    if index > len(string1)-1 or index > len(string2)-1:
        print('De 2 strings zijn hetzelfde')
    elif string1[index]==string2[index]:
        index+=1
        return verschil(index)
    else:
        print('Het eerste verschil zit bij index: '+str(index))
verschil(index)
