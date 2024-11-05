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
mmonstroF = ['Fraco',3, 1, 8, 2] #inserir os nomes dos monstros
monstroM = ['Médio', 4, 1, 12, 4]
monstroD = ['Difícil', 6, 2, 20, 6]
monstroC = ['Chefe', 10, 5, 45, 8]
#Pergunta se deseja entrar na caverna
#caverna = input('Deseja entrar na caverna misteriosa? [s/n]\n ').strip().lower()

    #Pergunta se deseja continuar ou desistir
continuar = input('Você deseja entrar na caverna misteriosa? [s/n]\n ').strip().lower()

if continuar == 's':

 #Rola o dado d20 para verificar o que encontrou
    for c in range (1, 20):
         if c <= 2:
             print("É um mímico! Você foi atacado!")



#inserir combate do monstro - menu input ataque, defesa +20 e fugir
    else:
        print("É um baú!")

            #O jogador tem 1 tentativa para abrir o baú

if c >= 2:
    print("Você abriu o baú e ganhou uma poção que restaura 50% da vida!")
else:
    print("Falha ao tentar abrir o baú.")

#Oferece a opção de desistir
desistir = input('Você deseja desistir de abrir o baú? [s/n]\n ').strip().lower()
if desistir == 's':
    print("Você decidiu desistir. O baú ficou fechado.")
else:
     print("Você não pode tentar abrir o baú novamente.")

if continuar == 'n':
    print('Você decidiu sair da caverna. Até a próxima! 🏃‍♂️💨')

else:
    print("Resposta inválida. Por favor, digite 's' ou 'n'.")
# Criando personagens
nome_heroi = "Heroi"
ataque_heroi = 5
defesa_heroi = 3
esquiva_heroi = 2

nome_inimigo = "Inimigo"
ataque_inimigo = 4
defesa_inimigo = 2
esquiva_inimigo = 1

# Teste de Ataque
d20 = random.randint(1, 20)
resultado_ataque = d20 + ataque_heroi
print(f"{nome_heroi} rolou {d20} + Ataque({ataque_heroi}) = {resultado_ataque}")

if resultado_ataque >= defesa_inimigo:
    print(f"{nome_heroi} acertou o ataque!")

    # Teste de Esquiva
    d20_esquiva = random.randint(1, 20)
    resultado_esquiva = d20_esquiva + esquiva_inimigo
    print(f"{nome_inimigo} rolou {d20_esquiva} + Esquiva({esquiva_inimigo}) = {resultado_esquiva}")

    if resultado_esquiva >= ataque_heroi:
        print(f"{nome_inimigo} esquivou do ataque!")
    else:
        print(f"{nome_inimigo} não esquivou!")

        # Cálculo de dano
        dano = ataque_heroi - defesa_inimigo
        if dano < 0:
            dano = 0

        print(f"Dano causado: {dano}")
else:
    print(f"{nome_heroi} não conseguiu acertar!")

# Verificação de Acerto Crítico
if d20 == 20:
    dano *= 2
    print("Crítico! Dano multiplicado por 2.")

# Definindo atributos iniciais do personagem
nivel = 1
exp = 0
atributo = 100  # Atributo inicial do personagem

# Experiência por tipo de monstro
exp_monstro_fraco = 50
exp_monstro_medio = 100
exp_monstro_dificil = 200
exp_monstro_chefe = 500

# Requisitos de EXP para subir de nível
def exp_para_subir_nivel(nivel):
    if nivel == 1:
        return 100
    else:
        return int(100 * (1.4 ** (nivel - 1)))

# Função para subir de nível
def subir_de_nivel():
    global nivel
    global atributo
    print("Parabéns! Você subiu para o nível", nivel + 1)
    nivel += 1
    atributo = int(atributo * 1.5)  # Aumenta o atributo em 50%
    print("Seu novo atributo é:", atributo)

# Loop principal do jogo
while True:
    print("\nVocê está no nível:", nivel)
    print("Experiência atual:", exp)
    exp_necessaria = exp_para_subir_nivel(nivel)
    print("Experiência necessária para o próximo nível:", exp_necessaria)

    # Escolher um monstro aleatório
    tipo_monstro = random.choice(["fraco", "medio", "dificil", "chefe"])
    if tipo_monstro == "fraco":
        print("Você enfrentou um Monstro Fraco!")
        exp += exp_monstro_fraco
    elif tipo_monstro == "medio":
        print("Você enfrentou um Monstro Médio!")
        exp += exp_monstro_medio
    elif tipo_monstro == "dificil":
        print("Você enfrentou um Monstro Difícil!")
        exp += exp_monstro_dificil
    elif tipo_monstro == "chefe":
        print("Você enfrentou um Monstro Chefe!")
        exp += exp_monstro_chefe

    print("Você ganhou", exp, "de experiência.")

    # Verifica se o personagem subiu de nível
    if exp >= exp_necessaria:
        subir_de_nivel()

    # Pergunta se deseja continuar jogando
    continuar = input("Deseja continuar enfrentando monstros? [s/n]\n").strip().lower()
    if continuar != 's':
        print("Obrigado por jogar!")
        break
# Definindo atributos iniciais do personagem
nivel = 1
exp = 0
atributo = 100  # Atributo inicial do personagem

# Experiência por tipo de monstro
exp_monstro_fraco = 50
exp_monstro_medio = 100
exp_monstro_dificil = 200
exp_monstro_chefe = 500

# Requisitos de EXP para subir de nível
def exp_para_subir_nivel(nivel):
    if nivel == 1:
        return 100
    else:
        return int(100 * (1.4 ** (nivel - 1)))

# Função para subir de nível
def subir_de_nivel():
    global nivel
    global atributo
    print("Parabéns! Você subiu para o nível", nivel + 1)
    nivel += 1
    atributo = int(atributo * 1.5)  # Aumenta o atributo em 50%
    print("Seu novo atributo é:", atributo)

# Loop principal do jogo
while True:
    print("\nVocê está no nível:", nivel)
    print("Experiência atual:", exp)
    exp_necessaria = exp_para_subir_nivel(nivel)
    print("Experiência necessária para o próximo nível:", exp_necessaria)

    # Escolher um monstro aleatório
    tipo_monstro = random.choice(["fraco", "medio", "dificil", "chefe"])
    if tipo_monstro == "fraco":
        print("Você enfrentou um Monstro Fraco!")
        exp += exp_monstro_fraco
    elif tipo_monstro == "medio":
        print("Você enfrentou um Monstro Médio!")
        exp += exp_monstro_medio
    elif tipo_monstro == "dificil":
        print("Você enfrentou um Monstro Difícil!")
        exp += exp_monstro_dificil
    elif tipo_monstro == "chefe":
        print("Você enfrentou um Monstro Chefe!")
        exp += exp_monstro_chefe

    print("Você ganhou", exp, "de experiência.")

    # Verifica se o personagem subiu de nível
    if exp >= exp_necessaria:
        subir_de_nivel()

    # Pergunta se deseja continuar jogando
    continuar = input("Deseja continuar enfrentando monstros? [s/n]\n").strip().lower()
    if continuar != 's':
        print("Obrigado por jogar!")
        break
#############################################################################################
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
