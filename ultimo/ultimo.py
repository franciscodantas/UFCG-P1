def ultimo_indice(num, lista):
    ultimo_indice = -1
    for numero in range(len(lista)):
        if lista[numero] == num:
            ultimo_indice = numero
    return ultimo_indice

print(ultimo_indice(0, [15,2,13,11,14,2]))
