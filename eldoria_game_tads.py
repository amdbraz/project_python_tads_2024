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

if classe==1 and raca==1:
    jogador[1]=base[1]+guerreiro[1]+humano[1]
    jogador[2]=base[2]+guerreiro[2]+humano[2]
    jogador[3]=base[3]+guerreiro[3]+humano[3]
    jogador[4]=base[4]+guerreiro[4]+humano[4]
    print(f'{jogador[0]}')
    print (f'seu vida:{jogador[1]}')
    print (f'seu ataque:{jogador[2]}')
    print (f'sua defesa:{jogador[3]}')
    print (f'esquiva:{jogador[4]}')
    print('teste')
elif classe== 1 and raca==2:
    jogador[1]=base[1]+guerreiro[1]+elfo[1]
    jogador[2]=base[2]+guerreiro[2]+elfo[2]
    jogador[3]=base[3]+guerreiro[3]+elfo[3]
    jogador[4]=base[4]+guerreiro[4]+elfo[4]
    print(f'{jogador[0]}')
    print (f'seu vida:{jogador[1]}')
    print (f'seu ataque:{jogador[2]}')
    print (f'sua defesa:{jogador[3]}')
    print (f'esquiva:{jogador[4]}')
elif classe == 1 and raca==3:
    jogador[1]=base[1]+guerreiro[1]+anao[1]
    jogador[2]=base[2]+guerreiro[2]+anao[2]
    jogador[3]=base[3]+guerreiro[3]+anao[3]
    jogador[4]=base[4]+guerreiro[4]+anao[4]
    print(f'{jogador[0]}')
    print (f'seu vida:{jogador[1]}')
    print (f'seu ataque:{jogador[2]}')
    print (f'sua defesa:{jogador[3]}')
    print (f'esquiva:{jogador[4]}') 
elif classe == 2 and raca==1:
    jogador[1]=base[1]+arqueiro[1]+humano[1]
    jogador[2]=base[2]+arqueiro[2]+humano[2]
    jogador[3]=base[3]+arqueiro[3]+humano[3]
    jogador[4]=base[4]+arqueiro[4]+humano[4]
    print(f'{jogador[0]}')
    print (f'seu vida:{jogador[1]}')
    print (f'seu ataque:{jogador[2]}')
    print (f'sua defesa:{jogador[3]}')
    print (f'esquiva:{jogador[4]}')
elif classe == 2 and raca==2:
    jogador[1]=base[1]+arqueiro[1]+elfo[1]
    jogador[2]=base[2]+arqueiro[2]+elfo[2]
    jogador[3]=base[3]+arqueiro[3]+elfo[3]
    jogador[4]=base[4]+arqueiro[4]+elfo[4]
    print(f'{jogador[0]}')
    print (f'seu vida:{jogador[1]}')
    print (f'seu ataque:{jogador[2]}')
    print (f'sua defesa:{jogador[3]}')
    print (f'esquiva:{jogador[4]}')
elif classe == 2 and raca==3:
    jogador[1]=base[1]+arqueiro[1]+anao[1]
    jogador[2]=base[2]+arqueiro[2]+anao[2]
    jogador[3]=base[3]+arqueiro[3]+anao[3]
    jogador[4]=base[4]+arqueiro[4]+anao[4]
    print(f'{jogador[0]}')
    print (f'seu vida:{jogador[1]}')
    print (f'seu ataque:{jogador[2]}')
    print (f'sua defesa:{jogador[3]}')
    print (f'esquiva:{jogador[4]}')
elif classe == 3 and raca==1:
    jogador[1]=base[1]+paladino[1]+humano[1]
    jogador[2]=base[2]+paladino[2]+humano[2]
    jogador[3]=base[3]+paladino[3]+humano[3]
    jogador[4]=base[4]+paladino[4]+humano[4]
    print(f'{jogador[0]}')
    print (f'seu vida:{jogador[1]}')
    print (f'seu ataque:{jogador[2]}')
    print (f'sua defesa:{jogador[3]}')
    print (f'esquiva:{jogador[4]}')    
elif classe == 3 and raca==2:
    jogador[1]=base[1]+paladino[1]+elfo[1]
    jogador[2]=base[2]+paladino[2]+elfo[2]
    jogador[3]=base[3]+paladino[3]+elfo[3]
    jogador[4]=base[4]+paladino[4]+elfo[4]
    print(f'{jogador[0]}')
    print (f'seu vida:{jogador[1]}')
    print (f'seu ataque:{jogador[2]}')
    print (f'sua defesa:{jogador[3]}')
    print (f'esquiva:{jogador[4]}') 
elif classe == 3 and raca==3:
    jogador[1]=base[1]+paladino[1]+anao[1]
    jogador[2]=base[2]+paladino[2]+anao[2]
    jogador[3]=base[3]+paladino[3]+anao[3]
    jogador[4]=base[4]+paladino[4]+anao[4]
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

# # Ficha inicial do jogador
# print("--------Seja Bem Vindo------")
# nome = str(input('Digite seu nome do aventureiro: '))
# print(f'Bem-vindo à aventura, {nome}.')
# print("""Escolha a sua vocação: )

# [1] Guerreiro

# [2] Arqueiro

# [3] Clero""")

# vocacao = int(input("Digite o número do seu tipo: "))

# #VOCAÇÃO
# guerreiro = {

#     'jogador': nome,

#     'vida': 5,

#     'ataque': 3,

#     'defesa': 2,

#     'esquiva': 0

# }

# if vocacao == 1:
#     print('Você escolheu o GUERREIRO. Este é seu quadro de vida:\n APARECER QUADRO DE VIDA')
# elif vocacao ==2:
#     print('Você escolheu o ARQUEIRO. Este é seu quadro de vida:\n APARECER QUADRO DE VIDA')
# else:
#     print('Você escolheu o CLERO. Este é seu quadro de vida:\n APARECER QUADRO DE VIDA')

caverna = str(input('Deseja entrar na caverna misteriosa? [s/n]\n '))
if caverna == 's':
    print('Bem-vindo à Caverna. Pode entrar!')
elif caverna == 'n':
    print('Você saiu da caverna!🏃‍♂️💨')

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

class personagem:
    def ____init_____(self, personagem):
        self.personagem=personagem
        self.nivel = 1
        self.exp =0
        self.exp_para_proximo_nivel = 100
        self.vida=100
        self.forca =10
        self.defesa =5
