import graph
import UPA
import ER 
import nodeOff
import CC
import networkx as nx
import time
import pandas as pd
import matplotlib.pyplot as plt
import sys
import seaborn as sns
from tqdm import tqdm

sys.setrecursionlimit(10000)

G1 =graph.NotOrientedGraph.inputGraph('as20000102.txt')
print G1.getEdgeNumber()

# se vuole abbiamo scritto su file dei grafi di esempio generati 
# con i due algoritmi senza bisogno che se li ricalcoli.
#G2 =graph.NotOrientedGraph.inputGraph('test/ER0.txt')
#G3 =graph.NotOrientedGraph.inputGraph('test/UPA0.txt')

#genero le label che voglio siano usate per creare i due grafici 
labels=[i for i in range(len(G1.nodes))]

#definisco la probabilita' p
p=(float(G1.getEdgeNumber())*2)/(len(labels)*(len(labels)-1))
print p
G2 =ER.ERNotOrientedGraph(labels,p)

#definisco la m
m=int(round(G1.avg_degree()/2))

G3 =UPA.UpaGraph(labels,m)

G={
    'real': G1,
    'ER p: 0.0006': G2,
    'UPA m: 2': G3
}

dim_CC_maxs=[] #dimensione della componente connessa massima al variare del tempo
keys=[]
index=[]

NumNodes=len(G1.nodes)

for g in G:
    arrayCC=CC.ConnectedComponets(G[g])
    dim_CC_maxs.append(CC.dim_CC_max(arrayCC))
    index.append(0)
    keys.append(g)

#simulazione attacco casuale
for g in G:
    for i in tqdm(range(1,NumNodes+1),desc=g):
        
        #strategia random
        nodeOff.randomStrategy(G[g])
        
        #strategia max degree
        #nodeOff.maxDegreeStrategy(G[g])

        arrayCC=CC.ConnectedComponets(G[g])
        dim_CC_maxs.append(CC.dim_CC_max(arrayCC))
        index.append(i)
        keys.append(g)

df=pd.DataFrame(data={'dim_CC_maxs': dim_CC_maxs,'index': index, 'key': keys})
df.to_csv('random.csv', encoding='utf-8',index=False)

sns.pairplot(x_vars=["index"], y_vars=["dim_CC_maxs"], data=df, hue="key",plot_kws=dict(s=50), markers="+",height=10)
plt.show()
