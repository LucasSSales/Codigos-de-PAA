def mochila (item, peso):
    if(memo[item][peso]!= -1):
        return memo[item][peso]
    if(item == n):
        return 0
    if(peso-w[item] < 0):
        return mochila(item+1, peso)
    else:
        put = price[item] + mochila(item+1, peso-w[item])
        ignore = mochila(item+1, peso)
        memo[item][peso] = put if (put > ignore) else ignore
        return memo[item][peso]


for i in range(int(input())):
    memo = []
    price, w = [], []
    n = int(input())
    for j in range(n):
        linha = input().split()
        price.append(int(linha[0]))
        w.append(int(linha[1]))
    saida = 0
    for j in range(int(input())):
        pesoM = int(input())

        for k in range(n + 1):
            memo.append([])
            for l in range(pesoM + 1):
                memo[k].append(-1)
        saida += mochila(0, pesoM)
    print(saida)
