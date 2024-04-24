#Calculadora com while

comando = 'o'
sair = '0'
input_invalida = False
comandos_validos = ['0','1','2','3','4']
while comando != sair:
    comando = input('0-Sair\n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\nComando:')
    
    while comando.isdigit() == False or comando not in comandos_validos:
        print('\nDigite um comando válido.\n')
        comando = input('0-Sair\n1-Adição\n2-Subtração\n3-Multiplicação\n4-Divisão\nComando:')
    
    if comando == '1':
        numero1 = input('\nDigite um numero: ')
        numero2 = input('Digite outro numero: ')
        while (numero1.isdigit() == False or numero2.isdigit() == False):
            print('Digite um numero valido.\n')
            numero1 = input('\nDigite um numero: ')
            numero2 = input('Digite outro numero: ')
        resultado = int(numero1)+int(numero2)
        print(f'O resultado de {numero1} + {numero2} é {resultado}\n')
    
    if comando == '2':
        numero1 = input('\nDigite um numero: ')
        numero2 = input('Digite outro numero: ')
        while (numero1.isdigit() == False or numero2.isdigit() == False):
            print('Digite um numero valido.\n')
            numero1 = input('\nDigite um numero: ')
            numero2 = input('Digite outro numero: ')
        resultado = int(numero1)-int(numero2)
        print(f'O resultado de {numero1} - {numero2} é {resultado}\n')
    
    if comando == '3':
        numero1 = input('\nDigite um numero: ')
        numero2 = input('Digite outro numero: ')
        while (numero1.isdigit() == False or numero2.isdigit() == False):
            print('Digite um numero valido.\n')
            numero1 = input('\nDigite um numero: ')
            numero2 = input('Digite outro numero: ')
        resultado = int(numero1)*int(numero2)
        print(f'O resultado de {numero1} * {numero2} é {resultado}\n')
    
    if comando == '4':
        numero1 = input('Digite um numero: ')
        numero2 = input('Digite outro numero: ')
        while (numero1.isdigit() == False or numero2.isdigit() == False):
            print('Digite um numero valido.\n')
            numero1 = input('Digite um numero: ')
            numero2 = input('Digite outro numero: ')
        while(numero2 == '0'):
            print('O divisor não pode ser zero.')
            numero2 = input('Digite outro numero: ')
        resultado = int(numero1)/int(numero2)
        print(f'O resultado de {numero1} / {numero2} é {resultado}\n')