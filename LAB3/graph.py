from parseeer import parser_LTS
from math import cos, acos, sqrt


class MatrixCompleteGraph():

    def __init__(self,n):
        self.weight_matrix = [[0] * n] * n
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

        if w_type == "GEO":
            pairs = [(elemX,elemY) for elemX in coord for elemY in coord]
            for e in pairs:
                dst = MatrixCompleteGraph.distanceGEO(e[0],e[1])
                index1 = int(e[0][0])-1
                index2 = int(e[1][0])-1
                G.addweight(index1,index2,dst)
            return G
                   
        if w_type == "EUC_2D":
            pairs = [(elemX,elemY) for elemX in coord for elemY in coord]
            for e in pairs:
                dst = MatrixCompleteGraph.distanceEUC(e[0],e[1])
                index1 = int(e[0][0])-1
                index2 = int(e[1][0])-1
                G.addweight(index1,index2,dst)
            return G
        return w_type
                
    @staticmethod
    def radiantConv(tupla):
        # tupla : (index,string-lat,string-long)
        # return : latitudine in radianti, longitudine in radianti approssimati per difetto
        pi = 3.141592

        lat_deg = float(tupla[1])
        lon_deg = float(tupla[2])

        lat_min = lat_deg - int(lat_deg)
        lat_rad = pi * (lat_deg + 5.0 * lat_min/ 3.0) / 180.0

        lon_min = lon_deg - int(lon_deg)
        lon_rad = pi * (lon_deg + 5.0 * lon_min/ 3.0) / 180.0

        return lat_rad,lon_rad

    @staticmethod
    def distanceGEO(node1,node2):
        #node(nodeId,x,y)
        #calcola la distanza geografica fra 2 nodi
        
        longitude_i,latitude_i = MatrixCompleteGraph.radiantConv(node1)
        longitude_j,latitude_j = MatrixCompleteGraph.radiantConv(node2)
        
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