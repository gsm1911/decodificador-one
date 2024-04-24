# desempacotamento

nomes = ['Aldair', 'Bernard', 'Claud']

nome1, nome2, nome3 = nomes # para desempacotar devem haver o mesmo numero de variáveis que elementos na lista.

print(nomes)
print(nome1, nome2, nome3)

nome1, *resto = nomes # para desempacotar tendo menos variáveis que elementos, usa-se *nome_da_variavel

print(resto)

nome1, *_ = nomes # o underline usa-se para sinalizar que a variável não vai ser utilizada (por convenção)