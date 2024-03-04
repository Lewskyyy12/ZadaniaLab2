liczba = int(input("Podaj Liczbe: "))
for i in range(2,liczba):
    if liczba % i == 0:
        print('Nie jest pierwsza')
        break
else:
    print('Jest pierwsza')