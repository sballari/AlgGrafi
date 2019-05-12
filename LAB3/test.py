from graph import MatrixCompleteGraph
from HK import HKTSP
from randomInsertion import RandomInsertion
import MSTApprox
import primMST
import pandas as pd
from os import listdir
from os.path import isfile, join
from sys import setrecursionlimit
from pandas.compat import OrderedDict

setrecursionlimit(10000)

f=open("dataset/data_opt.csv","r")
s=f.read()
s=s.split("\n")
optSol=[i.split() for i in s]

data = OrderedDict()

data["index"] = []

data["errore_min"] = []

data["errore_max"] = []

for ds_name, opt_sol in optSol:
    data["index"].append(ds_name)
    G = MatrixCompleteGraph.createGraphFromTSP(ds_name)
    l_error=[]
    for k in range(10000):
        csol,tm= RandomInsertion(G)

        sol= G.weightCirc(csol)
        errore=round(float(sol-int(opt_sol))/int(opt_sol)*100,2)
        l_error.append(errore)
    print ds_name
    data["errore_min"].append(min(l_error))
    data["errore_max"].append(max(l_error))

df=pd.DataFrame(data)
df.set_index("index",inplace=True)
with open('relazione/random.tex', 'w') as tf:
     tf.write(df.to_latex(index=True))
