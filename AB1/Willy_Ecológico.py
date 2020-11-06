def eco_willy (begin, end, lista, wood, finish):
    mid, total = int((end + begin)/2), 0

    for i in range(mid, finish):
        total += (lista[i] - lista[mid])

    if(total == wood or begin == mid):
        print(lista[mid])
    elif(total > wood):
        eco_willy(mid, end, lista, wood, finish)
    elif(total < wood):
        eco_willy(begin, mid, lista, wood, finish)

linha1, linha2 = str(input()), str(input())

linha1 = list(linha1.split())

linha2 = list(linha2.split())
linha2 = [int(i)for i in linha2]
linha2.sort()

eco_willy(0, int(linha1[0])-1, linha2, int(linha1[1]), int(linha1[0]))
