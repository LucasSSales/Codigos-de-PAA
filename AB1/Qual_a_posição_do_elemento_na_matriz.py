def binary_search (item, lista, i, f, c):
    x = 1
    while x:
        m = int((i+f)//2)
        if(lista[m] == item):
            print("YES WITH "+ str(int(m/c)+1) +" AND " + str(int(m%c)+1))
            x = 0
        elif(f<=i):
            print("NO")
            x = 0
        elif(lista[m] > item):
            f = m-1
        else:
            i = m+1

matriz, coord, buscar = [], [int(i) for i in list(input().split())], []

for i in range(0, coord[0]):
    lista = list(input().split())
    for j in range(0, coord[1]):
        matriz.append(int(lista[j]))

busca, buscar = int(input()), [int(i) for i in list(input().split())]

for i in range(0, busca):
    binary_search(buscar[i], matriz, 0, len(matriz)-1, coord[1])