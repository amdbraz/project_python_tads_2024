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
#ficha inicial
vida = 5
atk = 3
defesa = 2
esq = 0

guerreiro={'vida':5}
jogador_base={'jogador': nome ,'vida': 5 , 'ataque': 3, 'defesa' : 2, 'esq': 0}
if classe==1:
    jogador_base['ataque']+=2
    jogador_base['defesa']+=2
    print("jogador :",jogador_base['jogador'])
    print("ataque :",jogador_base['ataque'])

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






class monstro:
    def ___init____(self, personagen, exp_concedida):
        self.personagen = personagen 
        self.exp_concedida = exp_concedida


monstro_fraco = monstro('monstro fraco', 50)
monstro_medio = monstro ('monstro medio', 100)
monstro_dificil = monstro('monstro dificil', 200)
monstro_chefe = monstro('monstro chefe', 500)

class personagem:
    def ____init_____(self, personagem):
        self.personagem=personagem
        self.nivel = 1
        self.exp =0
        self.exp_para_proximo_nivel = 100
        self.vida=100
        self.forca =10
        self.defesa =5
