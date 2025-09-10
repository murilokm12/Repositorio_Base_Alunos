nome = input('Digite o nome: ')
email = input('Digite o email: ')

arquivo = open('pessoa.text','a')
arquivo.write(nome + ' | '  + email + '\n')


arquivo.close()
