import heapq
import sys

sys.setrecursionlimit(10000)

def findArctPts(graph, source, visited, ant):
    visited[source] = 1
    global discoveryTime
    discoveryTime += 1
    disc[source] = discoveryTime
    low[source] = disc[source]

    for i in range(len(graph[source])):
        g = graph[source][i]
        if (visited[g] == 1 and g != ant):
            low[source] = disc[g] if (disc[g] < low[source]) else low[source]

        if (visited[g] == 0):
            findArctPts(graph, g, visited, source)
            low[source] = low[g] if (low[g] < low[source]) else low[source]
            if (disc[source] <= low[g]):
                arctPoints[source] = 1

    visited[source] = 2


num = int(input())
while(num != 0):
    rede, disc, low, visited, arctPoints = [], [], [], [], []
    discoveryTime = -1

    for i in range(num + 1):
        rede.append([])
        disc.append(-1)
        low.append(-1)
        arctPoints.append(0)
        visited.append(0)

    for i in range(num):
        linha = input().split()
        if(len(linha) == 1 and int(linha[0]) == 0):
            break
        for j in range(1, len(linha)):
            rede[int(linha[0])].append(int(linha[j]))
            rede[int(linha[j])].append(int(linha[0]))

    for i in range(1, len(rede)):
        if(visited[i] == 0 and len(rede[i]) > 0):
            findArctPts(rede, i, visited, i)
            visited[i] = 3

    saida = 0
    for i in range(len(arctPoints)):
        if((arctPoints[i] == 1 and visited[i] != 3) or (arctPoints[i] == 1 and visited[i]==3 and len(rede[i]) > 1)):
            saida += 1
            
    print(saida)
    num = int(input())