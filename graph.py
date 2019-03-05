import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self,n):
        self.label=n
        self.adj = []
    def addEdge(self,label):
        self.adj.append(label)

class Graph:
    def __init__(self):
        self.nodes={}
    def addNode(self,node):
        if node.label not in self.nodes:
            self.nodes[node.label]=node
    def addEdge(self,startL,endL):
        #se i nodi non esistono li creo
        #if startL in self.nodes:

    def plotGraph(self):
        G = nx.Graph()
        
        for node in self.nodes:
            G.add_node(node.label)
        for node in self.nodes:
            for tail in node.adj: 
                G.add_edge(node.label,tail)
        
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()


        # for i in range(1,10) -> intervallo [1,10]
        # for i in range(10) -> intervallo [0,10]
        # [i for i in range(10)]
        # [i+j for i in range(10) if i!=j[for j in range(10)]]