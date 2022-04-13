conta = 0

while True:
    consoante = 0
    vogais = 0

    palavra = input()
    for i in palavra:
        if i.lower() in 'aeiou':
            vogais += 1
        else:
            consoante += 1

    conta += 1
    if consoante > vogais: break

print(conta)
