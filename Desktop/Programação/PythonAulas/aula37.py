# Break: Encerra a execução do loop
# Continue: 

contador = 0

while contador <= 100:
    contador += 1
    
    if contador%2 == 0:
        continue #Isso faz com que ele pule uma repetição.
                 #de acordo com a condição.
    
    print(contador)
    
    if contador == 40:
        break