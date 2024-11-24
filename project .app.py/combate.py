from tipo_monstros import*
from devagar import*
from random import randint
from random import randint 
from classe import*
from escolha import*
import math




classe=int(input("""ESCOLHA SUA CLASSE  :
                            [1] guerreiro
                            [2] arqueiro
                            [3] paladino """))
        
time_devagar("*****classe escolhida*****\n")
raca=int(input("""ESCOLHA A RACA DO SEU PERSONAGEM :
                            [1] humano
                            [2] elfo
                            [3] anoes """))

print("---==---==-- raca escolhida!-------=-=-===")


if classe== 1 and raca ==1:
        personagem=guerreiro_humano()
        
elif classe==1 and raca==2:
        personagem=guerreiro_elfo()
        
elif classe==1 and raca==3:
                
        personagem=guerreiro_anao()
        
elif classe==2 and raca==1:
              
        personagem= arqueiro_humano()
        
elif classe==2 and raca==2:
                
        personagem=arqueiro_elfo()
        
elif classe==2 and raca==3:
                
        personagem=arqueiro_anao()
elif classe==3 and raca==1:
                
        personagem=paladino_humano()
                    
elif classe==3 and raca==2:
              
        personagem=paladino_elfo()
        
elif classe==3 and raca==3:
                
        personagem=paladino_anao()
else :
        print("OPS!!! opcao errada")

  
def combate_mfra():
     print(f"\033[1;34m{"Você encontou um monstro Fraco\n"}\033[m")
  
     while True:
             def escolha ():
               opcao=int(input("""Escolha com sabedoria :
                     [1] Atacar
                     [2] Fugir """))
               return opcao
          
          
             if escolha()==1:
                  dado_dano=randint(1,20)
                  time_devagar(f"dano atribuido é {dado_dano}\n")
                  ataque_jogador=dado_dano+personagem['ataque']
                  time_devagar(f"seu ataque e de {ataque_jogador}\n")
                  dano=ataque_jogador-monstros['monstro_fraco']['defesa']
                  if dano >0:
                       monstros['monstro_fraco']['vida']-=dano
                       ataque_jogador2=ataque_jogador-monstros['monstro_fraco']['vida']
                       print(f"vida restante do mosntro é ",monstros['monstro_fraco']['vida'])
                  if monstros['monstro_fraco']['vida']<=0:
                       time_devagar('vc venceu o monstro\n')
                       personagem['exp']+=50
                       print(f"voce ganhou 50 exp")
                       print(f"\033[1;32m Seu exp atual :\033[m {personagem['exp']}")
                       if personagem['exp']>=100 and personagem["exp"]<=140:
                               personagem['nivel']+=1
                               time_devagar(f"parabens você subiu de nivel\n")
                               print(f"\033[1;32m Seu Nivel :\033[m{personagem["nivel"]}\n")
                               atributo()
                       elif personagem['exp']>=140  and personagem["exp"]<=196:
                               personagem['nivel']+=1
                               time_devagar(f"parabens você subiu de nivel\n")
                               print(f"\033[1;32m Seu Nivel :\033[m{personagem["nivel"]}\n")
                               atributo()
                       elif personagem['exp']>=196  and personagem["exp"]<=274:
                               personagem['nivel']+=1
                               time_devagar(f"parabens você subiu de nivel\n")
                               print(f"\033[1;32m Seu Nivel :\033[m{personagem["nivel"]}\n")
                               atributo()
                       elif personagem['exp']>=274  and personagem["exp"]>=276:
                               personagem['nivel']+=1
                               time_devagar(f"Level Maximo \n")
                               print(f"\033[1;32m Seu Nivel :\033[m{personagem["nivel"]}\n")
                               atributo()
                       break         
                   
                   
                  if monstros['monstro_fraco']['vida']>=0: 
                   print("vez do monstro\n")
                   ataque_monstro=monstros['monstro_fraco']['ataque']
                   print(f'o monstro causara ({ataque_monstro}) de poder')
                  
                   opcao2=int(input("""Escolha com sabedoria :
                     [1] Defender
                     [2] Equivar
                     """))
                     
                   if opcao2 == 1 :
                      
                      print(" O monstro atacou\n")
                      dano_inimigo=max(0,ataque_monstro - personagem['defesa'])
                      personagem['vida']-=dano_inimigo
                      print(f"o monstro causou " , dano_inimigo)
                      print(f" Sua vida total é {personagem['vida']}")
                      if personagem['vida']<=0:
                          print("vc foi derrotado\n ")
                          break
                  
                   elif opcao2 == 2:
                           
                           dado_esquiva=randint(1,20)
                           dado_esquiva2=randint(1,20)
                           print(f"dado esquiva [jogador] = {dado_esquiva}")
                           print(f"dado esquiva [Monstro] = {dado_esquiva2}")
                           personagem["esquiva"]+=dado_esquiva
                           ataque_monstro+=dado_esquiva2
                           if personagem['esquiva']>= ataque_monstro:
                                   print("Voce conseguiu esquivar ")
                           elif personagem['esquiva']<= ataque_monstro:
                                   print('Voce nao consguiu desviar ')
                                   break
                                                
             else:     
                    chance= randint(1,2)
                    if chance==1:
                       time_devagar("Você consegiu fugir ")
                       print(f'seus status :{personagem}')
                       break
                    if chance ==2:
                       print("Você tentou fugir mais foi atingindo pelas costas\n")
                       print("PERDEU")
                       break
def combate_mm():
        
     print(f"\033[1;34m{"Você encontou um monstro medio"}\033[m")
     while True:
             def escolha ():
               opcao=int(input("""Escolha com sabedoria :
                     [1] Atacar
                     [2] Fugir"""))
               return opcao
          
          
             if escolha()==1:
                  dado_dano=randint(1,20)
                  print(f"dano{dado_dano}")
                  ataque_jogador=dado_dano+personagem["ataque"]
                  print(f"seu ataque e de {ataque_jogador}")
                  dano=ataque_jogador-monstros['monstro_medio']['defesa']
                  if dano >0:
                       monstros['monstro_medio']['vida']-=dano
                       ataque_jogador2=ataque_jogador-monstros['monstro_medio']['vida']
                       print(f"vida restante do mosntro ",monstros['monstro_medio']['vida'])
                  if monstros['monstro_medio']['vida']<=0:
                       print('vc venceu o monstro')
                       personagem['exp']+=100
                       print(f"voce ganhou 100 exp")
                       print(f"\033[1;32m Seu exp atual :\033[m {personagem['exp']}")
                       if personagem['exp']>=100 and personagem["exp"]<=140:
                               personagem['nivel']+=1
                               time_devagar(f"parabens você subiu de nivel\n")
                               print(f"\033[1;32m Seu Nivel :\033[m{personagem["nivel"]}\n")
                               atributo()
                       elif personagem['exp']>=140  and personagem["exp"]<=196:
                               personagem['nivel']+=1
                               time_devagar(f"parabens você subiu de nivel\n")
                               print(f"\033[1;32m Seu Nivel :\033[m{personagem["nivel"]}\n")
                               atributo()
                       elif personagem['exp']>=196  and personagem["exp"]<=274:
                               personagem['nivel']+=1
                               time_devagar(f"parabens você subiu de nivel\n")
                               print(f"\033[1;32m Seu Nivel :\033[m{personagem["nivel"]}\n")
                               atributo()
                       elif personagem['exp']>=274  and personagem["exp"]>=276:
                               personagem['nivel']+=1
                               time_devagar(f"Level Maximo \n")
                               print(f"\033[1;32m Seu Nivel :\033[m{personagem["nivel"]}\n")
                               atributo()
                       break
                   
                  if monstros['monstro_medio']['vida']>=0: 
                   print("vez do monstro")
                   ataque_monstro=monstros['monstro_medio']['ataque']
                   print(f'o monstro causara {ataque_monstro} de poder')
                  
                   opcao2=int(input("""Escolha com sabedoria :
                     [1] Defender
                     [2] Equivar
                     """))
                     
                   if opcao2 == 1 :
                      
                      print(" O monstro atacaou")
                      dano_inimigo=max(0,ataque_monstro - personagem['defesa'])
                      personagem['vida']-=dano_inimigo
                      print(f"o monstro causou " , dano_inimigo)
                      print(f" sua vida total {personagem['vida']}")
                      if personagem['vida']<=0:
                          print("vc foi derrotado")
                          break
                  
                   elif opcao2 == 2:
                           
                           dado_esquiva=randint(1,20)
                           dado_esquiva2=randint(1,20)
                           print(f"dado esquiva [jogador] = {dado_esquiva}")
                           print(f"dado esquiva [Monstro] = {dado_esquiva2}")
                           personagem["esquiva"]+=dado_esquiva
                           ataque_monstro+=dado_esquiva2
                           if personagem['esquiva']>= ataque_monstro:
                                   print("Voce conseguiu esquivar ")
                           elif personagem['esquiva']<= ataque_monstro:
                                   print('Voce nao consguiu desviar ')
                                   break
                           
                           
                           
                          
                          
                  
                  
                  
                  
                  
                  
                  
                  
                                        
             else:     
                    chance= randint(1,2)
                    if chance==1:
                       time_devagar("vc consegiu fugir ")
                       print(f'seus status :{personagem}')
                       break
                    if chance ==2:
                       print("vc tentou fugir mais foi atingindo pelas costas")
                       print("fim")
                       break            
def combate_mff():
    
     print(f"\033[1;34m{"Você encontou um monstro Forte"}\033[m")
  
     while True:
             def escolha ():
               opcao=int(input("""Escolha com sabedoria :
                     [1] Atacar
                     [2] Fugir"""))
               return opcao
          
          
             if escolha()==1:
                  dado_dano=randint(1,20)
                  print(f"dano{dado_dano}")
                  ataque_jogador=dado_dano+personagem["ataque"]
                  print(f"seu ataque e de {ataque_jogador}")
                  dano=ataque_jogador-monstros['monstro_forte']['defesa']
                  if dano >0:
                       monstros['monstro_forte']['vida']-=dano
                       ataque_jogador2=ataque_jogador-monstros['monstro_forte']['vida']
                       print(f"vida restante do mosntro ",monstros['monstro_forte']['vida'])
                  if monstros['monstro_forte']['vida']<=0:
                       print('vc venceu o monstro')
                       personagem['exp']+=200
                       print(f"voce ganhou 200 exp")
                       print(f"\033[1;32m Seu exp atual :\033[m {personagem['exp']}")
                       if personagem['exp']>=100 and personagem["exp"]<=140:
                               personagem['nivel']+=1
                               time_devagar(f"parabens você subiu de nivel\n")
                               print(f"\033[1;32m Seu Nivel :\033[m{personagem["nivel"]}\n")
                               atributo()
                       elif personagem['exp']>=140  and personagem["exp"]<=196:
                               personagem['nivel']+=1
                               time_devagar(f"parabens você subiu de nivel\n")
                               print(f"\033[1;32m Seu Nivel :\033[m{personagem["nivel"]}\n")
                               atributo()
                       elif personagem['exp']>=196  and personagem["exp"]<=274:
                               personagem['nivel']+=1
                               time_devagar(f"parabens você subiu de nivel\n")
                               print(f"\033[1;32m Seu Nivel :\033[m{personagem["nivel"]}\n")
                               atributo()
                       elif personagem['exp']>=274  and personagem["exp"]>=276:
                               personagem['nivel']+=1
                               time_devagar(f"Level Maximo \n")
                               print(f"\033[1;32m Seu Nivel :\033[m{personagem["nivel"]}\n")
                               atributo()
                               
                       break
                   
                  if monstros['monstro_forte']['vida']>=0: 
                   print("vez do monstro")
                   ataque_monstro=monstros['monstro_forte']['ataque']
                   print(f'o monstro causara {ataque_monstro} de poder')
                  
                   opcao2=int(input("""Escolha com sabedoria :
                     [1] Defender
                     [2] Equivar
                     """))
                     
                   if opcao2 == 1 :
                      
                      print(" O monstro atacaou")
                      dano_inimigo=max(0,ataque_monstro - personagem['defesa'])
                      personagem['vida']-=dano_inimigo
                      print(f"o monstro causou " , dano_inimigo)
                      print(f" sua vida total {personagem['vida']}")
                      if personagem['vida']<=0:
                          print("vc foi derrotado")
                          break
                  
                   elif opcao2 == 2:
                           
                           dado_esquiva=randint(1,20)
                           dado_esquiva2=randint(1,20)
                           print(f"dado esquiva [jogador] = {dado_esquiva}")
                           print(f"dado esquiva [Monstro] = {dado_esquiva2}")
                           personagem["esquiva"]+=dado_esquiva
                           ataque_monstro+=dado_esquiva2
                           if personagem['esquiva']>= ataque_monstro:
                                   print("Voce conseguiu esquivar ")
                           elif personagem['esquiva']<= ataque_monstro:
                                   print('Voce nao consguiu desviar ')
                                   break 
                  
                  
                  
                  
                                                
             else:     
                    chance= randint(1,2)
                    if chance==1:
                       time_devagar("vc consegiu fugir ")
                       print(f'seus status :{personagem}')
                       break
                    if chance ==2:
                       print("vc tentou fugir mais foi atingindo pelas costas")
                       print("fim")
                       break                                
def combate_md():
     print(f"\033[1;34m{"Você encontou um monstro Dificil"}\033[m")
  
     while True:
             def escolha ():
               opcao=int(input("""Escolha com sabedoria :
                     [1] Atacar
                     [2] Fugir"""))
               return opcao
          
          
             if escolha()==1:
                  dado_dano=randint(1,20)
                  print(f"dano{dado_dano}")
                  ataque_jogador=dado_dano+personagem["ataque"]
                  print(f"seu ataque e de {ataque_jogador}")
                  dano=ataque_jogador-monstros['monstro_dificil']['defesa']
                  if dano >0:
                       monstros['monstro_dificil']['vida']-=dano
                       ataque_jogador2=ataque_jogador-monstros['monstro_dificil']['vida']
                       print(f"vida restante do mosntro ",monstros['monstro_dificil']['vida'])
                  if monstros['monstro_dificil']['vida']<=0:
                       print('vc venceu o monstro')
                       personagem['exp']+=500
                       print(f"voce ganhou 500 exp")
                       print(f"\033[1;32m Seu exp atual :\033[m {personagem['exp']}")
                       if personagem['exp']>=100 and personagem["exp"]<=140:
                               personagem['nivel']+=1
                               time_devagar(f"parabens você subiu de nivel\n")
                               print(f"\033[1;32m Seu Nivel :\033[m{personagem["nivel"]}\n")
                               atributo()
                       elif personagem['exp']>=140  and personagem["exp"]<=196:
                               personagem['nivel']+=1
                               time_devagar(f"parabens você subiu de nivel\n")
                               print(f"\033[1;32m Seu Nivel :\033[m{personagem["nivel"]}\n")
                               atributo()
                       elif personagem['exp']>=196  and personagem["exp"]<=274:
                               personagem['nivel']+=1
                               time_devagar(f"parabens você subiu de nivel\n")
                               print(f"\033[1;32m Seu Nivel :\033[m{personagem["nivel"]}\n")
                               atributo()
                       elif personagem['exp']>=274  and personagem["exp"]>=276:
                               personagem['nivel']+=1
                               time_devagar(f"Level Maximo \n")
                               print(f"\033[1;32m Seu Nivel :\033[m{personagem["nivel"]}\n")
                               atributo()
                       break
                   
                   
                  elif monstros['monstro_dificil']['vida']>=0: 
                   print("vez do monstro")
                   ataque_monstro=monstros['monstro_dificil']['ataque']
                   print(f'o monstro causara {ataque_monstro} de poder')
                  
                   opcao2=int(input("""Escolha com sabedoria :
                     [1] Defender
                     [2] Equivar
                     """))
                     
                   if opcao2 == 1 :
                      
                      print(" O monstro atacaou")
                      dano_inimigo=max(0,ataque_monstro - personagem['defesa'])
                      personagem['vida']-=dano_inimigo
                      print(f"o monstro causou " , dano_inimigo)
                      print(f" sua vida total {personagem['vida']}")
                      if personagem['vida']<=0:
                          print("vc foi derrotado")
                   
                   
                   
                   elif opcao2 == 2:
                           
                           dado_esquiva=randint(1,20)
                           dado_esquiva2=randint(1,20)
                           print(f"dado esquiva [jogador] = {dado_esquiva}")
                           print(f"dado esquiva [Monstro] = {dado_esquiva2}")
                           personagem["esquiva"]+=dado_esquiva
                           ataque_monstro+=dado_esquiva2
                           if personagem['esquiva']>= ataque_monstro:
                                   print("Voce conseguiu esquivar ")
                           elif personagem['esquiva']<= ataque_monstro:
                                   print('Voce nao consguiu desviar ')
                                   break           
                          
                          
                          
                          
                          
                          
                                                
             else:     
                    chance= randint(1,2)
                    if chance==1:
                       time_devagar("vc consegiu fugir ")
                       print(f'seus status :{personagem}')
                       break
                    if chance ==2:
                       print("vc tentou fugir mais foi atingindo pelas costas")
                       print("fim")
                       break
def bau():
        
        time_devagar("Você encontrou um baú dourado\n")
        time.sleep(1)
        time_devagar("Abrindo o baú...\n")
        time.sleep(1)
        sistema_bau=randint(1,10)
        #///////////////////////////////
        print(f"(sitema {sistema_bau})\n")
        if sistema_bau >=1 and sistema_bau <=2:
            time_devagar("!!!!PERIGO!!!!\n")
            time.sleep(1)
            time_devagar("o bau era um monstro camufrado\n")
            combate_mfra() 
            return
        if sistema_bau >=3 and sistema_bau <=10:
         v_t={'vida_tota' : personagem["vida"]}
         rolagem=randint(1,10)
        
        tentativas = 3
        time_devagar("\n Tentando abrir o baú... \n")
        for i in range(tentativas):
            rolagem = randint(1, 20)
            time_devagar(f" Tentativa {i + 1}:\n Você rolou {rolagem}\n")
            time.sleep(0.5)
            if rolagem >= 10:
                time_devagar("\n Baú aberto com sucesso!\n")
                time_devagar("vc recuperou 50% da sua vida\n")
                personagem['vida']=min(v_t['vida_tota'],personagem['vida'] + v_t['vida_tota'] //2)
                print(f"sua vida atual:{personagem['vida']}")
                break
                    
            elif rolagem<=10:
             time_devagar("vc falhou em abrir o bau... tente novamente\n")
        else:
            time_devagar("\n vc falhou\n")
            
def atributo():
        personagem['ataque'] = int(personagem['ataque'] * 1.5)
        personagem['defesa'] = int(personagem['defesa'] * 1.5)
        personagem['vida'] = int(personagem['vida'] * 1.5)
        personagem['esquiva'] = int(personagem['esquiva'] * 1.5)
        print(f"Seu ataque :{personagem['ataque']}")
        print(f"Seu defesa :{personagem['defesa']}")
        print(f"Sua vida  :{personagem['vida']}")
        print(f"Sua esquiva :{personagem['esquiva']}")
        return
