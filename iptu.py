area = float(input('Área construída? '))
aliquota = float(input('Alíquota? '))

iptu = 35.00 + (area * aliquota)
desconto1 = iptu * 0.75
desconto2 = iptu * 0.95

print(f'IPTU: R$ {iptu:.2f}\n')
print('Pagamento:')
print(f'1. Quota única. R$ {desconto1:.2f}')
print(f'2. Em 6 parcelas. Total: R$ {desconto2:.2f}')
print(f'   6 x R$ {desconto2/6:.2f}')
print(f'3. Em 10 parcelas. Total: R$ {iptu:.2f}')
print(f'   10 x R$ {iptu/10:.2f}')
