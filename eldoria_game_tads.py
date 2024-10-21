#Discentes: Amanda Moreira Braz, Tony, Ellen e Gabriel, Luidy Vieira.
#1 e 2  Período - TADS

import os
from random import randint
import math

#Configurando o personagem
#mimik = baú surpresa
#random = 0, 20
nome = str(input('Digite o nome do aventureiro: '))

#jogador = vida, esquiva, ataque, ataque crítico, defesa
jogador = [nome, 'Ataque','Defesa','vida', 'Esquiva'] #definir valores dos atributos

#Definição dos monstros -
monstroF = ['Fácil', , ,] #definir valores dos atributos dos monstros
monstroM = ['Médio', , ,]
monstroD = ['Difícil', , ,]
monstroB = ['Boss', , ,]


Guerreiro= ['Ataque'+2,'Defesa'+1,'Esquiva'-1]
Arqueiro= ['Ataque'+2 ,'Esquiva'+1 , -1 'Defesa', -1 'Vida']:
Paladino= [+1 'Defesa', +1 'Vida', +1 'Ataque', -1 'Esquiva']


print(f'Bem-vindo à aventura, {jogador}.')

caverna = str(input('Deseja entrar na caverna misteriosa? [s/n]\n '))
if caverna == 's':
    print('Bem-vindo à Caverna. Pode entrar!')
else:
    print('Você saiu da caverna!🏃‍♂️💨')
    while True: