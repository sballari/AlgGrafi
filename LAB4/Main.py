from ParserCancerData import ParserCancerData
from HierarchicalClustering import Hierarchicalclustering
from Coord import Point
from Circle import drawOnImage
import time
from kmeans import kmeans
from utility import getncolors,errore_distorsione

dataset = "1041"
k=15
q=5

Data = ParserCancerData("unifiedCancerData_"+dataset+".csv")

colors=getncolors(k)

print "KmeansClustering"
contee = sorted(Data,key=lambda x : x.getPop())
tm=time.time()

centers,clusters= kmeans(contee[-k:],contee,k,q)
print "Time Elapsed: ",time.time()-tm

errore,distorsione=errore_distorsione(centers,clusters)
print "distorsione:",distorsione

draw = drawOnImage()
for i in range (len(centers)):
    draw.drawCircle(centers[i])
    for point in clusters[i]:
        draw.drawLine(centers[i],point,colors[i])
draw.save("kmeans")
print ""
print "HierarchicalClustering"
P = sorted(Data,key=lambda x : x.getX())

tm=time.time()
centers,clusters= Hierarchicalclustering(P,k)
print "Time Elapsed: ",time.time()-tm

errore,distorsione=errore_distorsione(centers,clusters)
print "distorsione:",distorsione

draw = drawOnImage()
for i in range (len(centers)):
    draw.drawCircle(centers[i])
    for point in clusters[i]:
        draw.drawLine(centers[i],point,colors[i])
draw.save("gerarchico")


