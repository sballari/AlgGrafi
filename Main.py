import graph
import random
import DPATrial as DPA
import ER 
import nodeOff
import CC
import networkx as nx


m=1
nodes = [i for i in range(10)]

#G=DPA.DpaGraph(m,nodes)
G1 = ER.ERGraph(nodes,4)
print CC.ConnectedComponets(G1)


G1.plotGraph()
