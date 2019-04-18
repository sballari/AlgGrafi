from heap import heap
from graph import OrientedGraph

def astar(G,root,dest,hm,speed=1):
    #desc: euristica per la ricerca di cammini minimi da un nodo root ad un nodo dest
    #root: codice stazione di partenza, corrispondente al nodo root
    #dest: codice stazione di arrivo, corrispondente al nodo dest
    #hm: orario di partenza dalla stazione root
    #speed: velocita' kilometri/minuti
    
    #creo la struttura dati heap
    h = heap()

    #calcolo l'orario di arrivo sottostimato alla stazione dest dalla stazione root
    hour,day=OrientedGraph.addMinutes(hm,0,G.distance(root,dest)/speed)

    #eseguo il setup dell'heap
    h.setup([i for i in G.nodes],root,hm,hour,day)
    #estraggo il nodo con prioria' minima
    u = h.extractMin()

    #continuo a ciclare finche' il nodo u (minimo estratto) non e' il nodo dest
    while u != dest:
        #scorro la lista delle adiacenze del nodo minimo
        for v in G.nodes[u].adj:
            #ottengo le info sul trasporto migliore per viaggiare dalla stazione u alla stazione v
            best_v=G.nodes[u].nextTransport(v,h.data[u][2][0],h.data[u][2][1],h.data[u][2][3],h.data[u][2][4])

            #calcolo l'ora di arrivo sottostimata alla stazione destinazione dalla stazione v
            hour,day=OrientedGraph.addMinutes(best_v[0],best_v[1],G.distance(v,dest)/speed)

            #se e' la prima volta che si passa per la stazione v si inserisce nella coda con le sue info
            if h.data[v] == []:
                h.data[v]=[hour,day,best_v]
                h.parent[v]=u
                h.add(v)
            #altrimenti si vede se il trasporto attuale e' migliore di quello localmente trovato precedentemente
            else:
                h.decreaseKey(u,v,[hour,day,best_v])
        u = h.extractMin()

    return h.data,h.parent
