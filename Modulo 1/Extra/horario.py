
dia =  input('digite o periodo de agora manha , tarde ou noite:')

name= input('digite seu nome:')
def hora (nome , horario):

    if horario =='dia':
        print(f'Olá {nome},bom dia')
    
    elif horario =='tarde':
        print(f'Olá {nome},boa tarde')
    
    else :
        print(f'Olá {nome},boa noite')
    
hora(name,dia)



