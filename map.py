import random
from prints import *

# Geração do Mapa Aleatório


#Função que é responsável por gerar uma linha do labirinto usando aleatoriedade. Caso o numero gerado seja entre
#1 e 19, gera uma parede, caso contrário, gera um caminho livre. É de notar que o primeiro e último elemento da
#linha são sempre paredes.

def randomNumb(largura):
    string = ""                                   # Inicializar a String
    hm = largura                                  
    while(hm > 0):
        if (hm == largura or hm == 1):            # Caso seja a primeira ou ultimo nodo...
            string += "#"                         # ... tem de gerar uma parede
            string += " "
        elif ((random.randint(1,100)) < 20):      # Caso o número gerado seja entre 1 e 19...
            string += "#"                         # ... tem de gerar uma parede 
            string += " "
        else:
            string += "-"                         # Para todos os outros casos gera um lugar vazio
            string += " "
        hm = hm - 1
    print(string)                                
    printar_file(string)                          # print da linha para o ficheiro onde se guarda o mapa


def meio(largura,altura):
    hm = altura - 4
    while(hm > 0):
        randomNumb(largura)
        hm = hm - 1
        



def printPlayer(largura):
    string = ""
    x = random.randint(1,largura-3)
    i = 0
    while(i < largura):
        if (x == i): 
            string += "P" # aqui é P
            string += " "
            break
        else: 
            string += "#"
            string += " "
        i = i + 1
    i = i + 1
    x = random.randint(i, largura-2)
    while(i < largura):
        if (x == i):
            string += "J"
            string += " "
        else:
            string += "#"
            string += " "
        i = i + 1
    print(string)
    printar_file(string)


def printMeta(largura):
    hm = largura
    string = ""
    x = random.randint(2, hm-2)
    while(hm > 0):
        if (x == hm):
            string += "F"
            string += " "
        else:
            string += "#"
            string += " "
        hm = hm - 1
    print(string)
    printar_file(string)
    




def cleanLine(largura):
    string = "#"
    string += " "

    while(largura > 2):
        string += "-"
        string += " "
        largura = largura - 1


    string += "#"
    print(string)
    printar_file(string)

# Função que gera o map aleatóriamente
def gera_mapa(largura,altura):
        printPlayer(largura)
        cleanLine(largura)
        meio(largura,altura)
        cleanLine(largura)
        printMeta(largura)
