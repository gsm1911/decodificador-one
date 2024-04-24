"""
Constante = valores que não mudam
Usa-se letras maiúsculas para definir constantes.

Muitas condições no mesmo IF = ruim
contagem de complexidade alta = ruim
"""

velocidade = 61 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distância que o radar pega

if local_carro != (LOCAL_1-RADAR_RANGE) and local_carro != (LOCAL_1+RADAR_RANGE):
    print('O carro está fora do alcance do radar.')
elif velocidade > RADAR_1:
    print('O carro está acima da velocidade permitida.')
    print('Multado pelo radar 1.')
else:
    print('O carro está dentro do limite de velocidade.')