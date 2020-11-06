import heapq

def dijkstra (grafo, source, end, visited):
    dist = []
    pq = [(0, source)]
    while(len(pq)!=0):
        dequeued = heapq.heappop(pq)

        distancia,dequeued = dequeued[0], dequeued[1]
        visited[dequeued] =1

        if(dequeued == end):
            dist.append(distancia)

        for i in range(0,len(grafo[dequeued])):
            g = grafo[dequeued][i]
            if(visited[g[1]]==0 or g[1]==end):
                heapq.heappush(pq, (distancia+g[0], g[1]) )

    if(len(dist)<=2):
        print(-1)
    else:
        dist.sort()
        x = dist[0]
        i=1
        for i in range(len(dist)):
            if(dist[i]>x):
                break
        if(dist[i]==x):
            print(-1)
        else:
            print(dist[i])


casos = input().split()
while (int(casos[0]) != 0 and casos[1] != 0):
    graph = []
    visited = []

    for i in range(int(casos[0])):
        graph.append([])
        visited.append(0)

    dados = input().split()
    for i in range(int(casos[1])):
        edge = input().split()
        graph[int(edge[0])].append((int(edge[2]), int(edge[1])))


    dist = dijkstra(graph, int(dados[0]), int(dados[1]), visited)
    casos = input().split()