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
