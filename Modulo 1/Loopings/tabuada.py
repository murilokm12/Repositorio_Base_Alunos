numero = int(input("digite um  número para a tabuada:"))
inicio = int(input("digite o numero da aonde voce quer começar na tabuada:"))
fim = int(input("digite o numero da aonde voce quer terminar:"))


for i in range(inicio, fim):
    print(f"{i} x {numero} = {i * numero}")
   