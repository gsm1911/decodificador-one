#Operadores de atribuição

contador = 0

while contador < 10:
    contador += 1 #Podemos usar um igual junto da soma para somar e atribuir
    print(f'Contador:{contador}')

print('It\'s over')

#Outros exemplos:
contador *= 10
print(contador)  #multiplica e atribui
contador -= 10 #subtrai e atribui
print(contador)
contador /= 5 #divide e atribui
print(contador)
contador **= 2 # eleva ao expoente e atribui
print(contador)