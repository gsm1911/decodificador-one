#f-strings

nome = 'Gustavo'
altura = 1.8
peso = 100
imc = peso/(altura**2)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso:.2f} quilos'
linha_3 = f'e tem um imc igual a {imc:.2f}'

print(linha_1, linha_2, linha_3)