#Discentes: Amanda Moreira Braz, Tony, Ellen e Gabriel, Luidy Vieira , Rodrigo da silva,Erildo Nunes.
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

mmonstroF = ['Fracol','Ataque=3','Defesa=1','vida=8', 'Esquiva=2'] #definir valores dos atributos dos monstros
monstroM = ['Médio', 'Ataque=4','Defesa=1','vida=12', 'Esquiva=4']
monstroD = ['Difícil', 'Ataque=6','Defesa=2','vida=20', 'Esquiva=6']
monstroC = ['Chefe', 'Ataque=10','Defesa=5','vida=45', 'Esquiva=8']


Guerreiro= ['Ataque'+2,'Defesa'+1,'Esquiva'-1]
Arqueiro= ['Ataque'+2 ,'Esquiva'+1 , -1 'Defesa', -1 'Vida']
Paladino= ['Defesa'+1, 'Vida'+ 1, 'Ataque'+1, 'Esquiva' -1]


print(f'Bem-vindo à aventura, {jogador}.')

caverna = str(input('Deseja entrar na caverna misteriosa? [s/n]\n '))
if caverna == 's':
    print('Bem-vindo à Caverna. Pode entrar!')
else:
    print('Você saiu da caverna!🏃‍♂️💨')
    while True:
    


