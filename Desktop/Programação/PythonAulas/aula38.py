linhas_total = 5
colunas_total = 5

linha = 1
while linha <= linhas_total:
    coluna = 1
    while coluna <= colunas_total:
        print(f'{linha=} {coluna=}')
        coluna += 1
    linha += 1

print('END')