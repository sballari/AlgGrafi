from ParserCancerData import ParserCancerData
from FastClosestPair import FastClosestPair
from HierarchicalClustering import Hierarchicalclustering
import random
from Coord import Point
from Circle import *
import time
#Data = ParserCancerData("unifiedCancerData_212.csv")
"""
for i in tqdm(range(100)):
    Data = [Point(i,random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)) for i in range(100)]
    P = sorted(Data,key=lambda x : x.getX())

    centers,clusters= Hierarchicalclustering(P,20)
"""
Data = ParserCancerData("unifiedCancerData_1041.csv")
#Data = [Point(i,random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)) for i in range(30)]

P = sorted(Data,key=lambda x : x.getX())

tm=time.time()
centers,clusters= Hierarchicalclustering(P,9)
print time.time()-tm

draw = drawOnImage()
for i in range (len(centers)):
    draw.drawCircle(centers[i])
    for point in clusters[i]:
        draw.drawLine(centers[i],point)
draw.save()