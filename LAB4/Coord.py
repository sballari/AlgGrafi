class Point:
    def __init__(self,contea,x,y,pop,risk):
        self.tupla = (contea,x,y,pop,risk)

    def getX(self):
        return self.tupla[1]

    def getY(self):
        return self.tupla[2]

class Center:
    def __init__(self,x,y):
        self.tupla = (x,y)

    def getX(self):
        return self.tupla[0]

    def getY(self):
        return self.tupla[1]
