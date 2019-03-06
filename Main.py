import graph
import random
import DPATrial as DPA
import ER 

m=1
nodes = [i for i in range(20)]
G=DPA.DpaGraph(m,nodes)
G1 = ER.ERGraph(nodes,5)
G.plotGraph()

