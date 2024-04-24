#1
try:
    numero = int(input('Insira um numero inteiro: '))
    if numero%2 == 0:
        print(f'O numero {numero} é par.')
    else:
        print(f'O numero {numero} é impar')
except:
    print('Você não digitou um numero inteiro.')

#2
try:
    hora = int(input('Insira a hora: '))

    if 0 <= hora <= 11:
        print('Bom dia.')
    elif 12 <= hora <= 17:
        print('Boa tarde.')
    elif 18 <= hora <= 23:
        print('Boa noite.')
    else:
        print('Hora desconhecida.')
except:
    print('Você não digitou uma hora válida.')

#3

nome = input('Insira seu primeiro nome: ')
tamanho = len(nome)

if tamanho > 1:
    if tamanho <= 4:
        print(f'O nome {nome} é curto.')
    elif 5 <= tamanho <= 6:
        print(f'O nome {nome} é normal.')
    else:
        print(f'O nome {nome} é muito grande.')

else:
    print('Nome não pode ser vazio.')