from heap import heap

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

def dijkstra(G,root,hm):
    #desc: algoritmo per la ricerca di cammini minimi da un nodo root
    #root: codice stazione di partenza, corrispondente al nodo root
    #hm: orario di partenza dalla stazione root

    #creo la struttura dati heap
    h = heap()

    #eseguo il setup dell'heap
    h.setup([i for i in G.nodes],root,hm)

    #continuo l'esecuzione finche' la coda non rimane vuota
    while len(h.deque) > 0:
        #estraggo il nodo con tempo di arrivo minimo nella coda e aggiorno
        #print checkheap(0,h.deque,h.data)
        u = h.extractMin()

        #scorro la lista delle adiacenze del nodo minimo
        for v in G.nodes[u].adj:
            #ottengo le info sul trasporto migliore per viaggiare dalla stazione u alla stazione v
            best_v=G.nodes[u].nextTransport(v,h.data[u][0],h.data[u][1],h.data[u][2][3],h.data[u][2][4])

            #se e' la prima volta che si passa per la stazione v si inserisce nella coda con le sue info
            if h.data[v] == []:
                h.data[v]=[best_v[0],best_v[1],best_v]
                h.parent[v]=u
                h.add(v)
            #altrimenti si vede se il trasporto attuale e' migliore di quello localmente trovato precedentemente
            else:
                h.decreaseKey(u,v,best_v)

    storage = dict()

    for station in h.data:
        if len(h.data[station]) < 1:
            storage[station]= []
        else:
            storage[station]= h.data[station][2]
    return storage,h.parent

    '''
    def Astar(G,root,dest,hm,koordMap,speed):
        h = h.heap()
        h.setupE([i for i in G.nodes],root,hm,koordMap,dest,speed)
    '''