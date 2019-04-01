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
    h.setup([i for i in G.nodes],"500000079",graph.Hour("01300"),0)
    count =0
    while len(h.deque) > 0:
        u = h.extractMin()
        print len(h.deque)
        #print 
        #print u
        for v in G.nodes[u].adj:
            best_v=G.nodes[u].nextTransport(v,h.data[u][0],h.data[u][1])
            #print "data: ",v,str(h.data[u][0]),str(h.data[u][1]),[str(i) for i in best_v]

            if h.data[v] == None:
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
        """
        for i in h.deque:
            print str(i) ,[str(j) for j in h.data[i]]
        
        if count == 3:
            print "---------------------------------------------------"
            for i in h.deque:
                print str(i) ,[str(j) for j in h.data[i]]
            
            break;
        """
    return h