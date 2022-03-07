numeros = input()
lista = numeros.split()
contagem = 0

for i in range(len(lista) - 1):
    if lista[i] == lista[i + 1]:
        contagem += 1

print(contagem)
