#Exercicio: iterando string

nome = 'Gustavo Maeda'
novo_nome = ''
tamanho = len(nome)
contador = 0

while contador < tamanho:
    letra = nome[contador]
    novo_nome += f'*{letra}'
    contador += 1

nome = " ".join(str(n) for n in nome)
print(novo_nome)