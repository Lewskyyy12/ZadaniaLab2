import sys
lista = [1,2,5,2.3,'srt', 'srt', 'ba','ab', 'ba', 2,3,4,5,1,2,3,'ba',4,4,5,9,8,8,'abba']
licznik=0
slownik = {}
for i in range(len(lista)):
    for j in range(len(lista)):
        if lista[i]==lista[j]:
            licznik+=1
        slownik[lista[i]]=licznik
    licznik=0
print(slownik)




