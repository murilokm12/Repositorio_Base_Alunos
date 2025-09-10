nome = input("digite o nome do aluno: ")
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

print(f"O aluno {nome} tem a média de {media: .1f}")

