#Discentes: Amanda Moreira Braz, Tony, Ellen, Gabriel, Luidy Vieira, Rodrigo da silva, Erildo Nunes.
#1º e 2º  Período - TADS

import os
from random import randint
import math

#mimik = baú surpresa
#personagem
print("--------Seja Bem Vindo------")
nome = str(input('Digite seu nomedo aventureiro: '))
#jogador # Vida # ataque # defesa # esquiva 
base=[nome,8,2,1,0]
jogador=[nome,0,2,0,0,0]
#==-==-=-=-=-==-classe-=-=-=-=-=-=-=-=-
#nome | Vida | Ataque | Defesa | Esquiva 
guerreiro=[0,0,2,1,-1]
arqueiro=[0,-1,2,1,1]
paladino=[0,1,1,1,-1]

#=-=-=-=-==-Vocação-=-=-==-=-=
#nome | Vida | Ataque | Defesa | Esquiva 
humano=[0,1,1,1,1]
anao=[0,1,0,1,0]
elfo=[0,0,1,0,2]


print(f'Bem-vindo à aventura, {nome}.')

classe=int(input("""escolha sua classe :
                 [1] guerreiro
                 [2] arqueiro
                 [3] paladino"""))
#time aqui
print("---==---==-- classe escolhida!-------=-=-===")
#time aqui
raca=int(input("""escolha a raca do seu personagem :
                 [1] humano
                 [2] elfo
                 [3] anoes """))

print("---==---==-- raca escolhida!-------=-=-===")

if classe==1 and classe==1:
    jogador[1]=base[1]+guerreiro[1]+humano[1]
    jogador[2]=base[2]+guerreiro[2]+humano[2]
    jogador[3]=base[3]+guerreiro[3]+humano[3]
    jogador[4]=base[4]+guerreiro[4]+humano[4]
    print(f'{jogador[0]}')
    print (f'seu vida:{jogador[1]}')
    print (f'seu ataque:{jogador[2]}')
    print (f'sua defesa:{jogador[3]}')
    print (f'esquiva:{jogador[4]}')

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
