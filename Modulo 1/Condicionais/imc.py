
nome = input("digite o nome do paciente: ")
peso = float(input ("digite seu peso: "))
altura = float(input("digite sua altura: "))

imc = peso / ( altura * altura )



if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.9:
    print("Peso normal")
elif imc < 29.9:
    print("Sobrepeso")
elif imc < 34.9:
    print("Obesedade Grau I")
elif imc < 39.9:
    print("Obesedade Grau II")
else:
    print("Obesedade Grau III")

    print(f"O paciente {nome} tem um imc de {imc}")

