import bibMatriz
import random
import time

cont = 0
while(cont < 1):
    
    #Menu do jogo
    escolhas = ["0", "1", "2"]
    print("Bem-vindo(a)(s), caçadores de tesouros! \n\n(1) Iniciar jogo. \n(2) Tutorial. \n(0) Sair. \n")
    escolha = input("Faças uma escolha: ")
    print()
    #Menu do jogo

    #Jogo 
    if (escolha == "1"):
        #Matrizes
        matriz = []
        matrizVazia = []
        #Retorna matriz vazia
        matrizVazia = bibMatriz.matriz(matrizVazia)
        #Retorna matriz com valores
        matriz = bibMatriz.matrizValores(matriz)

        #Lista das coordenadas
        letras = ["a","b","c","d"]
        numeros = ["1","2","3","4"]
        
        #Interação dos usuários
        print("Escolheste aventurar-se numa enorme caça ao tesouro! Boa sorte... e precisarás! (Gargalhadas!)")
        print()
        jogador1 = input("Digites o nome do(a) primeiro(a) caçador(a) de tesouros: ") #Nome do jogador 1
        print(jogador1+", tu serás o(a) caçador(a) 1, ok?")
        pontuacao1 = 0 #Pontuação do jogador 1
        print()
        jogador2 = input("Digites o nome do(a) segundo(a) caçador(a) de tesouros: ") #Nome do jogador 2
        print(jogador2+", tu serás o(a) caçador(a) 2, ok?")
        pontuacao2 = 0 #Pontuação do jogador 2
        print()
        bibMatriz.exibeMatriz(matrizVazia) #Exibe a matriz inicial
        print()
        interacao = input("Este será o nosso mapa, caçadores(as)! Cavais escolhendo primeiro uma linha(letra) e depois uma coluna(número) e ficais ricos(as) encontrando tesouros, entretanto tomes cuidado com os buracos! Prontos(as)?! Pressiones enter!")
        print()
        
        jogadas = 8
        for i in range(jogadas):
            #Jogada do jogador 1
            jog1 = 0
            while(jog1 < 1):
                jLinha = str.lower(input("Caçador(a) 1, penses bem antes de cavares! Escolhas uma letra (a, b, c ou d): ")) #Usuário seleciona a linha
                jColuna = str.lower(input("Escolhas agora um número (1, 2, 3 ou 4): ")) #Usuário seleciona a coluna
                print()
                if((jLinha in letras) and (jColuna in numeros)): #Somente se ele informar os valores das coordenadas válidas satisfaz-se esta condição
                    x = int(jColuna) #Transformando o valor da coluna de string para inteiro
                    #Predefinindo os valores das colunas em inteiro
                    if(jLinha == "a"):
                        y = 1
                    elif(jLinha == "b"):
                        y = 2
                    elif(jLinha == "c"):
                        y = 3
                    elif(jLinha == "d"):
                        y = 4
                    #Evitando o usuário sobrepor valores já revelados
                    if(matrizVazia[y][x] == "[ ]"):
                        if(jLinha == "a"):
                            matrizVazia[y][x] = matriz[1][x]     
                        elif(jLinha == "b"):
                            matrizVazia[y][x] = matriz[2][x]
                        elif(jLinha == "c"):
                            matrizVazia[y][x] = matriz[3][x]
                        elif(jLinha == "d"):
                            matrizVazia[y][x] = matriz[4][x]
                        #Aumentando pontuação caso encontre tesouro
                        if(matrizVazia[y][x] == "[T]"):
                            pontuacao1 += 50
                            print("Parabéns, caçador 1, encontraste um tesouro! Comemores muito!")
                            print()
                            time.sleep(1)
                        #Diminuindo pontuação caso encontre um buraco
                        elif(matrizVazia[y][x] == "[B]"):
                            pontuacao1 -= 30
                            print("Socorroooo! O caçador 1 caiu em um buraco!")
                            print()
                            time.sleep(1)
                        elif(matrizVazia[y][x] == "[0]"):
                            print("A ideia de cavares neste local não foi das melhores, caçador 1! Tentes um pouco mais distante!")
                            print()
                            time.sleep(1)
                        else:
                            print("Caçador 1, sentes o cheiro do tesouro? Ele está próximo de ti!")
                            print()
                            time.sleep(1)
                        jog1 += 1
                    else:
                        print("Local já cavado. Caves novamente em outro lugar!") #Mensagem de sobreposição
                        print()
                else:
                    print("Este local não pertence a este mapa. Caves novamente em outro local.") #Mensagem de jogada inválida, pois os valores da coordenadas informados não satisfazem a condição if
                    print()
            bibMatriz.exibeMatriz(matrizVazia)
            print()
            print("Pontuação de", jogador1+" (caçador(a) 1):", pontuacao1) #Exibindo pontuação do primeiro jogador
            print("Pontuação de", jogador2+" (caçador(a) 2):", pontuacao2) #Exibindo pontuação do segundo jogador
            print()

            #Jogada do jogador 2
            #Mesma configurações da jogada do jogador 1
            jog2 = 0
            while(jog2 < 1):
                jLinha2 = str.lower(input("Caçador(a) 2, observes bem onde cavas! Escolhas uma letra (a, b, c ou d): "))
                jColuna2 = str.lower(input("Escolhas agora um número (1, 2, 3, 4): "))
                print()
                if((jLinha2 in letras) and (jColuna2 in numeros)):
                    x = int(jColuna2)
                    if(jLinha2 == "a"):
                        y = 1
                    elif(jLinha2 == "b"):
                        y = 2
                    elif(jLinha2 == "c"):
                        y = 3
                    elif(jLinha2 == "d"):
                        y = 4
                    if(matrizVazia[y][x] == "[ ]"):
                        if(jLinha2 == "a"):
                            matrizVazia[y][x] = matriz[1][x]     
                        elif(jLinha2 == "b"):
                            matrizVazia[y][x] = matriz[2][x]
                        elif(jLinha2 == "c"):
                            matrizVazia[y][x] = matriz[3][x]
                        elif(jLinha2 == "d"):
                            matrizVazia[y][x] = matriz[4][x]
                        if(matrizVazia[y][x] == "[T]"):
                            pontuacao2 += 50
                            print("Parabéns, caçador 2, encontraste um tesouro! Comemores muito!")
                            print()
                            time.sleep(1)
                        elif(matrizVazia[y][x] == "[B]"):
                            pontuacao2 -= 30
                            print("Socorroooo! O caçador 2 caiu em um buraco!")
                            print()
                            time.sleep(1)
                        elif(matrizVazia[y][x] == "[0]"):
                            print("A ideia de cavares neste local não foi da melhores, caçador 2! Tentes um pouco mais distante!")
                            print()
                            time.sleep(1)
                        else:
                            print("Caçador 2, sentes o cheiro do tesouro? Ele está perto de ti!")
                            print()
                            time.sleep(1)
                        jog2 += 1
                    else:
                        print("Local já cavado. Caves novamente em outro lugar!")
                        print()
                else:
                    print("Este local não pertence a este mapa. Caves novamente em outro local!")
                    print()
            bibMatriz.exibeMatriz(matrizVazia)
            print()
            print("Pontuação de", jogador1+" (caçador(a) 1):", pontuacao1)
            print("Pontuação de", jogador2+" (caçador(a) 2):", pontuacao2)
            print()

        #Mensagem de vitória
        time.sleep(3)
        if(pontuacao1 > pontuacao2):
            print("***Fim de jogo!*** Parabéns,", jogador1+",", "és um sinônimo de riqueza! És o caçador mais rico em toda esta ilha!")
            print()
        elif(pontuacao1 < pontuacao2):
            print("***Fim de jogo!*** Parabéns,", jogador2+",", "és um sinônimo de riqueza! És o caçador mais rico em toda esta ilha!")
            print()
        else:
            print("***Fim de jogo!*** Vós sois os caçadores mais ricos em toda a ilha e não há alguém como vós!")
            print()
        voltar = input("Pressiones enter para voltar ao início.")
        print()

    #Tutorial do jogo
    elif (escolha == "2"):
        matrizVazia = []
        #Retorna a matriz vazia
        matrizVazia = bibMatriz.matriz(matrizVazia)
        bibMatriz.exibeMatriz(matrizVazia)
        print()
        print("Acima está representado o mapa do tesouro. \n\n1: 8 jogadas para cada caçador. \n2: Para escolheres onde vais cavar, escolhas uma linha(letra) e uma coluna(número). \n3: Os tesouros estão representados pela letra T, enquanto os buracos pela letra B. Os números indicam a quantidade de tesouros adjacentes àquele local. \n4: Ao encontrares um tesouro, será acrescentada à tua pontuação 50 pontos; todavia, se caires em um buraco, tua pontuação será diminuída em 30 pontos.")
        escolha = input("Para voltares tecle enter! ")
        print()
        
    #Comando para sair    
    elif (escolha == "0"):
        print("Adeus, caçadores(as)! Até a próxima!")
        time.sleep(2)
        cont += 1
        
    else:
        print("Escolha inválida!")
        print()
