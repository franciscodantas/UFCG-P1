def inverte3a3(s):
    part = ''
    saida = ''
    tripla = []
    for i in range(len(s)):
        part += s[i]
        if len(part) == 3:
            tripla.append(part)
            part = ''

    for i in range(-1,(len(tripla)+1)*-1,-1):
        saida += tripla[i]

    return saida
