senha = '1234'
senha_digitada = ''
tentativas = 3

while tentativas > 0:
    senha_digitada = input('Digite a senha: ')
    if senha_digitada == senha:
        print('Bem vindo.')
        break
    else:
        print('Senha incorreta.')
        tentativas -= 1
        print(f'Tentativas restantes: {tentativas}')