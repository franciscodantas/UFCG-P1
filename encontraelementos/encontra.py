numero = int(input())
sequencia = input()
sequencia = sequencia.split()
encontrada = 0

for i in sequencia:
    if int(i) == numero:
        encontrada += 1

if encontrada > 0:
    print('sim')
else:
    print('não')
