soma = 0
quantidade = 0
while True:
    numero = int(input())
    if numero < 0: break
    soma += numero
    quantidade += 1

media = soma/quantidade

print(soma, media)
