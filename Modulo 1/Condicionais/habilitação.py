nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))
possui_carteira = input("possui carteira? 1 - sim | 2 - não: ")


if idade >= 18:
    print("maior de idade")
    if possui_carteira == "sim" or possui_carteira == "1":
        print("Pode dirigir !")
    else:
        print("Não pode dirigir")
else:
    print("menor de idade")