from classe import*
from devagar import time_devagar

def opcao_escolher():
  
    
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
        return opcao_escolher
