import os

palavra_secreta = 'Terra'
letras_usadas = []
adivinhadas = []
counter = 0
vidas = 5

for n in range(len(palavra_secreta)):
    adivinhadas.append('_')
    
print('Jogo da forca.')

while True:
    print(f'Tentativas restantes: {vidas}')
    tentativa = input('Letra: ')

    if tentativa in letras_usadas:
        print('Essa letra já foi usada.')
        continue
    else:
        letras_usadas.append(tentativa)
    
    if tentativa in palavra_secreta:
        counter = 0
        for letra in palavra_secreta:
            if letra == tentativa:
                adivinhadas[counter] = letra
            else:
                pass
            counter += 1
    else:
        vidas -= 1
        print(f'A letra {tentativa} não está na palavra secreta.')

    if vidas < 0:
        print('Fim de jogo!')
        print(f'A palavra era: {palavra_secreta}')
        break
    if ''.join(adivinhadas) == palavra_secreta:
        print(f'Letras adivinhadas: {adivinhadas}')
        print('Parabéns, você ganhou.')
        print(f'A palavra era: {palavra_secreta}')
        break
    else:
        print(f'Letras adivinhadas: {adivinhadas}')
        print(f'Letras usadas: {letras_usadas}')