def idosos_inicio(fila):

    for i in range(len(fila)):
        for x in range(i+1,len(fila)):
            if fila[i] >= 60: break
            if fila[i] < fila[x] and fila[x] >= 60:
                trocado = fila[x]
                fila[x] = fila[i]
                fila[i] = trocado
                break

fila = [45,60,70,100,45,35]
print(idosos_inicio(fila))
print(fila)
