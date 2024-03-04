napis=input('Wprowadz napis: ')
for i in range(len(napis)):
    if napis[i]!=napis[len(napis)-i-1]:
        print('Nie jest palindromem!')
        break
else:
    print('Palindrom')