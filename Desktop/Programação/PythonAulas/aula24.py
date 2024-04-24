# operadores in e not in
# strings são iteráveis
# 0 1 2 3 4 5 6
# G U S T A V O
#-7-6-5-4-3-2-1

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar not in nome:
    print(f'{encontrar} não está em {nome}')
else:
    print(f'{encontrar} está em {nome}')