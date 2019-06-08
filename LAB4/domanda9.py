from ParserCancerData import ParserCancerData
from FastClosestPair import FastClosestPair, euclide
from HierarchicalClustering import Hierarchicalclustering
import random
from Coord import Point
from Circle import *
import time
from kmeans import kmeans
from decimal import Decimal
import pandas as pd
import matplotlib.pyplot as plt
from decimal import Decimal

def distorsione(centers,clusters):
	errori = []
	distorsione = 0
	for center in range(len(centers)):

		errore = sum([point.getPop()*(euclide(centers[center],point))**2 for point in clusters[center]])
		distorsione+= errore
		errori.append('%.2E' % Decimal(errore))
	return distorsione, '%.2E' % Decimal(distorsione)
	
files = ['212','562','1041']
q = 5

dizKmeans={}
dizGer = {}
dizKmeansnum={}
dizGernum = {}
for f in files:
    dizKmeans[f]=[]
    dizGer[f]=[]

    Data =  ParserCancerData("unifiedCancerData_"+f+".csv")

    contee = sorted(Data,key=lambda x : x.getPop())
    P = sorted(Data,key=lambda x : x.getX())

    for k in range(6,21):
        print "KmeansClustering",f,k
        centers,clusters= kmeans(contee[-k:],contee,k,q)

        distNum,distStr=distorsione(centers,clusters)
        dizKmeans[f].append(distNum)

    print "HierarchicalClustering",f,str(20)
    centers,clusters,dist= Hierarchicalclustering(P,6,6,20)

    dizGer[f]=dist

for f in files:
    plt.clf()
    data = {'k': range(6,21),'hierarchical': dizGer[f], 'kmeans': dizKmeans[f] }
    df=pd.DataFrame(data)

    ax = plt.gca()
    df.plot(kind='line',x='k',y='hierarchical',color='blue',ax=ax)
    df.plot(kind='line',x='k',y='kmeans', color='red', ax=ax)
    plt.savefig('relazione/figures/output'+f+'.png')

    df.set_index("k",inplace=True)
    with open('relazione/table'+f+'.tex', 'w') as tf:
        tf.write(df.to_latex(index=True))


