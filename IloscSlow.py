zdanie = input("Podaj zdanie")
licznik=1

for i in range(len(zdanie)-1):
    if zdanie[i] == ' ':
        licznik= licznik+1
print(licznik, 'slow')



