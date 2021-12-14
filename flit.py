valor1 = int(input())
valor2 = int(input())
valor3 = int(input())

if valor1 % 10 == 0 or valor2 % 10 == 0 or valor3 % 10 == 0:
    print("Tumba")
else:
    if valor1 % 2 == 0:
        print("Fli")
    if valor2 % 3 == 0:
        print("Flat")
    if valor3 % 5 == 0:
        print("Flu")


