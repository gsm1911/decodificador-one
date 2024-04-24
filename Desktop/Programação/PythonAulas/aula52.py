# tuples

nomes = 'A', 'B', 'C' # ao declarar sem colchetes, cria-se uma tupla.
print(nomes)
#nomes[1] = 'A' geraria erro pois tuplas não são mutáveis

nomes = [1,2,3]
print(nomes)

nomes = tuple(nomes) #outra forma de declarar uma tupla é convertendo uma lista usando o método tuple()
print(nomes)