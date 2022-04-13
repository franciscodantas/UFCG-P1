def calcula_digitos_verificacao(cpf):
    soma = 0
    for i in range(1,len(cpf)+1):
        soma += int(cpf[i * -1]) * (i+1)
    primeiro = (soma * 10)%11
    if primeiro == 10:
        primeiro = "0"
    else:
        primeiro = str(primeiro)

    cpf = cpf + primeiro

    soma = 0
    for i in range(1,len(cpf)+1):
        soma += int(cpf[i * -1]) * (i+1)
        

    segundo = (soma * 10)%11

    if segundo == 10:
        segundo = '0'
    else:
        segundo = str(segundo)

    return primeiro + segundo
