
from Node import Node
from grafo import Graph
from queue import Queue

class Pista():

    def __init__(self, start, goal,matrix,linha,coluna):
        self.g=Graph(directed=True) # Grafo
        self.start=start # Posição Start
        self.goal=goal # Posição End
        self.matrix = matrix # Matrix correspondente ao grafo
        self.linha = linha # Número de linhas da matrix
        self.coluna = coluna # Número de colunas da matrix

    # Serve para criar o grafo à medida que passa por todos os nodos
    def cria_grafo(self):
        estados = [] # Lista dos nodos por expandir
        estados.append(self.start) # adicionado o estado inicial
        #self.g.m_nodes.append(Node(self.start[0],self.start[1]))
        #self.g.m_graph[self.start] = set()
        visitados = [] # Lista que guarda todos os nodos visitados(expandidos)
        visitados.append(self.start) # Adicionamos o estado inicial ao estados visitados


        while estados != []:  # O ciclo executa enquanto houver nodos por expandir
            estado = estados.pop() #Retira o último elemento da lista
            expansao = self.expande(estado) # expansao é uma lista que contém todos os estados possiveis a partir do estado atual que nos encontramos
            for e in expansao:                               # Para cada caminho possivel a partir do tuplo "e"
                self.g.add_edge(str(estado), str(e),1)        # add_edge(Tuplo, Caminho possivel, custo)
                if e not in visitados: 
                    estados.append(e)
                    visitados.append(e)



# Serve para obter numa lista, todos os estados possiveis a partir do estado atual que nos encontramos
    def expande(self, estado):
        possibilidades = []

        acels = [[0,0],[1,0],[0,1],[-1,0],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        
        for aceleratings in acels:

            novo_nodo = self.check_acel(estado, aceleratings)
            if novo_nodo is not None:
                possibilidades.append(novo_nodo)
        

        return possibilidades
        
        
        
        
    def check_acel(self, estado, acel):       
        
        velx = estado[2] + acel[0] 
        vely = estado[3] + acel[1]
        
        # Forma de verificar se o nodo é valido ou não

        novo = (estado[0] + velx, estado[1] + vely, velx, vely)# Novas posiçoes e novas velocidades [x,y, velocidadeX, velocidadeY]
        
        if novo[0] < self.linha and novo[0] > 0 and novo[1] < self.coluna and novo[1] > 0 and self.matrix[novo[0]][novo[1]] != '#':

            if estado[0] > novo[0]:
                xmax = estado[0]
                xmin = novo[0]
            else:
                xmax = novo[0]
                xmin = estado[0]

            if estado[1] > novo[1]:
                ymax = estado[1]
                ymin = novo[1]
            else:
                ymax = novo[1]
                ymin = estado[1]


            for x in range(xmin, xmax+1):
               for y in range(ymin, ymax+1):
                   if self.matrix[x][y] == "#":
                       return None

    
        else:
            return None

        return novo

    



    # Aplica a Procura BFS
    def solucaoBFS(self,start,goal):
        return self.g.procura_BFS(str(start),str(goal))

    # Aplica a Procura DFS
    def solucaoDFS(self,start,goal):
        res=self.g.procura_DFS(str(start),str(goal),path=[], visited=set())
        return (res)

    # Aplica a Procura aStar
    def solucaoAstar(self,start,goal):
        self.g.heuristica(goal)
        return self.g.procura_aStar(str(start),str(goal))

    # Aplica a Procura Greedy
    def solucaoGreedy(self,start,goal):
        self.g.heuristica(goal)
        return self.g.procura_greedy(str(start),str(goal))
