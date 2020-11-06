import heapq

def dijkstra (grafo, visited, begin, end):
    visited[begin] += 1
    pq, ant, tChegada = [], (-1, -1, -1), 9999
    heapq.heappush(pq, (0, begin, 0))

    while (len(pq)!=0):
        dequeued = heapq.heappop(pq)
        
        if(ant == dequeued):
            continue
            
        visited[dequeued[1]] += 1
        
        if(visited[dequeued[1]] >= 10):
            break

        if(dequeued[1] == end and dequeued[0] < tChegada):
            tChegada = dequeued[0]

        for i in range(len(grafo[dequeued[1]])):
            g = grafo[dequeued[1]][i]
            if (dequeued[0]%3 == 0 and g[0] == 1):
                heapq.heappush(pq, (dequeued[0]+1, g[1], g[0]) )
            elif (dequeued[0]%3 != 0 and g[0] == 0):
                heapq.heappush(pq, (dequeued[0]+1, g[1], g[0]) )
        ant = dequeued

    if(tChegada == 9999):
        print("*")
    else:
        print(tChegada)


grafo, visited = [], []
lista = input().split()

for i in range(int(lista[0])):
    grafo.append([])
    visited.append(0)
    
for i in range(int(lista[-1])):
    g = input().split()
    grafo[int(g[0])].append( (int(g[2]), int(g[1])) )
    
dijkstra(grafo, visited, int(lista[1]), int(lista[2]))