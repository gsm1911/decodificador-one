frase = 'O python é uma linguagem de '\
        'programação multiparadigma.'
        
i = 0
qtd = 0
maior = 0
letra_maior = ' '
while i < len(frase):
    letra = frase[i]
    if letra == ' ':
        i += 1
        continue
    qtd = frase.count(letra)
    if(qtd > maior):
        letra_maior = letra
        maior = qtd
    i += 1

print(f'A letra mais frequente foi [{letra_maior.upper()}] '\
      f'aparecendo {maior} vezes.')
