nome = input('Digite o nome do produto: ')
valor = input('Digite o valor do produto: ')
quantidade = input('Digite a quantidade do produto: ')

with open('produtos.text','a') as arquivo:
    arquivo.write(nome + ' | ' + valor + ' | ' + quantidade  +  '\n')