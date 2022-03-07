#UFCG - prog1
#Aluno: Francisco Antonio Dantas de Sousa
#Calcular o valor a ser pago pelos ingressos de x crianças e y adultos

adultos = int(input())
criancas = int(input())
preco = float(input())

valor = (adultos * preco) + (criancas * (preco/2))

print(f'Total: R$ {valor:.2f}')
