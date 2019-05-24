from parseeer import parser_LTS
from math import cos, acos, sqrt


class MatrixCompleteGraph():

    def __init__(self,n):
        # desc : crea un grafo completo non orientato
        # n : numero di nodi del grafo
        # tempo : O(n^2)

        self.weight_matrix = [ [0 for i in range(n)] for j in range(n)]
        # matrice bidimensinale (lista di liste) preinit a 0

    def addweight(self, x, y, weight):
        # desc : inserisce il peso weight tra i nodi con label x e y
        # x : label del primo nodo della coppia
        # y : label del secondo nodo della coppia
        # weight : peso da assegnare all'arco
        # tempo : O(1)

        if (x==y): self.weight_matrix[y][x]=0
        else :
            self.weight_matrix[x][y] = weight
            self.weight_matrix[y][x] = weight
        
    
    def getweight(self,start_index,dest_index): 
        # desc : restituisce il peso dell'arco tra start_index e dest_index
        # start_index : label del nodo da cui parte l'arco
        # dest_index : label del nodo a cui arriva l'arco
        # tempo : O(1)
        return self.weight_matrix[start_index][dest_index]

    def getNumNodes(self):
        return len(self.weight_matrix)

    @staticmethod
    def createGraphFromTSP(fileName):
        # desc : carica i dati dal file fileName e crea un grafo che poi restituisce
        # fileName : nome del file da cui caricare i dati

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
        # desc : data una stupla di dati restituisce latitudine in radianti, longitudine in radianti approssimati per difetto
        # tupla : (index,string-lat,string-long)

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
        # desc : calcola la distanza geografica fra 2 nodi
        # node1 : oggetto nodo con il seguente formalismo node(nodeId,x,y)
        # node2 : oggetto nodo con il seguente formalismo node(nodeId,x,y)

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
        # desc : calcola la distanza euclidea fra 2 nodi
        # node1 : oggetto nodo con il seguente formalismo node(nodeId,x,y)
        # node2 : oggetto nodo con il seguente formalismo node(nodeId,x,y)

        x1 = float(node1[1])
        x2 = float(node2[1])
        y1 = float(node1[2])
        y2 = float(node2[2])
        distance = round(sqrt((x1-x2)**2 + (y1-y2)**2),0)
        return distance

    def weightCirc(self,circ):
        # desc : restituisce il costo totale se si attraversa il grafo secondo la sequenza data in circ
        # circ : circuito hamiltoniano 
        # tempo : O(len(circ)) 
        somma = 0
        for j in range(1, len(circ)):
            i = j-1
            dij = self.getweight(circ[i],circ[j])
            somma += dij
        return somma
