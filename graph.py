#m = grado_medio(G)
# /2 se e' orientato
import matplotlib.pyplot as plt
import networkx as nx
import random

class Node:
    def __init__(self,n):
        self.label=n
        self.adj = set() 
    def addEdge(self,label):
        self.adj.add(label) 
    def subEdge(self,label):
        # elimina arco dal grafo,
        # se non esiste non fa niente
        # tempo: O(1)
        if label in self.adj: self.adj.remove(label)
    
class Graph(object):
    def __init__(self):
        self.nodesLabel=set() 
        self.nodes={} #dict

    def addNode(self,label):
        # tempo: O(1)
        if label not in self.nodes:
            self.nodes[label]=Node(label)
            self.nodesLabel.add(label)
    
    def checkNode(self,label):
        if label not in self.nodes: 
            self.addNode(label)
        return self.nodes[label]
    
    def subNode(self,label):
        if label in self.nodes:
            self.nodes.pop(label)
            self.nodesLabel.remove(label)
            for i in self.nodes:
                self.nodes[i].subEdge(label)

    def buildGraph(self,G):
        for node in self.nodes:
            G.add_node(self.nodes[node].label)
        for node in self.nodes:
            for tail in self.nodes[node].adj: 
                G.add_edge(self.nodes[node].label,tail)
        return G

    def get_Nodes_N (self):
        return len(self.nodes)

    def get_Max_Degree_Node(self):
        pass


class NotOrientedGraph(Graph):
    def __init__(self):
        Graph.__init__(self)

    def addEdge(self,n1L,n2L):
        #se i nodi non esistono li creo
        # se l'arco e' illegale (cappio) ignoro l'aggiunta
        if n1L != n2L:
            self.checkNode(n1L).adj.add(n2L)
            self.checkNode(n2L).adj.add(n1L)

    def plotGraph(self):
        G=self.buildGraph(nx.Graph())
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()

    def get_Max_Degree_Node(self):  
        max_label=random.sample(self.nodesLabel,1)[0]
        for label in self.nodes:
            if len(self.nodes[max_label].adj) < len(self.nodes[label].adj):
                max_label=label
        return max_label



class OrientedGraph(Graph):
    def __init__(self):
        Graph.__init__(self)

    def addEdge(self,n1L,n2L):
        # se i nodi non esistono li creo
        # se l'arco e' illegale (cappio) ignoro l'aggiunta
        if n1L != n2L:
            self.checkNode(n1L).adj.add(n2L)

    def plotGraph(self):
        G=self.buildGraph(nx.DiGraph())
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()
        
        # for i in range(1,10) -> intervallo [1,10]
        # for i in range(10) -> intervallo [0,10]
        # [i for i in range(10)]
        # [i+j for i in range(10) if i!=j[for j in range(10)]]
