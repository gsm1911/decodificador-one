"""
Fatiamento de strings

0123456789
-9876543210

fatiamento [i:f:p] [::]

len retorna a quantidade de caracteres da str
"""

var = '0123456789'
print(var[-1])
print(var[4:])#vai da quinta casa pra frente
print(var[:4])#vai do começo até a quinta casa
print(var[::2])#omite o inicio e fim e pula de 2 em 2
print(var[::-1])#omite o inicio e fim e pula de 2 em 2
print(len(var))#retorna a qtd de caracteres na variavel