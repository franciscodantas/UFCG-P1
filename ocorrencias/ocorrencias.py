def remove_muitas_ocorrencias(lista):
    for i in lista:
        iguais = 0
        for x in lista:
            if i == x:
                iguais += 1
        if iguais >= 3:
            for y in range(len(lista)-1,-1,-1):
                if lista[y] == i:
                    lista.pop(y)
digitos = [0]
print(remove_muitas_ocorrencias(digitos))
print(digitos)

