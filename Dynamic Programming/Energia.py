import sys
sys.setrecursionlimit(100000000)

def mochilaExT(prog, freq):
    if (memo[prog][freq] != -1):
        return memo[prog][freq]

    min = 999999999999999
    for i in range(f):
        new = tabela[prog][freq] + mochilaExT(prog - 1, i)
        if (i != freq):
            new += mudarF
        if (new < min):
            min = new
    memo[prog][freq] = min
    return min

linha = input().split()
f, p, e, a = int(linha[0]), int(linha[1]), int(linha[2]), int(linha[3])

while (f != 0 or p != 0 or e != 0 or a != 0):

    tabela = []
    memo = []
    mudarF = e * a
    
    for i in range(p):
        tabela.append([])
        memo.append([])
        for j in range(f):
            linha = input().split()
            tabela[i].append(int(linha[0]) * int(linha[1]))
            if(i == 0):
                if(j==0):
                    memo[i].append(tabela[i][j])
                else:
                    memo[i].append(tabela[i][j]+mudarF)
            else:
                memo[i].append(-1)
                
    tabela.append([])
    memo.append([])
    for i in range(f):
        memo[p].append(-1)
        tabela[p].append(0)

    saida = mochilaExT(len(tabela)-1, 0)

    min = 9999999999999
    for i in range(f):
        if(memo[len(memo)-2][i] < min):
            min = memo[len(memo)-2][i]
    print(min)

    linha = input().split()
    f, p, e, a = int(linha[0]), int(linha[1]), int(linha[2]), int(linha[3])
