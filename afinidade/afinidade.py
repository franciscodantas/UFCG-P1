def tem_afinidade(l1, l2):
    soma = 0

    for i in l1:
        for x in l2:
            if i == x:
                soma += 1
    if soma >= 3:
        return True
    else:
        return False

l1 = ['zeze', 'bruno e marrone', 'joao', 'pedro', 'u2']
l2 = ['zeze', 'joao', 'jquest']
print(tem_afinidade(l1, l2))
