
nome = input('Digite seu  nome: ')
email = input('Digite seu email: ')
telefone = input('Digite seu número de telefone:')



# print(f'nome: {nome}\n,email:{email},\ntelefone:{telefone}')


with open('contato.txt','a') as arquivo:
    arquivo.write(nome + ' | ' + email + ' | ' + telefone + '\n')







with open ('contato.txt','r')  as arquivos:
    leia = arquivos.read()
    print(leia)