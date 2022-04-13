def insere_ordenado_primeiro(lista):
    while True:
        troca = False
        for num in range(len(lista)-1):
            if lista[num] > lista[num + 1]:
                trocado = lista[num + 1]
                lista[num + 1] = lista[num]
                lista[num] = trocado
                troca = True
        if troca == False: return
