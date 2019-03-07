import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self,n):
        self.label=n
        self.adj = []
    def addEdge(self,label):
        self.adj.append(label)
    def subEdge(self,label):
        if label in self.adj: self.adj.remove(label)
    
class Graph:
    def __init__(self):
        self.nodes={}
    def addNode(self,node):
        if node.label not in self.nodes:
            self.nodes[node.label]=node
    def addEdge(self,startL,endL):
        #se i nodi non esistono li creo
        n1=0
        n2=0
        if startL in self.nodes:
            n1=self.nodes[startL]
        else:
            n1=Node(startL)
            self.nodes[startL]=n1
        if endL in self.nodes:
            n2=self.nodes[endL]
        else:
            n2=Node(endL)
            self.nodes[endL]=n2
        self.nodes[startL].addEdge(endL)
    def addDoubleEdge(self,startL,endL):
        #se i nodi non esistono li creo
        self.addEdge(startL,endL)
        self.nodes[endL].addEdge(startL)
    def subNode(self,label):
        if label in self.nodes:
            self.nodes.pop(label)
            for i in self.nodes:
                self.nodes[i].subEdge(label)
    def plotGraph(self):
        G = nx.Graph()
        
        for node in self.nodes:
            G.add_node(self.nodes[node].label)
        for node in self.nodes:
            for tail in self.nodes[node].adj: 
                G.add_edge(self.nodes[node].label,tail)
        
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()


        # for i in range(1,10) -> intervallo [1,10]
        # for i in range(10) -> intervallo [0,10]
        # [i for i in range(10)]
        # [i+j for i in range(10) if i!=j[for j in range(10)]]
