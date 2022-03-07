def maioridade_penal(lista1,lista2):
    resultado = []
    saida = ''
    lista1 = lista1.split()
    lista2 = lista2.split()
    for i in range(len(lista2)):
        if int(lista2[i]) >= 18:
            resultado.append(lista1[i])
        saida = str(resultado).strip('[,]')
    return saida
