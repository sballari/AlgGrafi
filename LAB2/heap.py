import parserCoord

class heap:
    def __init__(self):
        #desc: costruisco le strutture dati richieste dallo heap
        #deque: coda di priorita, contiene il codice di ciascuna 
        #       stazione ordinato nello heap secondo l'ordine di arrivo
        #position: dizionario che ha per chiave il codice della stazione 
        #          e valore la posizione della stazione nella coda deque
        #data: dizionario che tiene conto dei dati di arrivo migliore nella stazione
        #parent: dizionario che ha per chiave il codice della stazione e per valore
        #        la stazione da cui raggiungere la stazione chiave
        self.deque= []
        self.position=dict()
        self.data=dict()
        self.parent=dict()

    def setup(self,vlist,vstart,vhour,vday=0):
        #desc: inserisce valori vuoti per ciascuna stazione,
        #      inserisce i dati della stazione root e la 
        #      aggiunge alla coda deque
        #vlist: lista delle stazioni
        #vstart: stazione root
        #vhour: orario di partenza
        #vday: giorno di partenza di default a 0
        for i in vlist:
            self.data[i]=[] #orario infinito
            self.parent[i]=None
        self.data[vstart]=[vhour,vday] 
        self.add(vstart)
    
    def setupE(self,vlist,vstart,vhour,koordMap,dest,speed,vday=0):
        for i in vlist:
            self.data[i]=[]
            self.parent[i]=None

        ########################
        #### calcolo h #########
        ########################
        min_fastest_journey = int( ( parserCoord.distance(vstart, dest, koordMap) / speed ) * 60 ) # minuti del viaggio min        
        t_fast = parserCoord.hourPlusMinuts(vhour,min_fastest_journey)
        #######################
        self.data[vstart]=[t_fast[0],vday+t_fast[1]] 
        self.add(vstart)


    def add(self,station):
        #desc: inserisce una stazione nella coda e aggiorna la sua posizione
        #station: codice stazione da inserire
        self.position[station]=len(self.deque)
        self.deque.append(station)
        self.bubbleUp(station)
        
    def bubbleUp(self,station):
        #desc: aggiorna lo heap dopo l'inserimento o la modifica del nodo station
        #station: codice stazione inserito o modificato
        if station in self.position:
            i = self.position[station]
            p = (i-1)/2

            while i > 0 and self.TimeByIndex(i) <  self.TimeByIndex(p):
                #scambio gli indici nel dizionario
                self.position[self.deque[p]]=i
                self.position[self.deque[i]]=p
                #scambio gli indici nell'array
                mv = self.deque[i]
                self.deque[i]=self.deque[p]
                self.deque[p]=mv

                i=p
                p=(i-1)/2

    def decreaseKey(self,u,v,info):
        #desc: modifica in meglio un nodo e se non presente nella coda lo riaggiunge
        #u: nodo precedente/padre
        #v: nodo corrente
        #info: info sull'ora di arrivo alla stazione v 
        if self.RELAX(u,v,info):
            if v in self.position:
                self.bubbleUp(v)
            else:
                self.add(v)

    def extractMin(self):
        #desc: estrae il nodo con orario arrivo minimo e aggiorna la coda deque
        next_station = self.deque[0]
        del self.position[next_station]
        last = self.deque.pop()

        if len(self.deque) > 0:
            self.deque[0] = last
            self.position[self.deque[0]]=0
            self.trickledown(self.deque[0])
        return next_station

    def trickledown(self,station):
        #desc: aggiorna la posizione del nodo station se i 
        #      suoi figli hanno un orario di arrivo minore 
        #station: codice stazione da spostare eventualmente
        i = self.position[station]
        l = i * 2 + 1
        r = i * 2 + 2 
        smallest = i
        if l < len(self.deque) and self.TimeByIndex(l) <  self.TimeByIndex(i):
            smallest = l

        if r < len(self.deque) and self.TimeByIndex(r) <  self.TimeByIndex(i):
            smallest = r
        
        if smallest != i:
            self.position[self.deque[smallest]]=i
            self.position[self.deque[i]]=smallest

            mv = self.deque[i]
            self.deque[i]=self.deque[smallest]
            self.deque[smallest]=mv
            self.trickledown(self.deque[smallest])
    

    def RELAX(self,u,v,info):
        #desc: rilassa l'arco u-v
        #u: nodo predecessore/padre
        #v: nodo corrente
        #info: info sull'ora di arrivo alla stazione v 
        if self.data[v][0].fminute + self.data[v][1]*1440 > info[0].fminute + info[1]*1440:
            self.data[v]=info
            self.parent[v]=u
            return True
        return False

    def TimeByIndex(self,index):
        #desc: restituisce il tempo in minuti della stazione in posizione index
        #index: indice della coda deque corripondente ad una stazione di cui si vuole sapere
        #       l'orario di arrivo in minuti.
        return self.data[self.deque[index]][0].fminute+self.data[self.deque[index]][1]*1440