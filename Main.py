import graph
import random
import DPATrial as DPA
import ER 
import nodeOff
import CC
import networkx as nx
import input_graph as IOG
import time
import pandas as pd

G =IOG.IOGraph ('as20000102.txt', False)
dim_CC_maxs=[] #dimensione della componente connessa massima al variare del tempo
tm=time.time()
#simulazione attacco casuale
while len(G.nodesLabel) != 0:
    nodeOff.MaxDegreeOffNode(G)
    arrayCC=CC.ConnectedComponets(G)
    dim_CC_maxs.append(CC.dim_CC_max(arrayCC))
print time.time()-tm

df=pd.DataFrame(data={'dim_CC_maxs': dim_CC_maxs,'index': [i for i in range(len(dim_CC_maxs))]})

df.plot.scatter(x='index',y='dim_CC_maxs')