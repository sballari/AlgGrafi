import graph
import random
import DPATrial as DPA
import ER 
import nodeOff
import CC

m=1
nodes = [i for i in range(100)]

#G=DPA.DpaGraph(m,nodes)
G1 = ER.ERGraph(nodes,5)
print CC.ConnectedComponets(G1)


G1.plotGraph()
