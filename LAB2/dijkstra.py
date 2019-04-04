from heap import heap

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
        u = h.extractMin()

        #scorro la lista delle adiacenze del nodo minimo
        for v in G.nodes[u].adj:
            #ottengo le info sul trasporto migliore per viaggiare dalla stazione u alla stazione v
            best_v=G.nodes[u].nextTransport(v,h.data[u][0],h.data[u][1])

            #se e' la prima volta che si passa per la stazione v si inserisce nella coda con le sue info
            if h.data[v] == []:
                h.data[v]=best_v
                h.parent[v]=u
                h.add(v)
            #altrimenti si vede se il trasporto attuale e' migliore di quello localmente trovato precedentemente
            else:
                h.decreaseKey(u,v,best_v)

    return h.data,h.parent

    '''
    def Astar(G,root,dest,hm,koordMap,speed):
        h = h.heap()
        h.setupE([i for i in G.nodes],root,hm,koordMap,dest,speed)
    '''