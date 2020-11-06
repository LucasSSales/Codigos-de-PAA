def countSort (lista):
    count = 10000000 * [0]
    for i in range(0, len(lista)):
        count[lista[i]] += 1

    x= 0
    for i in range(0, len(count)):
        x += count[i]
        count[i] = x

    sorted = len(lista) * [0]

    for i in range(0, len(lista)):
        sorted[count[lista[i]]-1] = lista[i]
        count[lista[i]] -= 1

    for i in range (0, len(sorted)):
        print(sorted[i])




lista = [int(i) for i in (input().split())]
countSort (lista)
