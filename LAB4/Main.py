from ParserCancerData import ParserCancerData
from FastClosestPair import FastClosestPair
from HierarchicalClustering import HierarchicalClustering
import random

Data = ParserCancerData("unifiedCancerData_212.csv")

P = sorted(Data,key=lambda x : x.getX())
S = sorted(Data,key=lambda y : y.getY())

print HierarchicalClustering(P,5)