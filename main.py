import random
import sys
import os
import time
import numpy as np
from prints import *
from map import *
from grafo import *
from Node import *
from Pista import *


# Função main
def main():
    os.system('clear')
    var = -1
    while var != 0:
        menu()
        print("[1] - Gera Circuito")
        print("[2] - Gera Matriz correspondente ao Circuito escolhido")
        print("[3] - Mostrar Circuito Guardado")
        print("[4] - Cria Grafo")
        print("[5] - Correr Algoritmos")
        print("[0] - Saír")
        var = int(input("introduza a sua opcao-> "))
        if var == 0:
            print("Saindo.......")
        elif var == 1:
            largura = int(input("ESCOLHA A SUA LARGURA -> "))
            altura = int(input("ESCOLHA A SUA ALTURA -> "))
            open('mapa.txt', 'w').close()
            gera_mapa(largura,altura)
            l=input("Prima enter para continuar")
            os.system('clear')
            
        elif var == 2:
            print(converte_matrix())
            l=input("Prima enter para continuar")
            os.system('clear')
        elif var == 3:
            print_matrix()
            l=input("Prima enter para continuar")
            os.system('clear')
        elif var == 4:
            matrix = converte_matrix()
            start = retorna_coords_posicao(matrix,'P')
            goal = retorna_coords_posicao(matrix,'F')
            jogadorj= retorna_coords_posicao(matrix,'J')
            tP=gera_tuplo(start)
            tF=gera_tuplo(goal)
            tJ= gera_tuplo(jogadorj)
            problema = Pista(tP,tF,matrix,len(matrix),len(matrix[0]))
            problema.cria_grafo()
            problemaJ = Pista(tJ,tF,matrix,len(matrix),len(matrix[0]))
            problemaJ.cria_grafo()
            print("========> [GRAFO DO JOGADOR P]")
            print(problema.g)
            print(" ")
            print("========> [GRAFO DO JOGADOR J]")
            print(problemaJ.g)
            l=input("Prima enter para continuar")
            os.system('clear')
        elif var == 5:
            print("[1] -> Algoritmo DFS")
            print("[2] -> Algoritmo BFS")
            print("[3] -> Algoritmo aStar")
            print("[4] -> Algoritmo Greedy")
            varP = int(input("Escolha um algoritmo para o jogador P -> "))
            varJ = int(input("Escolha um algoritmo para o jogador J -> "))
            matrix_copia = converte_matrix()

            matrix = converte_matrix()
            jogadorP = retorna_coords_posicao(matrix,'P')
            goal = retorna_coords_posicao(matrix,'F')
            jogadorJ= retorna_coords_posicao(matrix,'J')
            tP=gera_tuplo(jogadorP)
            tF=gera_tuplo(goal)
            tJ= gera_tuplo(jogadorJ)
            problema = Pista(tP,tF,matrix,len(matrix),len(matrix[0]))
            problema.cria_grafo()
            problemaJ = Pista(tJ,tF,matrix,len(matrix),len(matrix[0]))
            problemaJ.cria_grafo()

            match varP:
                case 1:
                    caminho=problema.solucaoDFS(str(tP),str(tF))                                # Gera a solucao BFS para o jogador P
                case 2:
                    caminho=problema.solucaoBFS(str(tP),str(tF))
                case 3:
                    caminho=problema.solucaoAstar(str(tP),str(tF))
                case 4:
                    caminho=problema.solucaoGreedy(str(tP),str(tF))

            match varJ:
                case 1:
                    caminhoJ=problemaJ.solucaoDFS(str(tJ),str(tF))                                # Gera a solucao BFS para o jogador P
                case 2:
                    caminhoJ=problemaJ.solucaoBFS(str(tJ),str(tF))
                case 3:
                    caminhoJ=problemaJ.solucaoAstar(str(tJ),str(tF))
                case 4:
                    caminhoJ=problemaJ.solucaoGreedy(str(tJ),str(tF))

            printsAlgoritmos(varP, varJ, caminho, caminhoJ) 
            print("Tracking do caminho iniciando em breve....")
            time.sleep(5)
            tracking(caminho,caminhoJ,matrix_copia)

            print("O custo do Jogador P:"+ str(caminho[1]))
            print("O custo do Jogador J:"+ str(caminhoJ[1]))
            l=input("Prima enter para continuar")
            os.system('clear')

# Função que lê de um ficheiro um circuito e transforma-o em matrix
def converte_matrix():
    fin = open('mapa.txt','r')
    matrix=[]
    for line in fin.readlines():
        matrix.append( [ str(x) for x in line.split() ] )
    return matrix

# Função que devolve para cada posição "P" ou "F", uma lista com os tuplos das suas coordenadas
def retorna_coords_posicao(matrix,posicao):
    #a = np.array(matrix)
    #print(np.where(a=='P'))
        if (posicao == 'P'):
            resultado = [(cordx,cordy) for cordx, row in enumerate(matrix) for cordy, i in enumerate(row) if i == 'P']
            return resultado
        elif (posicao == 'F'):
            resultado = [(cordx,cordy) for cordx, row in enumerate(matrix) for cordy, i in enumerate(row) if i == 'F']
            return resultado
        elif (posicao == 'J'):
            resultado = [(cordx,cordy) for cordx, row in enumerate(matrix) for cordy, i in enumerate(row) if i == 'J']
            return resultado
        else :
            return None

def gera_tuplo(lista):
    listaNova = lista[0]
    tuploN = (int(listaNova[0]),int(listaNova[1]), 0, 0)
    return tuploN

def tracking(caminho1,caminho2,matrix):
    i=-1
    for c,r in zip(caminho1[0],caminho2[0]):
                i+=1
                x = c[1:-1].split(',')
                x1 = int(x[0])
                x2 = int(x[1])
               
                w = r[1:-1].split(',')
                w1 = int(w[0])
                w2 = int(w[1])
                matrix[x1][x2] = 'P'
                matrix[w1][w2] = 'J'
                z = 0
                k = 0
                os.system('clear')
                
                while (z < len(matrix)):
                    strr = ""
                    while (k < len(matrix[z])):
                
                        strr += matrix[z][k]
                        strr += " "
                        k = k+1
                
                    k = 0
                    print(strr)
                    z += 1
                time.sleep(0.5)
                matrix[x1][x2] = '-'
                matrix[w1][w2] = '-'
    if(len(caminho1[0]) >len(caminho2[0])):
        l1=caminho1[0]
        l2=caminho2[0]
        r=l2[i]
        w = r[1:-1].split(',')
        w1 = int(w[0])
        w2 = int(w[1])
        for i in range(i, len(l1)):
            x = l1[i][1:-1].split(',')
            x1 = int(x[0])
            x2 = int(x[1])
            """c = l1[i])
            x1 = int(c[0])
            x2 = int(c[1])"""
            matrix[x1][x2] = 'P'
            matrix[w1][w2] = 'J'
            z = 0
            k = 0
            os.system('clear')
            
            while (z < len(matrix)):
                strr = ""
                while (k < len(matrix[z])):
                    strr += matrix[z][k]
                    strr += " "
                    k = k+1
                
                k = 0
                print(strr)
                z += 1
            time.sleep(0.5)
            matrix[x1][x2] = '-'
    elif (len(caminho1[0]) < len(caminho2[0])):
        l2=caminho2[0]
        l1=caminho1[0]
        c=l1[i]
        x = c[1:-1].split(',')
        x1 = int(x[0])
        x2 = int(x[1])
        for i in range(i, len(l2)):
            r = l2[i][1:-1].split(',')
            w1 = int(r[0])
            w2 = int(r[1])
            matrix[x1][x2] = 'P'
            matrix[w1][w2] = 'J'
            z = 0
            k = 0
            os.system('clear')
            
            while (z < len(matrix)):
                strr = ""
                while (k < len(matrix[z])):
                    strr += matrix[z][k]
                    strr += " "
                    k = k+1
                
                k = 0
                print(strr)
                z += 1
            time.sleep(0.5)
            matrix[w1][w2] = '-'            

def printsAlgoritmos(x, y, caminho, caminhoJ): 
     
     print(" ")
 
     if (x == 1):
         print_dfs()
     elif(x == 2):
         print_bfs()
     elif(x == 3):
         print_astar()
     elif(x == 4):
         print_greedy()
 
     print("===> Caminho do Jogador P")
     print(caminho)
     print(" ")
 
     if (y == 1):
         print_dfs()
     elif (y == 2):
         print_bfs()
     elif (y == 3):
         print_astar()
     elif (y == 4):
         print_greedy()
 
     print("===> Caminho do jogador J")
     print(caminhoJ)
     print(" ")

            

if __name__ == "__main__":
    main()