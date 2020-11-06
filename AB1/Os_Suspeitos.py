def bfs(grafo, source, visited):
    cont = 1
    visited[source] = 1;
    queue = []
    queue.append(source)
    while (len(queue) != 0):
        dequeued = queue.pop(0)
        for i in range(len(grafo[dequeued])):
            if (visited[grafo[dequeued][i]] == 0):
                visited[grafo[dequeued][i]] = 1
                queue.append(grafo[dequeued][i])
                cont += 1
    print(cont)


def unvisited(visited):
    for i in range(len(visited)):
        visited[i] = 0


def addNodes(grafo, lista):
    n1 = lista.pop(0)
    for i in range(len(lista)):
        grafo[n1].append(lista[i])
        grafo[lista[i]].append(n1)
    #return grafo


def intzar_lista(lista):
    lista = list(lista.split())
    lista = [int(i) for i in lista]
    return list(lista)


linha = intzar_lista(str(input()))
tam, num = linha[0], linha[1]

while (tam != 0 or num != 0):
    grafo = [[x] for x in range(tam)]
    visited = tam * [0]

    for i in range(0, num):
        linha = intzar_lista(str(input()))
        linha.pop(0)
        addNodes(grafo, linha)

    bfs(grafo, 0, visited)
    linha = intzar_lista(str(input()))
    tam, num = linha[0], linha[1]

