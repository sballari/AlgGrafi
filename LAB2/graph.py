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
        self.adj = dict()
    
    def addEdge(self,dest,oraP,oraA,codCorsa,codLin):
        # desc : inserisce un arco dal nodo attuale , ordine ora arrivo
        # dest: label staz di destinazione
        # oraP : orario di partenza 
        # oraA : orario arrivo
        # tempo: O(log(n))
        if dest in self.adj :
            edgeList = self.adj[dest]
            self.orderedInsert(edgeList,oraP,oraA,codCorsa,codLin,len(edgeList)-1,False)
        else :
            self.adj[dest] = [(oraA,oraP,codCorsa,codLin)]
        
    @staticmethod
    def orderedInsert(list_,oraP,oraA,codCorsa,codLin,lim,sxdx):
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

            #i e' un offset
            if sxdx == False : i = i    #SIX
            else : i = lim + i          #DESTRA

            
            oraPi = (list_[i])[1]

            if oraP < oraPi: 
                Node.orderedInsert(list_,oraP,oraA,codCorsa,codLin,i-1,False)
            if oraP > oraPi: 
                Node.orderedInsert(list_,oraP,oraA,codCorsa,codLin,i+1,True)
            if oraP == oraPi: list_.insert(i,(oraA,oraP,codCorsa,codLin))
        else: 
            list_.insert(lim,(oraA,oraP,codCorsa,codLin))
    
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


    ####################################
    ### CODICE NON CONTROLLATO #########
    ####################################

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

    ####################################
    ### FINE CODICE NON CONTROLLATO ####
    ####################################
 
class OrientedGraph(Graph):
    # desc : crea un grafo orientato
    def __init__(self):
        Graph.__init__(self)

    def addEdge(self,stazA,stazB,oraP,oraA,codCorsa, codLin):
        # desc : crea un arco orientato: STAZA -> STAZB 
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

        
    ####################################
    ### CODICE NON CONTROLLATO GIU' ####
    ####################################

    def plotGraph(self):
        # desc : crea una struttura networkX e la usa per plottare il grafo
        G=self.buildGraph(nx.Graph())
        d={}
        for (node, val) in G.degree():
            d[node]=val

        nx.draw(G, nodelist=d.keys(),node_size=d.values())
        plt.show()
    ####################################
    ### FINE CODICE NON CONTROLLATO ####
    ####################################

    @staticmethod
    def inputGraph(f):
        # desc: crea un grafo orientato 
        #       preso dal file indicato
        # f : nome del file da cui attingere
        
        
        f=open(f,'r')
        s = f.read()
        lines = s.split('\n')
        
        i=0
        while i < len(lines) :
            print
            lines[i]=lines[i].split('\t') #[[stazP, stazA, oraP, oraA, codCorsa, codLin]]
            i += 1

        
        G = OrientedGraph()
        i = 0
        while i < len(lines)-1 : #l'ultima riga del file e' vuota
            stazP = lines[i][0]
            stazA = lines[i][1]
            oraP = lines[i][2]
            oraA =  lines[i][3]
            codCorsa =  lines[i][4]
            codLin =  lines[i][5]
            print "rigo "+str(i)
            G.addEdge(stazP, stazA, oraP, oraA, codCorsa, codLin)
            i += 1
        
        return G