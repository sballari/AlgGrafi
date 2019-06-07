class Point:
    def __init__(self,contea,x,y,pop,risk):
        self.tupla = (contea,x,y,pop,risk)

    def getX(self):
        return self.tupla[1]

    def getY(self):
        return self.tupla[2]

    def getPop(self):
        return self.tupla[3]

    def __str__(self):
        return str(self.tupla)

class Center:
    def __init__(self,x,y,IDcenter=0):
        self.tupla = (x,y)
        self.idcenter=IDcenter

    def getX(self):
        return self.tupla[0]

    def getY(self):
        return self.tupla[1]
        
    def __str__(self):
        return str(self.tupla)
