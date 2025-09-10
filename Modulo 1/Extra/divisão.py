num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')

try:
    num1 = int(num1)
    num2 = int(num2)
    
    print(f'O número {num1} dividido pelo número {num2} é: {num1 / num2}')

except:
    print('Digite uma divisão valida!')