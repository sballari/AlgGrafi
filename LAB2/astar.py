from heap import heap
from graph import OrientedGraph
def checkheap(i,coda,data):
    if i > len(coda):
        return True
    ok=False
    if 2*i+1 < len(coda):
        if data[coda[i]][0].fminute+data[coda[i]][1]*1440 <= data[coda[2*i+1]][0].fminute+data[coda[2*i+1]][1]*1440:
            ok=checkheap(2*i+1,coda,data)
        else:
            print data[coda[i]][0].fminute+data[coda[i]][1]*1440 , data[coda[2*i+1]][0].fminute+data[coda[2*i+1]][1]*1440
            return False
    else:
        return True
    if ok == True:
        if 2*i+2 < len(coda):
            if data[coda[i]][0].fminute+data[coda[i]][1]*1440 <= data[coda[2*i+2]][0].fminute+data[coda[2*i+2]][1]*1440:
                ok=checkheap(2*i+2,coda,data)
            else:
                print data[coda[i]][0].fminute+data[coda[i]][1]*1440 , data[coda[2*i+2]][0].fminute+data[coda[2*i+2]][1]*1440
                return False
        else:
            return True
    else:
        return False
    return ok
def astar(G,root,dest,hm,speed=2):
    h = heap()

    hour,day=OrientedGraph.addMinutes(hm,0,G.distance(root,dest)/speed)

    h.setup([i for i in G.nodes],root,hm,hour,day)
    u = h.extractMin()
    c=0
    while u != dest:
        for v in G.nodes[u].adj:

            best_v=G.nodes[u].nextTransport(v,h.data[u][2][0],h.data[u][1],h.data[u][2][3],h.data[u][2][4])
            hour,day=OrientedGraph.addMinutes(best_v[0],best_v[1],G.distance(v,dest)/speed)

            if h.data[v] == []:
                h.data[v]=[hour,day,best_v]
                h.parent[v]=u
                h.add(v)
            else:
                h.decreaseKey(u,v,[hour,day,best_v])

        u = h.extractMin()
        c+=1

    print "nodi visitati:",c

    return h.data,h.parent
