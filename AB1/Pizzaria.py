import heapq

def dijkstra (grafo, source, dist):
    pq, dist[source] = [(0, source)], 0
    while(len(pq)!=0):
        dequeued = heapq.heappop(pq)
        distancia,dequeued = dequeued[0], dequeued[1]
        if(distancia > dist[dequeued]):
            continue
        for i in range(0,len(grafo[dequeued])):
            g = grafo[dequeued][i]
            if((distancia+g[0]) > dist[g[1]]):
                continue
            dist[g[1]] = distancia + g[0]
            heapq.heappush(pq, (distancia+g[0], g[1]) )
    return dist

graph = []
for case in range(0, int(input())):
    lista = [int(i) for i in (input().split())]
    for i in range(lista[0]+1):
        graph.append([])
    dist = (lista[0]+1)*[9999]

    for j in range(0, lista[1]):
        l = [int(i) for i in (input().split())]
        node1, node2 = (l[2], l[0]), (l[2], l[1])
        graph[node1[1]].append(node2)
        graph[node2[1]].append(node1)

    num, orders = int(input()), [int(i) for i in (input().split())]
    d, dist = 0, dijkstra(graph, 1, dist)

    for j in range(0, num):
        d += dist[orders[j]]

    print("caso " + str(case+1) + ": " + str(d*2))
    graph.clear()