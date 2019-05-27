from ParserCancerData import ParserCancerData
from FastClosestPair import FastClosestPair
from HierarchicalClustering import Hierarchicalclustering
import random
from Coord import Point

#Data = ParserCancerData("unifiedCancerData_212.csv")
Data = [Point(i,random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)) for i in range(20)]
P = sorted(Data,key=lambda x : x.getX())

centers,clusters= Hierarchicalclustering(P,2)
