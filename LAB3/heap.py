import parserCoord

class heap:
    def __init__(self):
        
        self.A = [] #[index]
        self.indexPositionMap = dict()
        self.indexValueMap = dict()
        


    def add(self,index,value):
        #desc: inserisce una stazione nella coda e aggiorna la sua posizione
        #station: codice stazione da inserire
        indexValueMap[index] = value
        n = len(self.A) 
        self.A[n] = index #metto l'indice in ultima posizione
        self.indexPositionMap[index] = n
        self.bubbleUp(n)

    @staticmethod  
    def parentPosition(i):
        return (i-1)//2


    def isEmpty(self):
        return len(self.A) == 0
    
    def value(self,index):
        return self.indexValueMap[index]
    def changeValue(self,index,newValue):
        return self.indexValueMap[index]=newValue


    def isPresent(self,index):
        i=0
        trovato=False

        while i<len(self.A) && !trovato :
            if A[i] == index : 
                trovato = True
            i = i+1

        return trovato


    def bubbleUp(self,i):
        #desc: aggiorna lo heap dopo l'inserimento o la modifica del nodo station
        #station: codice stazione inserito o modificato
        p = self.parentPosition(i)

        while i > 0 and self.value(A[i]) <  self.value(A[p]):
            #scambio A[i] <-> A[p]
            self.indexPositionMap[A[p]] = i
            self.indexPositionMap[A[i]] = p
            
            tmp = A[p]
            self.A[p] = A[i]
            self.A[i] = tmp
            

            i=p
            p=(i-1)/2

    def decreaseKey(self,node_index,newValue):
        if self.value(node_index) < newValue:
            return False
        else: 
            self.changeValue(node_index,newValue)
            i = self.indexPositionMap[node_index]
            self.bubbleUp(self,i)
            return True


    def extractMin(self):
        #desc: estrae il nodo con orario arrivo minimo e aggiorna la coda deque
        n = len(self.A)

        minEl = self.value(self.A[0])
        del self.indexPositionMap[self.A[0]]
        del self.indexValueMap[self.A[0]]
        
        self.A[0] = self.A[n-1]
        self.A.pop() #decremento n

        self.trickledown(0)
        return minEl

    def trickledown(self,i):
        #desc: aggiorna la posizione del nodo station se i 
        #      suoi figli hanno un orario di arrivo minore 
        #station: codice stazione da spostare eventualmente
        
        l = i * 2 + 1
        r = i * 2 + 2 
        smallest = i
        if l < len(self.A) and self.value(self.A[l]) <  self.value(self.A[i]):
            smallest = l

        if r < len(self.A) and self.value(self.A[r]) <  self.value(A[smallest]):
            smallest = r
        
        if smallest != i:
            self.indexPositionMap[self.A[smallest]] = i
            self.indexPositionMap[self.A[i]] = smallest

            tmp = self.A[i]
            self.A[i]=self.A[smallest]
            self.A[smallest] = tmp
            self.trickledown(smallest)
    
