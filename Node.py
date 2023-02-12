
# Classe nodo para definiçao dos nodos
class Node:
    def __init__(self,name):     #  construtor do nodo"
        self.m_name = name       # posição linha(x,y), velocidade x, velocidade y (tuplo de 4 elementos)
 
    def __str__(self):
        return "node" + self.m_name

    def __repr__(self):
        return "node" + self.m_name

    def setName(self,name):
        self.m_name = name

    def getName(self):
        return self.m_name

    def __eq__(self, other):
        return self.m_name == other.m_name # 2 nodos são iguais se a sua posição(x,y) e velocidades(vx,vy) forem iguais

    def __hash__(self):
        return hash(self.m_name)
