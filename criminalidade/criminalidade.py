eocrime = []
saida = ''

media = float(input())

while True:
    entradas = input()
    if entradas == 'fim': break
    entradas = entradas.split()
    for i in entradas:
        if int(i) > media:
            eocrime.append(i)

for i in range(len(eocrime)-1):
    saida = f'{eocrime[i]} {eocrime[i + 1]}'

print(saida)
