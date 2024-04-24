"""
Interpolação básica de strings

s - string
d e i - INT
f - float
x e X - hexadecimal
"""

nome = 'Gustavo'
preco = 1200.10
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (150, 150))