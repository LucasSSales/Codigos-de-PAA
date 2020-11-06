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
            parentC[g[1]] = dequeued
            dist[g[1]] = distancia + g[0]
            heapq.heappush(pq, (distancia+g[0], g[1]) )
    return dist


def ford_fuckerson(source):
    conf = 0
    visited = []
    for i in range(locais):
        visited.append(0)
    visited[source] = 1
    queue = []
    max_flow = 99999
    queue.append(source)
    while len(queue)!=0 :
        deq = queue.pop(0)

        if(deq == destino):
            conf = 1
            break

        for i in range(len(percursoTotal[deq])):
            g = percursoTotal[deq][i]

            if(visited[g] == 0 and matriz[deq][g] > 0 and parentC[guiaCidades[g]] == -1):

                if (matriz[deq][g] < max_flow):
                    max_flow = matriz[deq][g]

                parent[g] = deq
                visited[g] = 1
                queue.append(g)

    if(conf == 1):
        return max_flow
    else:
        return -1


def tiraGargalo(min, begin, end):
    place = end
    while place!= begin :
        matriz[parent[place]][place] -= min
        place = parent[place]




guiaCidades = [] 
percursoCidades = [] 
percursoTotal = []
dist = []
parentC = []
parent = []
filaDeEspera = []
matriz = []

locais = int(input())
cidades = int(input())

for i in range(locais):
    guiaCidades.append(0)
    percursoTotal.append([])
    matriz.append([])
    parent.append(-1)
    for j in range(locais):
        matriz[i].append(-1)

for i in range(cidades):
    x = input().split()
    percursoCidades.append([])
    dist.append(9999)
    parentC.append(-1)
    for j in range(len(x)):
        guiaCidades[int(x[j])] = i

roads = int(input())

for i in range(roads):
    m = input().split()
    percursoTotal[int(m[0])].append(int(m[1]))
    matriz[int(m[0])][int(m[1])] = int(m[2])
    if(int(m[3]) != 0):
        percursoCidades[guiaCidades[int(m[0])]].append( ( int(m[3]), guiaCidades[int(m[1])] ) )

linha = input().split()
origem = int(linha[0])
destino = int(linha[1])

print(dijkstra(percursoCidades, guiaCidades[origem], dist)[guiaCidades[destino]])

place = guiaCidades[destino]
while place != guiaCidades[origem]:
    aux = parentC[place]
    parentC[place] = -1
    place = aux

flow = 0
f = ford_fuckerson(origem)
while f!= -1 :
    tiraGargalo(f, origem, destino)
    flow += f
    f = ford_fuckerson(origem)

print(flow)
