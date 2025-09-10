print('lista:','marcos,Murilo,maria')

nome = input('Digite o nome que voce quer excluir :')

lista = ['Marcos','Murilo','Maria']



try:
    lista.remove(nome)
    print('nome excluido')
except:
    print('o nome nao existe')


