from graph import MatrixCompleteGraph
from HK import HKTSP
from randomInsertion import RandomInsertion
import MSTApprox
import primMST
import pandas as pd
from os import listdir
from os.path import isfile, join
from sys import setrecursionlimit
from collections import OrderedDict


setrecursionlimit(10000)
optSol = {
    "burma14.tsp" : 3323,
    "ulysses22.tsp": 7013,
    "eil51.tsp": 426,
    "kroD100.tsp":21294,
    "gr229.tsp": 134602,
    "d493.tsp": 35002,
    "dsj1000.tsp": 	18659688
}

mypath="dataset"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

index = []

sol_HK = []
tempo_HK = []
errore_HK = []

sol_r = []
tempo_r = []
errore_r = [] 

sol_MSTA = []
tempo_MSTA = []
errore_MSTA = []

for ds_name in onlyfiles:
    print "------------------INIZIO "+ds_name+" ------------"
    G = MatrixCompleteGraph.createGraphFromTSP(ds_name)
    index.append(ds_name)
    """
    #HELD-KARP ALGORITHM
    print "esecuzione hk: "+ds_name
    sol,tm= HKTSP(G,60)
    tm=round(tm,3)
    print "costo soluzione: "+str(sol)
    print "tempo esecuzione: "+str(tm)
    errore=str(round(float(sol-optSol[ds_name])/optSol[ds_name]*100,2))+"%"
    print "errore: "+str(errore)
    sol_HK.append(sol)
    tempo_HK.append(tm)
    errore_HK.append(errore)
    """
    #RANDOM INSERTION
    print "esecuzione random insertione: "+ds_name
    sol,tm= RandomInsertion(G)
    sol= G.weightCirc(sol)
    tm=round(tm,3)
    print "costo soluzione: "+str(sol)
    print "tempo esecuzione: "+str(tm)
    errore=str(round(float(sol-optSol[ds_name])/optSol[ds_name]*100,2))+"%"
    print "errore: "+str(errore)
    sol_r.append(sol)
    tempo_r.append(tm)
    errore_r.append(errore)
    """
    #MST APPROX ALGORITHM
    print "esecuzione MSTApprox: "+ds_name
    sol,tm= MSTApprox.MSTApprox(G)
    sol = G.weightCirc(sol)
    tm=round(tm,3)
    print "costo soluzione: "+str(sol)
    print "tempo esecuzione: "+str(tm)
    errore=str(round(float(sol-optSol[ds_name])/optSol[ds_name]*100,2))+"%"
    print "errore: "+str(errore)
    sol_MSTA.append(sol)
    tempo_MSTA.append(tm)
    errore_MSTA.append(errore)
    """
"""
df=pd.DataFrame(data=OrderedDict({"Istanze":index,"Soluzione_HK":sol_HK,"Tempo_HK":tempo_HK,"Errore_HK":errore_HK,"Soluzione_RINS":sol_r,"Tempo_RINS":tempo_r,"Errore_RINS":errore_r,"Soluzione_MSTA":sol_MSTA,"Tempo_MSTA":tempo_MSTA,"Errore_MSTA":errore_MSTA,}))
df.set_index("Istanze",inplace=True)
print df.to_latex(index=True)
"""