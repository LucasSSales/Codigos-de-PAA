def subornar(idx, grana, part, current, memo):
    if(memo[idx][grana]!= -1):
        return memo[idx][grana]
    if(idx == len(tuplas)):
        return 0
    elif(grana-tuplas[idx][2] < 0 ):
        return subornar(idx+1, grana, part, current, memo)
    else:
        if(part==0):
            other = 1
        else:
            other = 0
        put = current-tuplas[idx][part]+tuplas[idx][other] + subornar(idx+1, grana-tuplas[idx][2], part, current-tuplas[idx][part]+tuplas[idx][other], memo)
        ignore = subornar(idx+1, grana, part, current, memo)
        memo[idx][grana] = put if (put > ignore) else ignore
        return memo[idx][grana]

def bfs(source):
    visited[source] = 1
    queue = []
    contPd, contPrism, grana = 0, 0, 0
    queue.append(source)
    while len(queue) != 0:
        deq = queue.pop(0)

        if(deq > pd):
            contPrism += 1
            grana += subornoPrism[deq-pd-1]
        else:
            contPd += 1
            grana += subornoPd[deq-1]

        for i in range(len(grafo[deq])):
            if(visited[grafo[deq][i]] == 0):
                visited[grafo[deq][i]] = 1
                queue.append(grafo[deq][i])
    return (contPd, contPrism, grana)


linha = input().split()

grafo, visited = [], []
grafo.append([])
visited.append(0)

subornoPd, subornoPrism, tuplas = [], [], []
pd, prism, riv, orc = int(linha[0]), int(linha[1]), int(linha[2]), int(linha[3])

pds = input().split()
prisms = input().split()

memoPd, memoPr = [], []

for i in range(pd):
    grafo.append([])
    visited.append(0)
    subornoPd.append(int(pds[i]))
for i in range(prism):
    grafo.append([])
    visited.append(0)
    subornoPrism.append(int(prisms[i]))

#print(subornoPrism)
#print(subornoPd)

for i in range(riv):
    linha = input().split()
    grafo[int(linha[0])].append(int(linha[1]) + pd)
    grafo[int(linha[1])+pd].append(int(linha[0]))
#print(grafo)
k=0
for i in range(1, len(grafo)-1):
    if(visited[i] == 0):
        tuplas.append(bfs(i))
        memoPd.append([])
        memoPr.append([])
        for j in range(orc+1):
            memoPd[k].append(-1)
            memoPr[k].append(-1)
        k+=1
memoPd.append([])
memoPr.append([])
for j in range(orc+1):
    memoPd[k].append(-1)
    memoPr[k].append(-1)

maxPd = subornar(0, orc, 0, pd, memoPd)
maxPrs = subornar(0, orc, 1, prism, memoPr)

if(maxPd < pd):
    maxPd = pd
if(maxPrs < prism):
    maxPrs = prism

print(str(maxPd) + " " + str(maxPrs))
#print(len(memo))