#UFCG - prog1
#Aluno: Francisco Antonio Dantas de Sousa
#Calcular o custo de pintura de uma parede retângular

altura = float(input())
largura = float(input())

area = altura * largura
custo = area * 20.00

print(f"R$ {custo:.2f}")
