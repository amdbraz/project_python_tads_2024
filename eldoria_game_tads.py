#Discentes: Amanda Moreira Braz, Tony, Ellen e Gabriel, Luidy Vieira , Rodrigo da silva, Erildo Nunes.
#1 e 2  Período - TADS

import os
from random import randint
import math

#mimik = baú surpresa
#random = 0, 20
nome = str(input('Digite o nome do aventureiro: '))

#jogador = vida, esquiva, ataque, ataque crítico, defesa
jogador = [nome, 'Ataque','Defesa','vida', 'Esquiva'] #definir valores dos atributos

#monstro = ataque, defesa, vida, esquiva
mmonstroF = ['Fraco',3, 1, 8, 2]
monstroM = ['Médio', 4, 1, 12, 4]
monstroD = ['Difícil', 6, 2, 20, 6]
monstroC = ['Chefe', 10, 5, 45, 8]

nome = str(input('Digite o nome do aventureiro: '))

print(f'Bem-vindo à aventura, {nome}.')

vocação = str(input('Escolha a sua vocação: '))


caverna = str(input('Deseja entrar na caverna misteriosa? [s/n]\n '))
if caverna == 's':
    print('Bem-vindo à Caverna. Pode entrar!')
else:
    print('Você saiu da caverna!🏃‍♂️💨') 
