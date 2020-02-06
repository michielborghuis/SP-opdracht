infile= open('text_opdracht_8.txt', 'r')
openfile= open('filter_opdracht_8.txt', 'w')

readlines=infile.readlines()
print(readlines)

for i in readlines:
    if i != '\n':
        openfile.write((i.strip()+'\n'))