def filtra_alunos(alunos,inscritos,minimo):
    for linha in range(len(alunos)-1,-1,-1):
        if alunos[linha][1] < minimo:
            alunos.pop(linha)

    for inscrito in inscritos:
        for linha in range(-1,len(alunos)*-1,-1):
            if inscrito != alunos[linha][0]:
                alunos.pop(linha)
    return alunos

inscritos = [121, 123, 124]
alunos = [ (120,8.0), (121,7.5), (122,5.0), (123,6.0), (124,9.0), (125,4.0) ]
print(filtra_alunos(alunos,inscritos,7.0))
