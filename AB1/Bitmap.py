
def verificar (bitmap, li, ci, lf, cf):
    v = bitmap[li][ci]
    for i in range(li, lf+1):
        for j in range(ci, cf+1):
            if(bitmap[i][j] != v):
                return -1
    return v

def recursao(bitmap, li, ci, lf, cf):
    if(verificar(bitmap, li, ci, lf, cf) == -1):
        global cont
        cont +=1
        print("D", end="")
        if (cont % 50 == 0):
            print ()

        lm, cm = int(((lf+1)+li)/2), int(((cf+1)+ci)/2)
        if(((lf-li)+1)%2 != 0): lm += 1
        if(((cf-ci)+1)%2 != 0): cm += 1

        recursao(bitmap, li, ci, lm - 1, cm - 1)
        if((cf-ci)>0): recursao(bitmap, li, cm, lm - 1, cf)
        if((lf-li)>0): recursao(bitmap, lm, ci, lf, cm - 1)
        if((cf-ci)>0 and (lf-li)>0): recursao(bitmap, lm, cm, lf, cf)
    else:
        global cont
        cont +=1
        print(bitmap[li][ci], end="")
        if (cont % 50 == 0):
            print ()

def intzar_lista(lista):
    lista = list(lista.split())
    lista = [int(i) for i in lista]
    return list(lista)

bitmap = []
for i in range(0, int(input())):
    lista = intzar_lista(str(input()))
    l, c = lista[0], lista[1]
    for j in range(0, l):
        cont = 0
        bitmap.append([int(i) for i in list(input())])
    recursao(bitmap, 0, 0, l-1, c-1)
    bitmap.clear()
    print("")