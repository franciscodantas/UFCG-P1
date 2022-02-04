capacidade = float(input('Capacidade de revestimento? '))

print('\n== Dados do vão a revestir ==')

comprimento = float(input('Comprimento? '))
largura = float(input('Largura? '))
altura = float(input('Altura? '))

arealateral = comprimento * altura
areadopiso = comprimento * largura
arealateral2 = largura * altura
total = arealateral * 2 + arealateral2 * 2 + areadopiso
caixas= int(total/capacidade)

print(f'\n== Resultados ==\nÁrea total a revestir: {total} m2\nNúmero de caixas: {caixas}')
