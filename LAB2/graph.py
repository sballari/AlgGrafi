import matplotlib.pyplot as plt
import networkx as nx
import random

class Hour:
    def __init__(self,hm):
        l=list(hm)
        self.shm=hm
        self.hour=int(l[1]+l[2])%24
        self.minute=int(l[3]+l[4])
        self.fminute=self.hour*60+self.minute

    def __str__(self):
        hour= str(self.hour) if len(str(self.hour)) == 2 else "0"+str(self.hour)
        minute= str(self.minute) if len(str(self.minute)) == 2 else "0"+str(self.minute)
        return hour+":"+minute

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
        
        if dest in self.adj:
            edgeList = self.adj[dest]
            self.orderedInsert(edgeList,oraP,oraA,codCorsa,codLin,0,len(edgeList)-1)
        else :
            self.adj[dest] = [[oraP,oraA,codCorsa,codLin]]

    @staticmethod
    def orderedInsert(list_,oraP,oraA,codCorsa,codLin,lbi,ubi):
        # desc : inserisce un arco dal nodo attuale , ordine ora arrivo
        # list: lista delle adiacenze
        # dest: label staz di destinazione
        # oraP : orario di partenza 
        # oraA : orario arrivo
        # lbi : lower bound compreso sx del chunk
        # ubi : upper bound compreso dx del chunk
        # tempo: O(log(n))

        dim=ubi-lbi+1 #dimensione del chunk
        i = lbi + (dim//2) #indice pivot
        
        if (dim>0) :
            oraPi = (list_[i])[0] #oraP dell'elemento pivot
            if oraP < oraPi: 
                Node.orderedInsert(list_,oraP,oraA,codCorsa,codLin,lbi,i-1)
            if oraP > oraPi: 
                Node.orderedInsert(list_,oraP,oraA,codCorsa,codLin,i+1,ubi)
            if oraP == oraPi: list_.insert(i,[oraP,oraA,codCorsa,codLin])
        else: 
            list_.insert(i,[oraP,oraA,codCorsa,codLin])
    
    def nextTransport(self,station,hm,d):
        if station in self.adj:
            best = []
            day = 0
            while len(best) == 0:
                i=0
                while i < len(self.adj[station]) and self.adj[station][i][0].fminute+day*1440 < hm.fminute+d*1440:
                    i+=1

                if i < len(self.adj[station]):
                    best = self.adj[station][i]
                    while i<len(self.adj[station]) and self.adj[station][i][0].fminute < best[1].fminute:
                        if self.adj[station][i][1].fminute < best[1].fminute:
                            best = self.adj[station][i]
                        i+=1
                else: 
                    day+=1
            best=[best[0],day,best[2],best[3]]
            #print str(hm),str(d),"-",[str(i) for i in best]
            return best
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
    ### CODICE NON CONTROLLATO #########
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
            lines[i]=lines[i].split('\t') #[(stazP, stazA, oraP, oraA, codCorsa, codLin)]
            i += 1
        
        G = OrientedGraph()
        del lines[-1] #elimino l'ultima riga che e' vuota
        i=0

        for edge in lines:
            stazP = edge[0]
            stazA = edge[1]
            oraP = edge[2]
            oraA =  edge[3]
            codCorsa =  edge[4]
            codLin =  edge[5]
            G.addEdge(stazP, stazA, oraP, oraA, codCorsa, codLin)
            i+=1
        
        for A in G.nodes:
            for B in G.nodes[A].adj:
                for corsa in G.nodes[A].adj[B]:
                    corsa[0]=Hour(corsa[0])
                    corsa[1]=Hour(corsa[1])
        return G