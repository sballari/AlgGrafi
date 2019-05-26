from ParserCancerData import ParserCancerData
from FastClosestPair import FastClosestPair
from HierarchicalClustering import Hierarchicalclustering
import random

Data = ParserCancerData("unifiedCancerData_212.csv")

P = sorted(Data,key=lambda x : x.getX())

centers,clusters= Hierarchicalclustering(P,100)
