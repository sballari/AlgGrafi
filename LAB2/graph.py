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
        # adj: insieme di etichette dei nodi adiacenti
        self.adj = []
    
    def addEdge(self,dest,oraP,oraA,codCorsa,codLin):
        # desc : inserisce un arco dal nodo attuale , ordine ora arrivo
        # dest: label staz di destinazione
        # oraP : orario di partenza 
        # oraA : orario arrivo
        # tempo: O(log(n))
        self.orderedInsert(self.adj,dest,oraP,oraA,codCorsa,codLin,len(self.adj)-1,False)
        
    @staticmethod
    def orderedInsert(list_,dest,oraP,oraA,codCorsa,codLin,lim,sxdx):
        # desc : inserisce un arco dal nodo attuale , ordine ora arrivo
        # list: lista delle adiacenze
        # dest: label staz di destinazione
        # oraP : orario di partenza 
        # oraA : orario arrivo
        # sxdx = false sinistra , true destra, 
        # lim = indice LIMITE COMPRESO sx o dx in cui fare l'inserimento,prima volta len-1
        #       Chunk = sx : [0,lim], dx: [lim,n-1]
        # tempo: O(log(n))

        dim=0 #dimensione del chunk
        if sxdx == False : dim = lim+1
        else : dim = len(list_) - lim
        
        if (dim!=0) :
            i = dim//2 #lower bound
            oraPi = (list_[i])[1]

            if oraP < oraPi: 
                Node.orderedInsert(list_,dest,oraP,oraA,codCorsa,codLin,i-1,False)
            if oraP > oraPi: 
                Node.orderedInsert(list_,dest,oraP,oraA,codCorsa,codLin,i+1,True)
            if oraP == oraPi: list_.insert(i,[dest,oraA,oraP,codCorsa,codLin])
        else: 
            list_.insert(lim,[dest,oraA,oraP,codCorsa,codLin])
    
class Graph(object):
    def __init__(self):
        # desc : costruttore della classe grafo
        # tempo : O(1)

        # nodes : dizionario {label -> oggetto nodo}
        self.nodes={} 

    def addNode(self,label):
        # desc : aggiunge un oggetto nodo al grafo
        # label : label del nodo che si vuole aggiungere
        # tempo: O(1)
        if label not in self.nodes:
            self.nodes[label]=Node(label)

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

    def writeOnFile(self,nm):
        # desc : crea un file con le tabelle delle adiacenze del grafo
        # nm : nome del file su cui scrivere
        f=open(nm+'.txt','a')
        for l in self.nodes:
            for out in self.nodes[l].adj_out:
                f.write(str(l)+'\t'+str(out)+'\n')

class OrientedGraph(Graph):
    # desc : crea un grafo orientato
    def __init__(self):
        Graph.__init__(self)

    def addEdge(self,stazA,stazB,oraP,oraA,codCorsa, codLin):
        # desc : crea un arco orientato: n1L -> n2L 
        #        se i nodi non esistono li crea,
        #        se l'arco e' illegale (cappio) ignora l'aggiunta
        #        se archi // allora legali   
        # stazA : label del nodo di partenza
        # stazB : label del nodo di arrivo
        # codCorsa : 
        # codLin : 
        # tempo : O(log n)
        if stazA != stazB: #evita i cappi
            self.addNode(stazA)
            self.addNode(stazB)
            self.nodes[stazA].addEdge(stazB,oraP,oraA,codCorsa,codLin)

    def plotGraph(self):
        # desc : crea una struttura networkX e la usa per plottare il grafo
        G=self.buildGraph(nx.Graph())
        d={}
        for (node, val) in G.degree():
            d[node]=val

        nx.draw(G, nodelist=d.keys(),node_size=d.values())
        plt.show()

    def get_Max_Degree_Node(self):  
        # desc : restituisce la label del nodo con in-degree maggiore
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
        return edge

    # [(staz_p, staz_a, ora_p, ora_a, cod_corsa, cod_lin)]

    @staticmethod
    def inputGraph(f):
        # desc: crea un grafo orientato 
        #       preso dal file indicato
        # f : nome del file da cui attingere
        
        f=open(f,'r')
        s = f.read()
        s=s.split('\n')
        for i in range(len(s)):
            s[i]=s[i].split('\t') #array in N^2
        G = OrientedGraph()
        for i in range(len(s)-1):
            G.addEdge(s[i][0],s[i][1])
    
        return G