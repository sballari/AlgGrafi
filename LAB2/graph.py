import numpy as np
from matplotlib import pyplot as plt
import random
import parserCoord
import matplotlib.lines as lines
from math import radians, sin, cos, acos

class Hour:
    def __init__(self,hm="00000",d=0):
        #desc: classe orario ci supporta nella gestione degli orari
        #hm: orario nel seguente formato '0HHMM'
        #day: usato per tenere traccia delle coppie di orario a cavallo della mezzanotte
        l=list(hm)
        self.shm=hm
        self.hour=int(l[1]+l[2])%24
        self.minute=int(l[3]+l[4])
        self.day=int(d)*1440
        self.fminute=int(self.hour*60+self.minute)

    def __str__(self):
        #desc: fornisce una stampa "pulita" di un oggetto orario
        hour= str(self.hour) if len(str(self.hour)) == 2 else "0"+str(self.hour)
        minute= str(self.minute) if len(str(self.minute)) == 2 else "0"+str(self.minute)
        return hour+":"+minute
    def addMinute(self,addminute):
        addhour=addminute/60
        addminute=addminute%60

        self.minute+=addminute
        self.hour+=addhour

        if self.minute >= 60:
            self.minute = self.minute%60
            self.hour+=1
        if self.hour >= 24:
            self.hour = self.hour%24

        self.fminute=int(self.hour*60+self.minute)


class Node:
    def __init__(self,n):
        # desc : costruttore oggetto nodo
        # n : label del nodo
        # tempo : O(1)

        # label : etichetta del nodo
        self.label=n
        # adj: insieme di etichette dei nodi adiacenti
        self.adj = dict()
        self.geocoord=[0,0]
    
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
    
    def nextTransport(self,station,hm,d,corsa,linea):
        #desc: fornisce la migliore soluzione di viaggio di viaggio tra questa stazione/nodo e 
        # la stazione station se presente nella sua lista delle adiacenze dall'orario hm
        #station: stazione verso cui si cerca il miglior trasporto
        #hm: orario di partenza
        #d:giorno di partenza 

        #controllo se la il nodo/stazione station e' nella lista delle adiacenze di questo nodo
        if station in self.adj:
            #inizializzo valori valori di ricerca
            best = []
            day = d
            findsolution=False

            #ciclo finche' non trovo una soluzione
            while findsolution == False:
                i=0
                #salto tutte le soluzioni di viaggio con partenza minore di hm
                while i < len(self.adj[station]) and self.adj[station][i][0].fminute+day*1440 < hm.fminute+d*1440:
                    i+=1
                #se ho altri viaggi nella stessa giornata il viaggio i e' il primo viaggio valido ma non e' detto sia ottimo
                if i < len(self.adj[station]):
                    #prendo questa soluzione e la tengo come ottimo provvisorio
                    best = self.adj[station][i]

                    #setup valori per una ricerca tra le soluzioni successive valide e migliori di quella ottenuta finora
                    findsolution = True
                    isbest = False
                    partial_day=0

                    #ciclo finche' non trovo una soluzione di viaggio che parta ad un orario maggiore da questo nodo verso il nodo stazione 
                    #rispetto l'orario di arrivo del nodo migliore trovato.
                    while isbest == False:
                        #se non ho altre soluzioni di viaggio ricomincio a cercare dal giorno dopo
                        if i == len(self.adj[station]):
                            i=0
                            partial_day += 1
                        #controllo che l'orario di partenza non sia successivo all'orario di arrivo al nodo stazione
                        #print self.adj[station][i][2] , corsa , self.adj[station][i][3] , linea
                        if self.adj[station][i][2] == corsa and self.adj[station][i][3] == linea:
                            if self.adj[station][i][0].fminute+partial_day*1440 == best[0].fminute+best[0].day:
                                if self.adj[station][i][1].fminute+partial_day*1440 == best[1].fminute+best[1].day:
                                    best = self.adj[station][i]
                                    day +=partial_day
                        
                        if self.adj[station][i][0].fminute+partial_day*1440 < best[1].fminute+best[1].day:

                            #controllo che l'orario di arrivo di questo trasporto non sia migliore di quello ottimo localmente trovato
                            if self.adj[station][i][1].fminute+partial_day*1440 < best[1].fminute+best[1].day:
                                
                                #in caso positivo ho trovato un nuovo trasporto ottimo!
                                best = self.adj[station][i]
                                day +=partial_day
                            i+=1
                        else:
                            isbest= True
                #non ho altri viaggi per questa giornata vado al giorno dopo
                else:
                    day+=1
            #se l'orario e' a cavallo aggiungo un giorno
            if best[0].fminute > best[1].fminute:
                day+=1
            
            #info sul viaggio migliore trovato, data arrivo, giorno, arrivo, corsa, linea
            best=[best[1],day,best[0],best[2],best[3]]
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

    def plotGraph(self,s=0):
        # desc : crea una struttura networkX e la usa per plottare il grafo
        fig, ax = plt.subplots()

        data = np.array([self.nodes[i].geocoord for i in self.nodes])
        for i in s:
            line = [(self.nodes[i[0]].geocoord[0],self.nodes[i[0]].geocoord[1]),(self.nodes[i[1]].geocoord[0],self.nodes[i[1]].geocoord[1])]
            (line1_xs, line1_ys) = zip(*line)
            ax.add_line(lines.Line2D(line1_xs, line1_ys, linewidth=1, color='blue'))
        x, y = data.T
        plt.scatter(x,y,s=1,c='grey')
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()
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

        #per ogni arco creo il collegamento tra due nodi
        for edge in lines:
            stazP = edge[0]
            stazA = edge[1]
            oraP = list(edge[2])
            oraA =  list(edge[3])
            codCorsa =  edge[4]
            codLin =  edge[5]

            #normalizzo gli orari
            oraP=oraP[0]+str(0)+str(int(oraP[1]+oraP[2])%24)+oraP[3]+oraP[4] if int(oraP[1]+oraP[2]) > 23 else oraP[0]+oraP[1]+oraP[2]+oraP[3]+oraP[4]
            oraA=oraA[0]+str(0)+str(int(oraA[1]+oraA[2])%24)+oraA[3]+oraA[4] if int(oraA[1]+oraA[2]) > 23 else oraA[0]+oraA[1]+oraA[2]+oraA[3]+oraA[4]
            G.addEdge(stazP, stazA, oraP, oraA, codCorsa, codLin)
            i+=1
        
        for A in G.nodes:
            for B in G.nodes[A].adj:
                for corsa in G.nodes[A].adj[B]:
                    #se l'orario e' a cavallo inserisco nella classe hour del nodo di arrivo un giorno in piu'
                    if(int(corsa[0])> int(corsa[1])):

                        corsa[1]=Hour(corsa[1],1)
                    else:
                        corsa[1]=Hour(corsa[1],0)
                    corsa[0]=Hour(corsa[0])
        coord=parserCoord.readCord()
        for station in coord:
            if station in G.nodes:
                G.nodes[station].geocoord=coord[station]

        return G
    def getSolution(self,From,To,parent,data):
        i=To

        points=[]

        stazioni = []

        while parent[i]!=None:
            points.append([i,parent[i]])
            stazioni.append((i,data[i]))
            i=parent[i]

        print "Viaggio da",From,"a",To
        print "Orario di partenza:",data[From][2]
        print "Orario di arrivo:",data[To][0]
        i=len(stazioni)-1

        cod=''
        staz=From
        while i >= 0:
            if cod != data[stazioni[i][0]][3]:
                if i+1 != len(stazioni):
                    print staz
                print stazioni[i][1][2],"corsa",data[stazioni[i][0]][3],data[stazioni[i][0]][4],"da",staz,"a",
                cod = data[stazioni[i][0]][3]
                staz=stazioni[i][0]
            i-=1
        print To
        return points

    def distance(self,u,v):
        coordA = self.nodes[u].geocoord
        coordB = self.nodes[v].geocoord
        slat = radians(float(coordA[1]))
        slon = radians(float(coordA[0]))
        elat = radians(float(coordB[1]))
        elon = radians(float(coordB[0]))
        dist = dist = float(6371.01) * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
        return int(dist)

    @staticmethod
    def addMinutes(hour,day,addMinutes):
        if hour.fminute+day*1440 +addMinutes>= day+1*1440:
            day+=1
        newhour=Hour(hour.shm)
        newhour.addMinute(addMinutes)
        return newhour,day