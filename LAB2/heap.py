class heap:
    def __init__(self):
        self.deque= []
        self.position=dict()
        self.data=dict()
        self.parent=dict()

    def setup(self,vlist,vstart,vhour,vday):
        for i in vlist:
            self.data[i]=[]
            self.parent[i]=None
        self.data[vstart]=[vhour,vday]
        self.add(vstart,[vhour,vday])

    def add(self,station,info):
        self.position[station]=len(self.deque)
        self.deque.append(station)
        self.bubbleUp(station)
        
    def bubbleUp(self,station):
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
        if self.RELAX(u,v,info):
            if v in self.position:
                self.bubbleUp(v)
            else:
                self.add(v,info)

    def extractMin(self):
        next_station = self.deque[0]
        del self.position[next_station]
        last = self.deque.pop()

        if len(self.deque) > 0:
            self.deque[0] = last
            self.position[self.deque[0]]=0
            self.trickledown(self.deque[0])
        return next_station

    def trickledown(self,station):
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
        if self.data[v][0].fminute + self.data[v][1]*1440 > info[0].fminute + info[1]*1440:
            self.data[v]=info
            self.parent[v]=u
            return True
        return False

    def TimeByIndex(self,index):
        return self.data[self.deque[index]][0].fminute+self.data[self.deque[index]][1]*1440