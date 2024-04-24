senha_permitida = '123'

entrada = input('Entrar: E / Sair: S\nComando:')

if entrada not in 'EeSs':
    print('Comando inválido')
elif entrada not in 'Ss':
    senha_digitada = input('Senha: ')
else:
    print('Saiu')

if (entrada == 'E' or entrada == 'e'):
    if senha_digitada != senha_permitida:
        print('Senha inválida.')
    else:
        print('Entrou')