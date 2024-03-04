licznik=0
lista = []
while licznik<10:
    a = int(input())
    if a % 2 == 0:
        lista.append(a)
    licznik+=1
print(lista)