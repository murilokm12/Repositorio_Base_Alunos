listaUser=['jose','paulo']
while True:
    option=input('Digite uma opção:\n 1 para cadastrar o nome \n 2 para listar os nomes já cadastrados \n 3 para digitar o nome da lista que você quer \n excluir \n 0 para terminar o cadastro:')
    
    
    print()


    if option == '1' :

     nome=input('Digite seu nome para o cadastro: ')
     print()
     print('Nome cadastrado, para vê-lo, escolhe a opção 2 \n')
     listaUser.append(nome)

    elif option == '2':

     print('Nomes cadastrados:',listaUser) 
     print()

    elif option =='3':

        nomeDelete=input('Digite o nome que quer deletar: ')
        print()
    
         
        if nomeDelete in listaUser:
          listaUser.remove(nomeDelete)
          print('Nome deletado \n')
        
        else:
           print('NÃO ACHE ESSE NOME NA LISTA,POR FAVOR TENTE NOVAMENTE!\n')
       
    elif option == '0':
        print('👋Tchau Tchau👋')

        break;
