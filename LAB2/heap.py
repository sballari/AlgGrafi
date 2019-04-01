class heap:
    def __init__(self):
        self.deque= []
        self.dc=dict()
        self.d=dict()
        self.p=dict()
    #def setup(self,G,A,hm):
    #    for B in G.nodes[A].adj:
    #        data = G.nodes[A].nextTransport(B,hm)
    #        if len(data) > 0:
    #            self.add(B,data)
    def add(self,station,data):
        self.dc[station]=len(self.deque)
        self.deque.append([station,data])
        self.bubbleUp(station)
    def bubbleUp(self,station):
        if station in self.dc:
            i = self.dc[station]
            p = (i-1)/2

            while i > 0 and self.deque[i][1][0].fminute+self.deque[i][1][1]*1440 <  self.deque[p][1][0].fminute+self.deque[p][1][1]*1440:
                #scambio gli indici nel dizionario
                self.dc[self.deque[p][0]]=i
                self.dc[self.deque[i][0]]=p
                #scambio gli indici nell'array
                mv = self.deque[i]
                self.deque[i]=self.deque[p]
                self.deque[p]=mv

                i=p
                p=(i-1)/2

    def decreaseKey(self,station,data):
        if station in self.dc:
            i = self.dc[station]
            self.deque[i][1]=data
            self.bubbleUp(station)
        else:
            self.add(station,data)
    def extractMin(self):
        next_station = self.deque[0]
        del self.dc[next_station[0]]
        
        last = self.deque.pop()
        if len(self.deque) > 0:
            self.deque[0] = last
            self.dc[self.deque[0][0]]=0
            self.trickledown(self.deque[0][0])
        return next_station

    def trickledown(self,station):
        i = self.dc[station]
        l = i * 2 + 1
        r = i * 2 + 2 
        smallest = i
        if l < len(self.deque) and self.deque[l][1][0].fminute+self.deque[l][1][1]*1440 < self.deque[i][1][0].fminute+self.deque[i][1][1]*1440:
            smallest = l

        if r < len(self.deque) and self.deque[r][1][0].fminute+self.deque[r][1][1]*1440 < self.deque[i][1][0].fminute+self.deque[i][1][1]*1440:
            smallest = r
        
        if smallest != i:
            self.dc[self.deque[smallest][0]]=i
            self.dc[self.deque[i][0]]=smallest
            #scambio gli indici nell'array
            mv = self.deque[i]
            self.deque[i]=self.deque[smallest]
            self.deque[smallest]=mv
            #print self.deque[smallest]
            self.trickledown(self.deque[smallest][0])
    

    def RELAX(self,u,v,data):
        self.d[v]=data
        self.p[v]=u
