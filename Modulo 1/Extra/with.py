nome = input('Digite o nome: ')
email = input('Digite o email: ')

with open('pessoa.text','a') as arquivo:
    arquivo.write(nome + ' | ' + email + '\n')