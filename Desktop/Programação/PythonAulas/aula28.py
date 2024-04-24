nome = input('Insira seu nome: ')
idade = input('Insira sua idade: ')
if idade and nome:
    print(f'Seu nome invertido é: {nome[::-1]}')
    if ' ' not in nome:
        print(f'O nome {nome} não contém espaços.')
    else:
        print(f'O nome {nome} contém espaço.')
    print(f'Seu nome tem {len(nome.replace(" ", ""))} letras.')
    print(f'A ultima letra de {nome} é {nome[-1]}.')
else:
    print('Você deixou campos vazios.')