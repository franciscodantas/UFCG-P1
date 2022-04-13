def minhafun(lista, preco=0):
    lista += [preco]
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] >= lista[i - 1]: break
        troca = lista[i]
        lista[i] = lista[i - 1]
        lista[i - 1] = troca
    return lista

lista = [15,16,18,20]
print(minhafun(lista, 17))
print(lista)
