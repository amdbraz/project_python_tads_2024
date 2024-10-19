#Discentes: Amanda Moreira Braz, Tony, Ellen e Gabriel.
#1 Período - TADS

import os
from random import randint

#Configurando o personagem
#mimik = baú surpresa

jogador = str(input('Digite o nome do aventureiro: '))
nivel = 1
experiencia = 0
vida = 3
tentativa = 0
print(f'''Bem-vindo à aventura, {jogador}. Esse é seu quadro atual:
Nível: {nivel}
Experiência: {experiencia}
Vida: {vida}''')

caverna = str(input('Deseja entrar na caverna misteriosa? [s/n]\n '))
if caverna == 's':
    print('Bem-vindo à Caverna. Pode entrar!')
else:
    print('Você saiu da caverna!🏃‍♂️💨')
    while True: