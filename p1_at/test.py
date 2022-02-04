numeros = input()

inteiros = "1234567890."
tratamento = ""
lista= []


for caracter in numeros:
    if caracter in inteiros:
            tratamento += caracter
    if caracter not in inteiros or caracter == numeros[-1]:
        lista.append(tratamento)
        tratamento = ""

print(lista)
