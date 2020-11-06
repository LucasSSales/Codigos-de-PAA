s = input().split()
l = len(s)
for i in range(l):
    s[i] = int(s[i])

d = int(input())

s.append(d)
sum = sum(s)
l = len(s)

tabela = []
for i in range(sum//2 + 1):
    tabela.append([])
    for j in range(l + 1):
        tabela[i].append(-1)
        if(i == 0):
            tabela[i][j] = 1
        if(i!=0 and j==0):
            tabela[i][j] = 0

if (sum % 2 == 1):
    print("No")
else:
    for i in range(sum//2 + 1):
        tabela[i][0] = 0
    for j in range(l + 1):
        tabela[0][j] = 1
        
    for i in range(1, sum//2 +1):
        for j in range(1, l + 1):
            tabela[i][j] = tabela[i][j-1]
            if(i >= s[j-1]):
                if(tabela[i][j] < tabela[i - s[j-1]][j-1]):
                    tabela[i][j] = tabela[ i - s[j-1] ][j-1]

    if(tabela[sum//2][l] == 1):
        print("Yes")
    else:
        print("No")
