#split e join

frase = 'Vamos lá, que interessante.'

lista_frases_cruas = frase.split(',') # separa a string toda vez que encontra uma virgula

lista_frases = []

print(lista_frases)

for i,frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip()) #remove espaços

print(lista_frases_cruas)
print(lista_frases)

frase_unida = ', '.join(lista_frases) # junta novamente as frases com ,

print(frase_unida)