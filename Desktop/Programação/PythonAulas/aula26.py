"""
Formatação de strings

"""

var = 'oki doki'
print(f'{var}')
print(f'{var: >10}')
print(f'{var: <10}')

print(f'{1000.19325555253:0=+10,.1f}') 
# o + indica para mostrar o sinal de positivo
# o .1f indica para arredondar para uma casa decial
# o = força o numero aparecer antes do 0

print(f'O hexadecimal de 1500 é {1500:08X}')
# o X maiúsculo força o valor hexadecimal ser escrito em maiúsculo
print(f'O valor de 1500 em hexadecimal é {1500:x}')
# o x minúsculo faz o oposto, escreve tudo em minúsculo

print(f'{var!r}')
print(f'{var!s}')
print(f'{var!a}')

#experiment...
#for x in range(1):
#    for i in range(10):
#        print(' ' *  i + var)
#    for i in range(10):
#        print(' ' * (10-i) + var)
#        