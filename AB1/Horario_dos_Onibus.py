import heapq

def dijkstra (grafo, source, dist, tempoDeViagem):
    pq, dist[source] = [(0, source)], 0
    ant = (-1, -1)

    while (len(pq) != 0):
        
        dequeued = heapq.heappop(pq)
        
        if(ant == dequeued):
            continue
        if dequeued[0] > dist[dequeued[1]]:
            continue

        if dequeued[1] in grafo:
            for i in range(0, len(grafo[dequeued[1]])):
                g = grafo[dequeued[1]][i]
    
                if (dequeued[1] == source or dequeued[0]%g[0]==0):
                    espera = 0
                else:
                    espera = ((int(dequeued[0] / g[0]) + 1) * g[0]) - dequeued[0]
    
                if ((dequeued[0] + espera + tempoDeViagem) > dist[g[1]]):
                    continue
    
                dist[g[1]] = dequeued[0] + espera + tempoDeViagem
                heapq.heappush(pq, (dequeued[0] + espera + tempoDeViagem, g[1]))
        ant = dequeued

    return dist

for caso in range(0, int(input())):
    grafo, dist = {}, {}
    destino = input().split()
    
    grafo[destino[0]], grafo[destino[1]] = [], []
    for i in range(0, int(destino[3])):
        rotas = input().split()

        dist[rotas[0]] = 9999
        dist[rotas[1]] = 9999

        if rotas[0] not in grafo:
            grafo[rotas[0]] = [(int(rotas[2]), rotas[1])]
        else:
            grafo[rotas[0]].append((int(rotas[2]), rotas[1]))


    if destino[0] in grafo:
        dist = dijkstra(grafo, destino[0], dist, int(destino[2]))
        if destino[1] not in dist or (dist[destino[1]] == 9999):
            print("Caso #" + str(caso+1) + ": Destino inalcancavel")
        else:
            print("Caso #" + str(caso + 1) + ": " + str(dist[destino[1]]) + " anticalmas")
    else:
        print("Caso #" + str(caso+1) + ": Destino inalcancavel")
        