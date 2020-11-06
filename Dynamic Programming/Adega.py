def max(a, b):
    if (a < b):
        a = b
    return a

def adega(price, left, right, year):
    global memo
    if(memo[left][right]!=-1):
        return memo[left][right]
    if(left == right):
        memo[left][right] = price[left]*year
        return memo[left][right]
    else:
        memo[left][right] = max( price[left]*year+adega(price, left+1, right, year+1) , price[right]*year + adega(price, left, right-1, year+1) )
        return memo[left][right]


price = []
memo = []

casos = int(input())

for i in range(casos):
    price.append(int(input()))
    memo.append([])
    for j in range(casos):
        memo[i].append(-1)

print(adega(price, 0, len(price)-1, 1))
