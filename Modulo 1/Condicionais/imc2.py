nome = input("digite o nome do paciente: ")
peso = float(input ("digite seu peso do paciente: "))
altura = float(input("digite sua altura do paciente: "))

imc = peso / ( altura * altura )



if imc < 18.5:
   peso = "Abaixo do peso"
   print(peso)
   

elif imc <=24.9:
    peso = "Sobrepeso"
    print(peso)

elif imc <=29.9:
  peso = "sobrepeso"
  print(peso)



elif imc <=34.9:
   peso ="Obesedade Grau I"
   print(peso)    

elif imc <=39.9:
  peso = "Obesedade Grau II"
  print(peso)


else:
    peso ="Obesedade Grau III"
    print(peso)






print(f"O paciente {nome} tem IMC igual a {imc}, Classificado como {peso}")