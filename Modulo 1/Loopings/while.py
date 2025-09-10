numero = int(input("digite um  número para a tabuada:"))
inicio = int(input("digite o numero da aonde voce quer começar na tabuada:"))
fim = int(input("digite o numero aonde voce quer terminar:"))



while inicio <=  fim:
    print(f"{inicio} x {numero} = {inicio * numero}")
    inicio  +=1