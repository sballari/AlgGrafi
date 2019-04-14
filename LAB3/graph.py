from parseeer import parser_LTS
from math import cos, acos, sqrt


class MatrixCompleteGraph():

    def __init__(self,n):
        self.weight_matrix = [ [0 for i in range(n)] for j in range(n)]
        # matrice bidimensinale (lista di liste) preinit a 0

    def addweight(self, x, y, weight):
        #grafo non orientato
        if (x==y): self.weight_matrix[y][x]=0
        else :
            self.weight_matrix[x][y] = weight
            self.weight_matrix[y][x] = weight
        
    
    def getweight(self,start_index,dest_index): 
        return self.weight_matrix[start_index][dest_index]

    @staticmethod
    def createGraphFromTSP(fileName):
        w_type, coord = parser_LTS(fileName)
        G=MatrixCompleteGraph(len(coord))

        distFun = None
        if w_type == "GEO" : distFun = MatrixCompleteGraph.distanceGEO
        if w_type == "EUC_2D" : distFun = MatrixCompleteGraph.distanceEUC

        pairs = [(x,y) for x in range(len(coord)) for y in range(x+1,len(coord))]
        for (x,y) in pairs:
            dst = distFun(coord[x],coord[y])
            G.addweight(x,y,dst)
            
        return G

                
    @staticmethod
    def radiantConv(tupla):
        # tupla : (index,string-lat,string-long)
        # return : latitudine in radianti, longitudine in radianti approssimati per difetto
        pi = 3.141592

        lat_deg = float(tupla[1])
        lon_deg = float(tupla[2])

        lat_min = lat_deg - int(lat_deg)
        lat_rad = pi * (int(lat_deg) + 5.0 * lat_min/ 3.0) / 180.0

        lon_min = lon_deg - int(lon_deg)
        lon_rad = pi * (int(lon_deg) + 5.0 * lon_min/ 3.0) / 180.0

        return lat_rad,lon_rad

    @staticmethod
    def distanceGEO(node1,node2):
        #node(nodeId,x,y)
        #calcola la distanza geografica fra 2 nodi
        
        latitude_i, longitude_i = MatrixCompleteGraph.radiantConv(node1)
        latitude_j, longitude_j = MatrixCompleteGraph.radiantConv(node2)
        
        RRR = 6378.388

        q1 = cos( longitude_i - longitude_j ) 
        q2 = cos( latitude_i - latitude_j )
        q3 = cos( latitude_i + latitude_j ) 
        dij = (int) ( RRR * acos( 0.5*((1.0+q1)*q2 - (1.0-q1)*q3) ) + 1.0)
        
        return dij
    
    @staticmethod
    def distanceEUC(node1, node2): 
        x1 = float(node1[1])
        x2 = float(node2[1])
        y1 = float(node1[2])
        y2 = float(node2[2])
        distance = sqrt((x1-x2)**2 + (y1-y2)**2)
        return distance