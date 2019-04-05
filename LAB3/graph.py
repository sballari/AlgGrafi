from parser import parser_LTS


class MatrixCompleteGraph():

    def __init__(self,n):
        self.weight_matrix = [[0 for i in n]for j in n]
        # matrice bidimensinale preinit a 0

    def addweight(self, x, y, weight):
        self.weight_matrix[x][y] = weight

    @staticmethod
    def createGraphFromTSP(fileName):
        w_type, coord = parser_LTS(fileName)
        G=MatrixCompleteGraph(len(coord))

        if w_type == "GEO":
            #map(lambda a,b: distanceGEO(a,b,) ,coord)
            pairs = [(x,y) for y in coord for x in coord]
            reduce(lambda sr ,t: distanzaGeo(t[0],t[1]))
  
                    
                    
        if w_type == "EUC_2D":
            for node1 in coord):
                for node2 in coorcoordd:
                    G.weight_matrix[node1[0]][node2[0]]=distanceGEO(node1,node2)
    @staticmethod
    def radiantConv(tupla):
        # tupla : (index,string-lat,string-long)
        # return : lat in rad, long in rad approssimati per difetto
        pi = 3.141592;

        lat = tupla[0]
        lon = tupla[1]

        lat_deg = (int) lat;
        lat_rad = pi * (lat_deg + 5.0 * lat_min/ 3.0) / 180.0;

        lon_deg = (int) lon;
        lon_rad = pi * (lon_deg + 5.0 * lon_min/ 3.0) / 180.0;

        return lat_rad,lon_rad

    @staticmethod
    def distanceGEO(node1,node2):
        #node1(nodeI,x,y)
        
        longitude_i,latitude_i = radiantConv(node1)
        longitude_j,latitude_j = radiantConv(node2)
        
        RRR = 6378.388;

        q1 = cos( longitude_i - longitude_j ); 
        q2 = cos( latitude_i - latitude_j ); 
        q3 = cos( latitude_i + latitude_j ); 
        dij = (int) ( RRR * acos( 0.5*((1.0+q1)*q2 - (1.0-q1)*q3) ) + 1.0);
        
        return dij


