import heapq

def findMaxST (grafo, source, visited):
    pq, x = [(0, source)], 0
    
    while(len(pq)!=0):
        dequeued = heapq.heappop(pq)

        if(visited[dequeued[1]]==0):
            x += dequeued[0]
        else:
            continue

        visited[dequeued[1]] = 1

        for i in range(0,len(grafo[dequeued[1]])):
            if(visited[grafo[dequeued[1]][i][1]] == 0):
                heapq.heappush(pq, (grafo[dequeued[1]][i][0], grafo[dequeued[1]][i][1]))
    print(-x)



for caso in range(int(input())):
    grafo = []
    visited = []
    linha = input().split()
    for i in range(int(linha[0])+1):
        grafo.append([])
        visited.append(0)
    for i in range(int(linha[1])):
        linha2 = input().split()
        grafo[int(linha2[0])].append((-int(linha2[2]), int(linha2[1])))
        grafo[int(linha2[1])].append((-int(linha2[2]), int(linha2[0])))
    findMaxST(grafo, 1, visited)

