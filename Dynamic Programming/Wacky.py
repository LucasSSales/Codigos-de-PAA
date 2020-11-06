import heapq
import sys

sys.setrecursionlimit(10000)

def findBridges (graph, source, visited, ant):
    visited[source] = 1
    global discoveryTime
    discoveryTime += 1
    disc[source] = discoveryTime
    low[source] = disc[source]

    for i in range(len(graph[source])):
        g = graph[source][i]
        if(visited[g[1]] == 1 and g[1] != ant):
            low[source] = disc[g[1]] if (disc[g[1]] < low[source]) else low[source]
            continue


        if(visited[g[1]] == 0):
            findBridges(graph, g[1], visited, source)
            low[source] = low[g[1]] if (low[g[1]] < low[source]) else low[source]
            if(disc[source] < low[g[1]]):
                bridges.append( (source, g[1]) )

    visited[source] = 2


def dijkstra (grafo, source, dist):
    cont = 0
    pq, dist[source] = [(0, source)], 0
    while(len(pq)!=0):
        cont += 1
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
        if(cont == 10005):
            break
    return dist
    

road, disc, low, visited, dist, bridges = [], [], [], [], [], []
discoveryTime = -1
linha = input().split()
for i in range(int(linha[0])+1):
    road.append([])
    disc.append(-1)
    low.append(-1)
    visited.append(0)
    dist.append(9999)
    

for i in range(int(linha[1])):
    edge = input().split()
    road[int(edge[0])].append( (int(edge[2]), int(edge[1])) )
    road[int(edge[1])].append((int(edge[2]), int(edge[0])))


findBridges(road, 1, visited, 0)
dist = dijkstra(road, 1, dist)

min = 9999

for i in range(len(bridges)):
    min = dist[bridges[i][0]] if(dist[bridges[i][0]] < min) else min
    min = dist[bridges[i][1]] if (dist[bridges[i][1]] < min) else min
    
if(min != 9999):
    print("It's possible with distance " + str(min))
else:
    print("It's not possible")
