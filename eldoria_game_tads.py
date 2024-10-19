#Discentes: Amanda Moreira Braz, Tony, Ellen e Gabriel.
#1 Período - TADS

import os
from random import randint
import math

#Configurando o personagem
#mimik = baú surpresa
#random = 0, 20
nome = str(input('Digite o nome do aventureiro: '))

#jogador = vida, esquiva, ataque, ataque crítico, defesa
jogador = [nome, , ,] #definir valores dos atributos

#Definição dos monstros -
monstroF = ['Fácil', , ,] #definir valores dos atributos dos monstros
monstroM = ['Médio', , ,]
monstroD = ['Difícil', , ,]
monstroB = ['Boss', , ,]





jogador = str(input('Digite o nome do aventureiro: '))



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