def bubblesort(dados):
    while True:
        troca = False
        for num in range(len(dados)-1):
            if dados[num] > dados[num + 1]:
                trocado = dados[num + 1]
                dados[num + 1] = dados[num]
                dados[num] = trocado
                troca = True
        if troca == False:
            return dados
