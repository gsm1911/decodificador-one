lista_compras = []

print('Lista de compras APP')
while True:
    print('Comandos: 1- inserir 2- deletar 3- visualizar 4- sair')
    try:
        comando = int(input('Insira um comando: '))
    except:
        print('Algo deu errado.')
        continue
    if comando == 1:
        lista_compras.append(input('Insira a compra: '))
    if comando == 2:
        try:
            lista_compras.remove(input('Qual compra deseja remover? '))
        except:
            print('Algo deu errado.')
    if comando == 3:
        print(lista_compras)
    if comando == 4:
        break