import sys as system

print('Podaj liczby: ')
napis =system.stdin.readline()
liczby = napis.split(' ')
a=int(liczby[0])
b=int(liczby[1])
c=int(liczby[2])
system.stdout.write(str(a**b+c))