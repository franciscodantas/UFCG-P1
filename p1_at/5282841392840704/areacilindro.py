#UFCG - prog1
#Aluno: Francisco Antonio Dantas de Sousa
#Calcular o valor da area do cilindro

print("Cálculo da Superfície de um Cilindro")
print("---")

diametro = float(input("Medida do diâmetro? "))
altura = float(input("Medida da altura? "))

print("---")

raio = diametro/2
base = diametro*3.1415
arearetangulo = base * altura
areacirculo = raio**2 * 3.1415
areacilindro = 2*areacirculo + arearetangulo

print(f"Área calculada: {areacilindro:.2f}")
