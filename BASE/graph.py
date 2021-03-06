#m = grado_medio(G)
# /2 se e' orientato
import matplotlib.pyplot as plt
import networkx as nx
import random

class Node:
    def __init__(self,n):
        self.label=n
        self.adj_out = set()
        #la lista delle adiacenze in entrata non e' necessaria
        #essa e' ridondante, dublica le informazioni presenti in adj_out
        #e' stata inserita per permettere un'eliminazione efficiente dei nodi in un
        #grafo orientato
        self.adj_in = set()
    def addEdge(self,n2):
        self.adj_out.add(n2.label)
        n2.adj_in.add(self.label)
    def subEdge(self,label):
        # elimina l'arco dal grafo,
        # se non esiste non fa niente
        # tempo: O(1)
        if label in self.adj_in: self.adj_in.remove(label)
        if label in self.adj_out: self.adj_out.remove(label)

    def degree(self):
        return len(self.adj_out)
    def in_degree(self):
        return len(self.adj_in)
    
class Graph(object):
    def __init__(self):
        self.nodesLabel=set()
        self.nodes={} #dict
        self.maxDegree=''

    def addNode(self,label):
        # tempo: O(1)
        if label not in self.nodes:
            self.maxDegree=label
            self.nodes[label]=Node(label)
            self.nodesLabel.add(label)
    
    def checkNode(self,label):
        if label not in self.nodes: 
            self.addNode(label)
    
    def subNode(self,label):
        if label in self.nodes:
            for l in self.nodes[label].adj_out:
                self.nodes[l].subEdge(label)
            for l in self.nodes[label].adj_in:
                self.nodes[l].subEdge(label)
            self.nodes.pop(label)
            self.nodesLabel.remove(label)

    def buildGraph(self,G):
        for node in self.nodes:
            G.add_node(self.nodes[node].label,size=self.nodes[node].out_degree()/100)
        for node in self.nodes:
            for tail in self.nodes[node].adj_in: 
                G.add_edge(self.nodes[node].label,tail,width=0.0001)
        return G

    def get_Nodes_N (self):
        return len(self.nodes)

    def get_Max_Degree_Node(self):
        pass

    def avg_out_degree(self):
        return float(sum([self.nodes[label].degree() for label in self.nodes]))/len(self.nodes)

    def writeOnFile(self,nm):
        f=open(nm+'.txt','a')
        for l in self.nodes:
            for out in self.nodes[l].adj_out:
                f.write(str(l)+'\t'+str(out)+'\n')

class NotOrientedGraph(Graph):
    def __init__(self):
        Graph.__init__(self)

    def addEdge(self,n1L,n2L):
        #se i nodi non esistono li creo
        # se l'arco e' illegale (cappio) ignoro l'aggiunta
        if n1L != n2L:
            self.checkNode(n1L)
            self.checkNode(n2L)
            self.nodes[n1L].addEdge(self.nodes[n2L])
            self.nodes[n2L].addEdge(self.nodes[n1L])

    def plotGraph(self):
        G=self.buildGraph(nx.Graph())
        d={}
        for (node, val) in G.degree():
            d[node]=val

        nx.draw(G, nodelist=d.keys(),node_size=d.values())
        plt.show()

    def get_Max_Degree_Node(self):  
        max_label=random.sample(self.nodesLabel,1)[0]
        for label in self.nodes:
            if len(self.nodes[max_label].adj_out) < len(self.nodes[label].adj_out):
                max_label=label
        return max_label

    def avg_degree(self):
        return self.avg_out_degree()

    def getEdgeNumber(self):
        edge=0
        for label in self.nodes:
            edge+=self.nodes[label].out_degree()
        return edge/2

class OrientedGraph(Graph):
    def __init__(self):
        Graph.__init__(self)

    def addEdge(self,n1L,n2L):
        # se i nodi non esistono li creo
        # se l'arco e' illegale (cappio) ignoro l'aggiunta
        if n1L != n2L:
            self.checkNode(n1L)
            self.checkNode(n2L)
            self.nodes[n1L].addEdge(self.nodes[n2L])

    def plotGraph(self):
        G=self.buildGraph(nx.DiGraph())
        d={}
        for (node, val) in G.degree():
            d[node]=val
        nx.draw(G, nodelist=d.keys(),node_size=d.values())
        plt.show()
        
        # for i in range(1,10) -> intervallo [1,10]
        # for i in range(10) -> intervallo [0,10]
        # [i for i in range(10)]
        # [i+j for i in range(10) if i!=j[for j in range(10)]]
