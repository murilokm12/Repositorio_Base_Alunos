import requests


dados = requests.get('https://68dd8c16d7b591b4b78cc263.mockapi.io/Restaurante')
print(f'Bem vindo ao meu restaurante ☺️\n')

while True:
    print()
    print(
    '1- Para ver todos os pedidos \n'
    '2- Para criar um novo pedido \n'
    '3- Para modificar um pedido específico \n'
    '4- Para remover uma mesa \n'
    '5- Para encenrrar:  ')
    print()
    resposta = input('Escolha uma opção: ')


    print()
    
    if  resposta =='1':
        dados = requests.get('https://68dd8c16d7b591b4b78cc263.mockapi.io/Restaurante').json()
        print('📋 Pedidos: \n')
        print(dados)
    
    
    
    if resposta == '2':
    
        mesa = int(input('qual o número da sua mesa: '))
        prato = input('qual o seu prato: ')
        bebida = input('qual a sua bebida: ')
    
    
    
    
        pedido={
        'Prato': prato,
        'Bebida': bebida,
        'Mesa': mesa
    }
    
        dados = requests.post(f'https://68dd8c16d7b591b4b78cc263.mockapi.io/Restaurante/' , pedido )
    
        dadosTratados = dados.json()
        
        print()
    
        print('Pedido anotado ')

    if resposta == '3':
        
        dados = requests.get('https://68dd8c16d7b591b4b78cc263.mockapi.io/Restaurante').json()
        print('📋 Ids: \n')
        # print(dados)
        mesa = ''
        for item in dados:
         print(item.get('id'))
         print()

        id = input('Qual o número da mesa que deseja modificar(id): ')
        novo_prato = input('Novo prato: ')
        nova_bebida = input('Nova bebida: ')

        for item in dados:
            if item.get('id') == id:
               mesa= item.get('Mesa')

        print()

        dados_atualizados = {
            'Prato': novo_prato,
            'Bebida': nova_bebida,
            'Mesa': mesa,
        }

        
        
        print()
         
        result = requests.put(f'https://68dd8c16d7b591b4b78cc263.mockapi.io/Restaurante/{id}',dados_atualizados)
        
        
        print(f'Mesa {id} modificada.')

    if resposta == '4':
            
            dados = requests.get('https://68dd8c16d7b591b4b78cc263.mockapi.io/Restaurante').json()
            print('📋 Pedidos: \n')
            print(dados)

            print()

            id = input('qual o número da sua mesa que deseja remover(id): ') 

            print()

            requests.delete(f'https://68dd8c16d7b591b4b78cc263.mockapi.io/Restaurante/{id}')

            print(f'Mesa {id} removida.' )
            
            print()

    if resposta == '5':
        
        print('Serviço encerrado.\n')
        break;


    # else:
    #  print('❌ Erro, essa opção não existe')



            # print('❌ Erro ao remover. Verifique se o ID está correto ou se a mesa existe.')


            # id = int(input('Digite um número correto ou uma mesa que já existe: '))

