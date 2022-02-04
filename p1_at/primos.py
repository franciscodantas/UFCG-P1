
primos = [2,3,5,7]

while 1 > 0:
    primo = int(input())
    cont = 0
    for i in range(len(primos)):
        if primo%primos[i] != 0:
            cont += 1
    if cont == len(primos) and primo != 1:
        primos.append(primo)
    print (primos)
