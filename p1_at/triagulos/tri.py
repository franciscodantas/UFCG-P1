import math

a = float(input())
b = float(input())
c = float(input())

perimetro = a + b + c

if (a > math.fabs(b - c)) and (b + c > a):
    if (b > math.fabs(a-c)) and (a + c > b):
        if (c > math.fabs(a-b)) and (a + b > c):
            print(f'triangulo valido. {int(perimetro)}')
        else:
            print('triangulo invalido.')
    else:
        print('triangulo invalido.')
else:
    print('triangulo invalido.')
