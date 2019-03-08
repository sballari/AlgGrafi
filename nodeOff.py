import random 
import graph

def randomOffNode(G):
    if len(G.nodes) > 0:
        off=random.choice(G.nodes.keys())
        G.subNode(off)

def MaxDegreeOffNode(G):
    if len(G.nodes) > 0:
        off=G.get_Max_Degree_Node()
        print len(G.nodes[off].adj)
        G.subNode(off)