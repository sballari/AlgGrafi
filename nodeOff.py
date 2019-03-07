import random 
import graph

def randomOffNode(G):
    off=random.choice(G.nodes)
    G.subNode(off)