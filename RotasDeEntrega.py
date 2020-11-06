import heapq

def dijkstra (grafo, source, dist):
    pq, dist[source] = [(0, source)], 0
    while(len(pq)!=0):
        dequeued = heapq.heappop(pq)
        distancia,dequeued = dequeued[0], dequeued[1]
        if(distancia > dist[dequeued]):
            continue
        for i in range(0,len(grafo[dequeued])):
            g = grafo[dequeued]
            if((distancia+1) > dist[g[i]]):
                continue
            dist[g[i]] = distancia + 1
            heapq.heappush(pq, (distancia+1, g[i]) )
    return dist

print("SHIPPING ROUTES OUTPUT")
for case in range(0, int(input())):
    graph = {}
    dist = {}
    dados = [int(i) for i in (input().split())]
    portos = input().split()

    for i in range(0, len(portos)):
        graph[portos[i]] = []
        dist[portos[i]] = 9999

    for i in range(0, dados[1]):
        aquavias = input().split()
        graph[aquavias[0]].append(aquavias[1])
        graph[aquavias[1]].append(aquavias[0])

    print("\nDATA SET  "+str(case+1)+"\n")
    for i in range(0, dados[2]):
        encomendas = input().split()
        dijkstra(graph, encomendas[1], dist)
        if(dist[encomendas[2]]!=9999):
            print("$" +str(int(encomendas[0])*dist[encomendas[2]]*100))
        else:
            print("NO SHIPMENT POSSIBLE")
        for i in range(0, len(portos)):
            dist[portos[i]] = 9999
print("\nEND OF OUTPUT")
