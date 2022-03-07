#UFCG - prog1
#Aluno: Francisco Antonio Dantas de Sousa
#Calcular quantos campos de futebol equivale 3 x áreas

area1 = float(input())
area2 = float(input())
area3 = float(input())

campo1 = area1/4000.0
campo2 = area2/4000.0
campo3 = area3/4000.0
media = (campo1 + campo2 + campo3)/3

print(f"{campo1:.2f}")
print(f"{campo2:.2f}")
print(f"{campo3:.2f}")
print(f'{media:.2f}')
