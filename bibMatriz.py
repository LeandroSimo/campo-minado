def matriz(matrizVazia): #Função que cria a matriz vazia
    matrizVazia = []

    numero = ["   "," 1 "," 2 "," 3 "," 4 "] #Uma linha com números que representam as coordenadas das colunas
    matrizVazia.append(numero) #Adicionando as coordenadas das colunas à matriz
    letra = [" a ", " b ", " c ", " d "] #Lista de letras que representarão as linhas

    repeticao = 4

    #Cria uma matriz com as representações "[ ]" 4x4
    for i in range(repeticao):
        linha = []
        linha.append(letra[i]) #adiciona respectivamente uma letra da lista letra omo primeiro valor de uma sublista, assim representará as coordenadas das linhas
        for i in range(repeticao):
            coluna = "[ ]"
            linha.append(coluna)
        matrizVazia.append(linha)
        
    return(matrizVazia)

def exibeMatriz(matrizVazia): #Função que exibe a matriz
    repeticaoExibe = 5
    
    for i in range(repeticaoExibe):
        for j in range(repeticaoExibe):
            print(matrizVazia[i][j], end=" ")
        print()

def matrizValores(matriz): #Função que cria a matriz com os valores
    import random

    matriz = [] #Matriz sem valores

    repeticao = 6 #Uma matriz 6x6

    for i in range(repeticao):
        linha = []
        for j in range(repeticao):
            coluna = "[ ]"
            linha.append(coluna)
        matriz.append(linha)

    repeticaoT = 1
    while(repeticaoT <= 6): #Repetir 6 vezes para que este comando possa adicionar seis "[T]" na matriz
        celula = "[T]"
        x = random.randint(1,4) #Sorteando números de 1 a 4 para que os valores fiquem no centro da matriz 6x6 
        y = random.randint(1,4)
        if(matriz[x][y] == "[ ]"):
            matriz[x][y] = celula
            repeticaoT += 1 #Adicionar +1 a esta variável somente se suprir esta condição, assim evita-se sobrepor um valor escrito anteriormente

    repeticaoB = 1
    while(repeticaoB <= 3): #Repetir 3 vezes para que este comando possa adicionar três "[B]" na matriz
        celula = "[B]"
        x = random.randint(1,4)
        y = random.randint(1,4)
        if(matriz[x][y] == "[ ]"):
            matriz[x][y] = celula
            repeticaoB += 1 

    #O motivo da matriz 6x6 foi evitar que este comando tente verificar células fora da matriz, ocasionando erro
    for i in range(1,5): #De 1 a 5 para que os valores sejam substituídos no interior da matriz 6x6
        for j in range(1,5):
            num = 0
            if(matriz[i][j] == "[ ]"):
                if(matriz[i-1][j] == "[T]"): #Verifica-se o mesmo índice da sublista anterior
                    num += 1 #Adiciona-se 1 a cada condição atendida
                if(matriz[i+1][j] == "[T]"): #Verifica-se o mesmo índice da sublista posterior
                    num += 1
                if(matriz[i][j-1] == "[T]"): #Verifica-se o índice anterior da mesma sublista
                    num += 1
                if(matriz[i][j+1] == "[T]"): #Verifica-se o índice posterior da mesma sublista
                    num += 1
                matriz[i][j] = "["+str(num)+"]" #Transforma o valor da variável num em string e o põe na matriz

    return(matriz)
