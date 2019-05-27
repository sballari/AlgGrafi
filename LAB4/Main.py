from ParserCancerData import ParserCancerData
from FastClosestPair import FastClosestPair
from HierarchicalClustering import Hierarchicalclustering
import random
from Coord import Point
from tqdm import tqdm

#Data = ParserCancerData("unifiedCancerData_212.csv")
"""
for i in tqdm(range(100)):
    Data = [Point(i,random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100)) for i in range(100)]
    P = sorted(Data,key=lambda x : x.getX())

    centers,clusters= Hierarchicalclustering(P,20)
"""
Data = ParserCancerData("unifiedCancerData_212.csv")
P = sorted(Data,key=lambda x : x.getX())
centers,clusters= Hierarchicalclustering(P,20)
