entrada = input()
palavra = []
saida = ''
trocas = 0
inicio = 0

if entrada[0].lower() == 'a' or entrada[0].lower() == 'e' or entrada[0].lower() == 'i' or entrada[0].lower() == 'o':
    palavra.append(entrada[0])
    inicio += 1

for i in range(inicio,len(entrada)):
    if entrada[i].lower() == 'a':
        palavra.append('4')
        trocas += 1
    elif entrada[i].lower() == 'e':
        palavra.append('3')
        trocas += 1
    elif entrada[i].lower() == 'i':
        palavra.append('1')
        trocas += 1
    elif entrada[i].lower() == 'o':
        palavra.append('0')
        trocas += 1
    else:
        palavra.append(entrada[i])
for i in range(len(entrada)):
    saida += palavra[i] 

print(f'{saida} ({trocas} troca(s))')
