import time

def time_devagar(texto, intervalo=0.07):
    for caractere in texto:
        print(caractere, end='', flush=True)
        time.sleep(intervalo)
        
def guerreiro_anao():
     
     print("**SEJA BEM VINDO JOGADOR**")
     Nome=input( "DIGITE SEU NOME ")
     

     g_a={
   
    "vida": 10,
    "ataque": 3,
    "defesa": 3,
    "esquiva": 0,
    "nivel":1,
    "exp":0}
     time_devagar("Configurando seu personagem....\n")
    
     print(f"\033[1;30;47m{"///// SEUS STATUS /////"}\033[m")
     print(f"jogador : \033[32m{Nome}\033[m")
     print(g_a)
     return g_a

def guerreiro_humano():
     print("**SEJA BEM VINDO JOGADOR**")
     Nome=input("DIGITE SEU NOME ")
     
     
     g_h={
    
        "vida": 9,
        "ataque": 5,
        "defesa": 3,
        "esquiva": 0,
        "nivel":1,
        "exp":0}
     time_devagar("Configurando seu personagem....\n")
     print(f"\033[1;30;47m{"///// SEUS STATUS /////"}\033[m")
     print(f"jogador : \033[32m{Nome}\033[m")
     print(g_h)
     return g_h

def guerreiro_elfo():
     print("**SEJA BEM VINDO JOGADOR**")
     Nome=input("DIGITE SEU NOME ")
     
     g_e={
 
    "vida": 8,
    "ataque": 5,
    "defesa": 2,#2
    "esquiva": 1,
    "nivel":1,
    "exp":0}
     time_devagar("Configurando seu personagem....\n")
     print(f"\033[1;30;47m{"///// SEUS STATUS /////"}\033[m")
     print(f"jogador : \033[32m{Nome}\033[m")
     print(g_e)
     return g_e
 
def arqueiro_humano():
     print("**SEJA BEM VINDO JOGADOR**")
     Nome=input("DIGITE SEU NOME ")
     a_h={
  
    "vida": 8,
    "ataque": 5,
    "defesa": 3,
    "esquiva": 2,
    "nivel":1,
    "exp":0}
     time_devagar("Configurando seu personagem....\n")
     print(f"\033[1;30;47m{"///// SEUS STATUS /////"}\033[m")
     print(f"jogador : \033[32m{Nome}\033[m")
     print(a_h)
     return a_h
 
def arqueiro_elfo():
     print(f"\033[1;30;47m{"///// SEUS STATUS /////"}\033[m")
     print(f"jogador : \033[32m{Nome}\033[m")
     a_e={
  
    "vida": 7,
    "ataque": 5,
    "defesa": 2,
    "esquiva": 3,
    "nivel":1,
    "exp":0}
     time_devagar("Configurando seu personagem....\n")
     print(f"\033[1;30;47m{"///// SEUS STATUS /////"}\033[m")
     print(f"jogador : \033[32m{Nome}\033[m")
     print(a_e)
     return a_e
 
def arqueiro_anao():
     print("**SEJA BEM VINDO JOGADOR**")
     Nome=input("DIGITE SEU NOME ")
     a_a={

    "vida": 7,
    "ataque": 5,
    "defesa": 2,
    "esquiva": 3,
    "nivel":1,
    "exp":0}
     time_devagar("Configurando seu personagem....\n")
     print(f"\033[1;30;47m{"///// SEUS STATUS /////"}\033[m")
     print(f"jogador : \033[32m{Nome}\033[m")
     print(a_a)
     return a_a
 
def paladino_humano():
     print("**SEJA BEM VINDO JOGADOR**")
     Nome=input("DIGITE SEU NOME ")
     p_h={

    "vida": 10,
    "ataque": 4,
    "defesa": 3,
    "esquiva": 0,
    "nivel":1,
    "exp":0}
     time_devagar("Configurando seu personagem....\n")
     print(f"\033[1;30;47m{"///// SEUS STATUS /////"}\033[m")
     print(f"jogador : \033[32m{Nome}\033[m")
     print(p_a)
     return p_h
def paladino_elfo():
     print("**SEJA BEM VINDO JOGADOR**")
     Nome=input("DIGITE SEU NOME ")
     p_e={

    "vida": 9,
    "ataque": 4,
    "defesa": 2,
    "esquiva": 1,
    "nivel":1,
    "exp":0}
     time_devagar("Configurando seu personagem....\n")
     print(f"\033[1;30;47m{"///// SEUS STATUS /////"}\033[m")
     print(f"jogador : \033[32m{Nome}\033[m")
     print(p_e)
     return p_e

def paladino_anao():
     print("**SEJA BEM VINDO JOGADOR**")
     Nome=input("DIGITE SEU NOME ")
     p_a={

    "vida": 10,
    "ataque": 3,
    "defesa": 3,
    "esquiva": 0,
    "nivel":1,
    "exp":0}
     time_devagar("Configurando seu personagem....\n")
     print(f"\033[1;30;47m{"///// SEUS STATUS /////"}\033[m")
     print(f"jogador : \033[32m{Nome}\033[m")
     print(p_a)
     return p_a
