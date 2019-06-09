from decimal import Decimal
import random
from Coord import Center

def euclide(p1,p2):
    #desc: calcola la distanza euclidea tra i punti p1 e p2
    #tempo: O(1)

    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    return (float((x1-x2)**2+(y1-y2)**2))**0.5
    

def getncolors(n):

	colors1 = [[255-i,i,0] for i in range(0,255,5)]
	colors2 = [[0,255-i,i] for i in range(0,255,5)]
	colors3 = [[i,0,255-i] for i in range(0,255,5)]
	colors = colors1+colors2+colors3

	chosen_colors=[]
	for c in range(0,len(colors),(len(colors)/n)):
		chosen_colors.append(colors[c])
	colors=chosen_colors
	colors = [(color[0],color[1],color[2]) for color in colors]			
	colors = ["rgb"+str(color) for color in colors]
	random.shuffle(colors)
	return colors

def errore_distorsione(centers,clusters):
    #desc: calcola di distorsione totale

	errori = []
	distorsione = 0
	for center in range(len(centers)):

		errore = sum([point.getPop()*(euclide(centers[center],point))**2 for point in clusters[center]])
		distorsione+= errore
		errori.append('%.2E' % Decimal(errore))
	return errori, '%.2E' % Decimal(distorsione)
	
# cluster : set di punti
def newCenter(cluster,idcenter=0):
    #desc: crea un nuovo centroide

    x = 0
    y = 0
    for point in cluster:
        x = x + point.getX() 
        y = y + point.getY()
    x = x / len(cluster)
    y = y / len(cluster)
    return Center(x,y,idcenter) 
