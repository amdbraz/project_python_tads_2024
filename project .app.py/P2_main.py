#Alunos: Luidy Viera, Ellen Roberta , Amanda Moreira , Gabriel Eiji ,Rodrigo Rodrigues, Erildo Nunes, Tony Everton.
#TADS - Projeto Eldoria/P2
#1º e 2º Período
#Prof : Richard Vieira

import time
from random import randint 
from classe import*
from tipo_monstros import*
from combate import combate_mfra,combate_mm,combate_mff,combate_md,bau 
from escolha import opcao_escolher

while True:
      caverna=int(input(f"""\033[34m Voce deseja explorar caverna ?\033[m 
                    [1]SIM
                    [2]NAO
                    """))
      if caverna == 2:
         print(f"\033[91m Você é fraco...lhe falta coragem\033[m\n1")
         print("-"*30)
        
      if caverna==1:
       
       time_devagar(f"\033[1;33m{"Você entrou na caverna... a procura de tesouros\n"}\033[m")
       jogada_d20 = randint (1,20)
       print(f'( dado obteve : {jogada_d20} )\n')
       #///////////////////////////////////////////////////
       if jogada_d20<=4:
           bau()
       #//////////////////////////////////////////////////    
       if jogada_d20>=4 and jogada_d20<=20:
           print("-"*30)
           time_devagar(f"\033[1;31m{"Voce encontrou um monstro!!!!\n"}\033[m")
           tipo_monster= randint(1,20)
           print(f'(sistema monstro {tipo_monster} )')
           print("-"*30)
       #//////////////////////////////////////////////
           if tipo_monster >=1 and tipo_monster <=9: #1 a 9 
               combate_mfra()
           if tipo_monster >=10 and tipo_monster <=15:
               combate_mm()
           if tipo_monster >=16 and tipo_monster <=19:
               combate_mff()
           if tipo_monster==20:
               combate_md()
