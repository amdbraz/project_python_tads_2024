#Discentes: Amanda Moreira Braz, Tony, Ellen e Gabriel.
#1 Período - TADS

from random import randint

#Configurando o personagem
jogador = str(input('Digite o nome do aventureiro: '))
nivel = 1
experiencia = 0
vida = 3
print(f'''Bem-vindo à aventura, {jogador}. Esse é seu quadro atual:
Nível: {nivel}
Experiência: {experiencia}
Vida: {vida}''')

print('Deseja entrar na caverna misteriosa? [s/n]')
