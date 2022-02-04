#UFCG - prog1
#Aluno: Francisco Antonio Dantas de Sousa
#Calcular a hipotenuza

cpf1 = int(input())
cpf2 = int(input())
cpf3 = int(input())

cpf1numero = int(cpf1/100)
cpf1digito1 = int((cpf1%100 - cpf1%10)/10)
cpf1digito2 = cpf1%10
soma = cpf1digito1 + cpf1digito2

cpf2numero = int(cpf2/100)
cpf2digito1 = int((cpf2%100 - cpf2%10)/10)
cpf2digito2 = cpf2%10
soma2 = cpf2digito1 + cpf2digito2

cpf3numero = int(cpf3/100)
cpf3digito1 = int((cpf3%100 - cpf3%10)/10)
cpf3digito2 = cpf3%10
soma3 = cpf3digito1 + cpf3digito2

print(f'{cpf1numero}-{cpf1digito1}{cpf1digito2}\n{soma}\n{cpf2numero}-{cpf2digito1}{cpf2digito2}\n{soma2}\n{cpf3numero}-{cpf3digito1}{cpf3digito2}\n{soma3}')
