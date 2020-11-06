def palindromo (word):
    for i in range(len(matriz)):
        aux = 0
        for j in range(i, len(matriz)):
            if(aux == j):
                matriz[aux][j] = 1
            else:
                if (word[aux] == word[j]):
                    matriz[aux][j] = 2 + matriz[aux + 1][j - 1]
                else:
                    matriz[aux][j] = matriz[aux+1][j] if matriz[aux+1][j] > matriz[aux][j-1] else matriz[aux][j-1]
            aux+=1


n = int(input())
for i in range(n):
    matriz = []
    word = list(input())
    if(word==[]):
        print("0")
    else:
        for j in range(len(word)):
            matriz.append([])
            for k in range(len(word)):
                matriz[j].append(0)
        palindromo(word)
        print(matriz[0][len(word)-1])

