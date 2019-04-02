import heap
import graph

def INITSSSP(h,G,station,hm):
    for i in G.nodes:
        h.d[i]=None
        h.p[i]=None
    h.d[station]=hm

def algo(G,root,hm):
    h = heap.heap()
    h.setup([i for i in G.nodes],root,graph.Hour(hm),0)
    count =0
    while len(h.deque) > 0:
        u = h.extractMin()
        #print "---------------------------------------------------"            

        #print 
        #print count, len(h.deque)
        for v in G.nodes[u].adj:
            best_v=G.nodes[u].nextTransport(v,h.data[u][0],h.data[u][1])
            #print "data: ",v,str(h.data[u][0]),str(h.data[u][1]),[str(i) for i in best_v]
            if h.data[v] == []:
                h.data[v]=best_v
                h.parent[v]=u
                h.add(v,best_v)

                #print "add"
            else:
                h.decreaseKey(u,v,best_v)
                #print "descrease"
        count+=1
        #print 
        #print "coda"
        
        #for i in h.deque:
        #    print str(i) ,[str(j) for j in h.data[i]]
        
        #if len(h.deque)> 0 and h.data[h.deque[0]][0].fminute+h.data[h.deque[0]][1]*1440<h.data[A][0].fminute:
        #    break;
        
    return h