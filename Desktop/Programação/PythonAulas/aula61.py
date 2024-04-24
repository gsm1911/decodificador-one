"""
Validar CPF

Colete a soma dos 9 primeiros digitos do CPF
Multiplique cada um dos valores por uma contagem regressiva
somar todos os resultados
multiplicar por 10
obter o resto da conta por 11

se for maior q 9:
resultado é 0
else:
resultado é o valor da conta


"""
cpf = '32375061098'
cpf_lista = []
soma = 0
i = 10
for n in cpf:
    cpf_lista.append(int(n))

cpf_lista = cpf_lista[:9]
print(cpf_lista)

for n in cpf_lista:
    print(n, i)
    soma += n * i
    i -= 1
    

soma = soma * 10

print('teste: ', soma%11)

if (soma%11) > 9:
    soma = 0
else:
    soma = soma%11

print(soma)


