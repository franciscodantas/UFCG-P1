def multiplica_lista(n,lista):
    resultado = []
    if n == 0:
        return []
    for i in range(n):
        for x in range(len(lista)):
            resultado.append(lista[x])
    return resultado

