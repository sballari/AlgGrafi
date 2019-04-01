import heap
import graph

def INITSSSP(h,G,station,hm):
    for i in G.nodes:
        h.d[i]=None
        h.p[i]=None
    h.d[station]=hm

def algo(G):
    A="500000079"
    h = heap.heap()
    tstart=graph.Hour("01300")
    INITSSSP(h,G,A,[tstart,0])
    h.add(A,[tstart,0])
    count =0
    while len(h.deque) > 0:
        u = h.extractMin()
        #print str(u[0]),[str(i) for i in u[1]]
        u=u[0]
        for v in G.nodes[u].adj:
            next_transport=G.nodes[u].nextTransport(v,h.d[u][0],h.d[u][1])
            #print "data: ",str(h.d[u][0]),str(h.d[u][1]),[str(i) for i in next_transport]
            if h.d[v] == None:
                h.RELAX(u,v,next_transport)
                h.add(v,next_transport)
                print "add"
            else:
                if next_transport[0].fminute + next_transport[1]*1440 < h.d[v][0].fminute+h.d[v][1]*1440:
                    print str(h.deque[h.dc[v]][1][0])
                    h.RELAX(u,v,next_transport)
                    h.decreaseKey(v,next_transport)
                    print str(h.deque[h.dc[v]][1][0])
                    print "descrease"
        count+=1
        if count == 20:
            for i in h.deque:
                print [str(z) for z in h.d[i[0]]], str(i[0]),[str(j) for j in i[1]]
            
            break;
    return h