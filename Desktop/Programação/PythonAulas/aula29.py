"""
try/except
"""

numero_str = input('Digite um número: ')

try:
    numero_float = float(numero_str)
    numero_float = float(numero_str)
    print(f'Dobro de {numero_str} é {2 * numero_float}')
except:
    print('Isso não é um número.')