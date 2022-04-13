escrita_C1 = float(input())
didatica_C1 = float(input())
titulacao_C1 = float(input())
idade_C1 = float(input())
escrita_C2 = float(input())
didatica_C2 = float(input())
titulacao_C2 = float(input())
idade_C2 = float(input())

media_C1 = ((escrita_C1 * 30)+(didatica_C1 * 40)+(titulacao_C1 * 30))/100
media_C2 = ((escrita_C2 * 30)+(didatica_C2 * 40)+(titulacao_C2 * 30))/100

if media_C1 > media_C2 or (media_C1 == media_C2 and idade_C1 > idade_C2):
    print(f'O primeiro candidato foi aprovado com média {media_C1}.')
elif media_C1 == media_C2 and idade_C1 == idade_C2:
    print('Empate.')
else:
    print(f'O segundo candidato foi aprovado com média {media_C2}.')

