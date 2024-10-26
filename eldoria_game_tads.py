#Discentes: Amanda Moreira Braz, Tony, Ellen, Gabriel, Luidy Vieira, Rodrigo da silva, Erildo Nunes.
#1º e 2º  Período - TADS

import os
from random import randint
import math

#mimik = baú surpresa
#personagem
print("--------Seja Bem Vindo------")
nome = str(input('Digite seu nomedo aventureiro: '))
print(f'Bem-vindo à aventura, {nome}.')
classe=int(input("""escolha sua classe :
                 [1] guerreiro
                 [2] arqueiro
                 [3] clerico"""))
vida = 5
atk = 3
defesa = 2
esq = 0

jogador_base={'jogador': nome ,'vida': 5 , 'ataque': 3, 'defesa' : 2, 'esq': 0}
if 

#monstro = ataque, defesa, vida, esquiva
mmonstroF = ['Fraco',3, 1, 8, 2]
monstroM = ['Médio', 4, 1, 12, 4]
monstroD = ['Difícil', 6, 2, 20, 6]
monstroC = ['Chefe', 10, 5, 45, 8]



caverna = str(input('Deseja entrar na caverna misteriosa? [s/n]\n '))
if caverna == 's':
    print('Bem-vindo à Caverna. Pode entrar!')
else:
    print('Você saiu da caverna!🏃‍♂️💨')

vocação = str(input('Escolha a sua vocação: '))

# Rola o dado d20 para verificar o baú
rolagem = randint(1, 20 +1)

if rolagem <= 2:
    print("É um mímico! Você foi atacado!")
else:
    print("É um baú!")

# O jogador tem 3 tentativas para abrir o baú
    tentativas = 0
    while tentativas < 3:
        rolagem_abertura = randint(1, 20)
        if rolagem_abertura >= 10:
            print("Você abriu o baú e ganhou uma poção que restaura 50% da vida!")
            break
        else:
            print("Falha ao tentar abrir o baú.")
            tentativas += 1

    if tentativas == 3:
        print("Você falhou 3 vezes. O baú foi travado para sempre.")
