nome = input()
idade = int(input())

if idade < 5:
    print(f"{nome}, {idade} anos, Não pode competir.")
elif idade >= 5 and idade <= 7:
    print(f"{nome}, {idade} anos, Infantil A.")
elif idade <= 10:
    print(f"{nome}, {idade} anos, Infantil B.")
elif idade <= 13:
    print(f"{nome}, {idade} anos, Juvenil A.")
elif idade <= 17:
    print(f"{nome}, {idade} anos, Juvenil B.")
else:
    print(f"{nome}, {idade} anos, Senior.")
