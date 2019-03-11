import random 
import graph

def randomOffNode(G):
    if len(G.nodes) > 0:
        off=random.choice(G.nodes.keys())
        G.subNode(off)
        G.maxDegree=''

def MaxDegreeOffNode(G):
    if len(G.nodes) > 0:
        #print len(G.nodes[off].adj)
        G.subNode(G.maxDegree)
        G.maxDegree=''
