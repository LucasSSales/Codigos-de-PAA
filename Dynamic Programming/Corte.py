def max(a, b):
    if (a < b):
        a = b
    return a


def cutRods(size, v, memo):
    for i in range(size):
        best = 0
        k = i
        for j in range(i+1):
            best = max(best, v[j] + memo[k])
            k -= 1
        memo[i + 1] = best
    print(memo[size])


case = int(input())
while (case != 0):
    v, memo = [], [0]

    for i in range(case):
        v.append(int(input()))
        memo.append(-1)

    cutRods(case, v, memo)
    case = int(input())