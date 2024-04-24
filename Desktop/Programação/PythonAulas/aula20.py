#Programa que compara dois valores e diz qual é o maior e o menor.
n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')

if n1 > n2:
    print('O primeiro número digitado é o maior.')
    print(f'{n1} é maior que {n2}')
elif n2 > n1:
    print('O segundo número digitado é o maior.')
    print(f'{n2} é maior que {n1}')
else:
    print('Os dois números são iguais.')