licznik=0
suma=0
for j in range(5,1000):
    for i in range(1,j-1):
        if(j%i==0):
            suma+=i
    if(suma==j):
        licznik+=1
    suma=0
print(licznik)
