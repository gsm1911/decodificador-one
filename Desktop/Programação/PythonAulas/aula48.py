#Aula sobre listas.
# append, pop, del, insert, clear

lista = [1,2,3,4, ['a','b']]
print(lista)

lista[4] = 0 # alterando um valor
print(lista)

del lista[0] # deletando um valor
print(lista) # quando um valor é deletado, ele move todos os valores para indices novos para manter a consistência da lista.

lista.append(1) # adiciona um valor ao final da lista
print(lista)

lista.pop() # deletando o ultimo elemento da lista
print(lista)

lista.insert(0,5) # adicionando um item a um determinado índice
print(lista)

lista.clear() # limpando a lista
print(lista)

# adição de listas
lista1 = [0,1,2]
lista2 = [3,4,5]
lista3 = lista1 + lista2 

lista1.extend(lista2)
print(lista3)
print(lista1)

#valores imutáveis

lista_a = [1,2,3,4] 
lista_b = lista_a

print(lista_b)

lista_a[0] = 9 #mudando o valor de A, podemos observar que o valor de B também muda.

print(lista_b)

lista_b = lista_a.copy()

lista_a[0] = 'Mudei'

print(lista_b) # A lista B mantém o valor do momento em que o copy foi invocado.
print(lista_a) # A lista A muda sem mudar B ao usar o método copy().