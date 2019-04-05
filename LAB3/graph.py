class MatrixCompleteGraph():
    
    def __init__(self,n) : 
        self.weight_matrix = [[0 for i in n]for j in n] #matrice bidimensinale  
    def addweight(self,x,y,weight):
        self.weight_matrix[x][y]=weight