from heap import heap
from graph import OrientedGraph

def astar(G,root,dest,hm,speed=1):
    h = heap()

    hour,day=OrientedGraph.addMinutes(hm,0,G.distance(root,dest)/speed)

    h.setup([i for i in G.nodes],root,hm,hour,day)
    u = h.extractMin()
    c=0
    while u != dest:
        #for i in h.deque:
        #    if len(h.data[i]) > 0:
        #        print i,str(h.data[i][0]),str(h.data[i][1]),[str(j) for j in h.data[i][2]]
        #    else:
        #        print i,[]
        #print "+++++++++++++++++++++++++++++++++++++++++++++++++++"
        for v in G.nodes[u].adj:
            #print h.data[u][2][0]
            best_v=G.nodes[u].nextTransport(v,h.data[u][2][0],h.data[u][2][1],h.data[u][2][3],h.data[u][2][4])
        #    print [str(i) for i in best_v]
            #print G.distance(v,dest)
            hour,day=OrientedGraph.addMinutes(best_v[0],best_v[1],G.distance(v,dest)/speed)
        #    print "nuovo orario di arrivo",str(hour), day
            if h.data[v] == []:
                h.data[v]=[hour,day,best_v]
                h.parent[v]=u
                h.add(v)
            else:
                h.decreaseKey(u,v,[hour,day,best_v])
            #print str(h.data[v][0]),h.data[v][1],[str(j) for j in h.data[v][2]]
        #print "------------------------------" 
        #for i in h.deque:
        #    if len(h.data[i]) > 0:
        #        print i,str(h.data[i][0]),str(h.data[i][1]),[str(j) for j in h.data[i][2]]
        #    else:
        #        print i,[]
        #print "---------------------------------------------------"
        #print checkheap(i,h.deque,h.data)
        u = h.extractMin()
        c+=1
        #if c == 3:
        #    break;

    print "nodi visitati:",c

    return h.data,h.parent
