# enumerate

numeros = [1,2,3]

lista_enumerada = enumerate(numeros)

for n in lista_enumerada:
    print(n)
    
lista_enumerada = list(enumerate(numeros))
print(lista_enumerada)