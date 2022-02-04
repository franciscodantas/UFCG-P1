peso1 = float(input())
peso2 = float(input())

porcentagem = ((peso1 - peso2) * 100)/ peso1

if porcentagem >= 10.0:
    print(f"{porcentagem:.1f}% do peso do produto é de água congelada.\nProduto não conforme.")
elif porcentagem >= 5.0:
    print(f"{porcentagem:.1f}% do peso do produto é de água congelada.\nProduto em conformidade.")
else:
    print(f"{porcentagem:.1f}% do peso do produto é de água congelada.\nProduto qualis A.")

