#While/Else

string = 'valor qualquer'

i=0

while i < len(string):
    letra = string[i]
    print(letra, end='.')
    i += 1
else:
    print('O else foi executado')