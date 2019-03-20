#m = grado_medio(G)
# /2 se e' orientato
import matplotlib.pyplot as plt
import networkx as nx
import random

class Node:
    def __init__(self,n):
        # desc : costruttore oggetto nodo
        # n : label del nodo
        # tempo : O(1)

        # label : etichetta del nodo
        self.label=n
        # adj: insieme di etichette dei nomi 
        self.adj = set() 
    
    def addEdge(self,n2L):
        # desc : inserisce un arco partente dal nodo attuale e in arrivo a n2
        # n2L: label del nodo di arrivo 
        # tempo: O(1)
        self.adj.add(n2L)
        
    def subEdge(self,n2L):
        # desc : elimina l'arco dal grafo partente dal nodo attuale e in arriva sul nodo 
        #        con label n2L, se non esiste non fa niente
        # n2L: arrivo del nodo di arrivo
        # tempo: O(1)
        if n2L in self.adj: self.adj.remove(n2L)

    def degree(self):
        # desc : grado del nodo, numero di archi con cui e' connesso
        # tempo : O(1)
        return len(self.adj) 
    
class Graph(object):
    def __init__(self):
        # desc : costruttore della classe grafo
        # tempo : O(1)

        # nodes : dizionario label -> oggetto nodo
        self.nodes={} 

    def addNode(self,label):
        # desc : aggiunge un oggetto nodo al grafo
        # label : label del nodo che si vuole aggiungere
        # tempo: O(1)
        if label not in self.nodes:
            self.nodes[label]=Node(label)
    
    def checkNode(self,label):
        # desc : verifica se un nodo e' gia' presente nel grafo,
        #        in caso non lo sia lo aggiunge
        # label : label del nodo che si vuole verificare
        # tempo: O(1)
        if label not in self.nodes: 
            self.addNode(label)
    
    def subNode(self,label):
        # desc : elimina un nodo dal grafo e tutti i suoi archi
        # label : label del nodo che si vuole eliminare
        # tempo: O(len(nodes))
        if label in self.nodes:
            for l in self.nodes[label].adj:
                self.nodes[l].subEdge(label)
            self.nodes.pop(label)

    def buildGraph(self,G):
        # desc : popola G con nodi e archi
        # G : oggetto grafo networkx vuoto, 
        #     se il grafo e' diretto va usata networkX.DiGraph altrimenti networkX.Graph
        for node in self.nodes:
            G.add_node(self.nodes[node].label,size=self.nodes[node].degree()/100)
        for node in self.nodes:
            for tail in self.nodes[node].adj: 
                G.add_edge(self.nodes[node].label,tail,width=0.0001)
        return G

    def avg_degree(self):
        # desc : calcola il grado medio del grafo
        # tempo : O(len(nodes))
        return float(sum([self.nodes[label].degree() for label in self.nodes]))/len(self.nodes)

    def writeOnFile(self,nm):
        # desc : crea un file con le tabelle delle adiacenze del grafo
        # nm : nome del file su cui scrivere
        f=open(nm+'.txt','a')
        for l in self.nodes:
            for out in self.nodes[l].adj_out:
                f.write(str(l)+'\t'+str(out)+'\n')

class NotOrientedGraph(Graph):
    # desc : crea un grafo non orientato
    def __init__(self):
        Graph.__init__(self)

    def addEdge(self,n1L,n2L):
        # desc : crea un arco tra i nodi con labael n1L e n2L 
        #        se i nodi non esistono li crea,
        #        se l'arco e' illegale (cappio o //) ignora l'aggiunta
        # n1L : label del nodo di partenza
        # n2L : label del nodo di arrivo
        # tempo : O(1)
        if n1L != n2L:
            self.checkNode(n1L)
            self.checkNode(n2L)
            self.nodes[n1L].addEdge(self.nodes[n2L].label)
            self.nodes[n2L].addEdge(self.nodes[n1L].label)

    def plotGraph(self):
        # desc : crea una struttura networkX e la usa per plottare il grafo
        G=self.buildGraph(nx.Graph())
        d={}
        for (node, val) in G.degree():
            d[node]=val

        nx.draw(G, nodelist=d.keys(),node_size=d.values())
        plt.show()

    def get_Max_Degree_Node(self):  
        # desc : restituisce la label del nodo di grado maggiore
        # tempo : O (len(nodes))
        max_label=random.choice(self.nodes.keys())
        for label in self.nodes:
            if len(self.nodes[max_label].adj) < len(self.nodes[label].adj):
                max_label=label
        return max_label

    def getEdgeNumber(self):
        # desc : restituisce il numero di archi totali del grafo
        # tempo : O(len(nodes))
        edge=0
        for label in self.nodes:
            edge+=self.nodes[label].degree()
        return edge/2

    @staticmethod
    def inputGraph(f):
        # desc: crea un grafo non orientato 
        #       preso dal file indicato
        # f : nome del file da cui attingere
        
        f=open(f,'r')
        s = f.read()
        s=s.split('\n')
        for i in range(len(s)):
            s[i]=s[i].split('\t')
        G = NotOrientedGraph()
        for i in range(len(s)-1):
            G.addEdge(s[i][0],s[i][1])
    
        return G