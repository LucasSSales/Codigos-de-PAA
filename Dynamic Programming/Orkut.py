x = int(input())
case = 1
while (x != 0):
    dic = {}
    visited = {}
    indegree = {}
    friends = input().split()

    for i in range(len(friends)):
        if friends[i] not in visited:
            visited[friends[i]] = 0
        if friends[i] not in dic:
            dic[friends[i]] = []
        if friends[i] not in indegree:
            indegree[friends[i]] = -1



    for i in range(len(friends)):
        linha = input().split()

        indegree[linha[0]] = int(linha[1])


        for j in range(int(linha[1])):
            if linha[j+2] not in dic:
                dic[linha[j+2]] = [linha[0]]
            else:
                dic[linha[j+2]].append(linha[0])

    conf = 0

    print("Teste "+str(case))

    queue = []
    for i in range(len(friends)):
        if(indegree[friends[i]] == 0):
            queue.append(friends[i])

    stack = []

    if(len(queue) == 0):
        print("impossivel", end="")
    else:
        conf = 0
        while len(queue) != 0 :
            deq = queue.pop(0)

            for i in range(len(dic[deq])):
                indegree[dic[deq][i]] -= 1
                if(visited[dic[deq][i]] == 1):
                    conf = 1
                    break
                if(indegree[dic[deq][i]] == 0):
                    queue.append(dic[deq][i])
                    visited[dic[deq][i]] = 1

            stack.append(deq)

        if(conf == 1 or len(stack) != len(friends)):
            print("impossivel", end="")
        else:
            for i in range(len(stack)):
                print(stack[i], end="")
                if(i!= len(stack)-1):
                    print(" ", end="")
    print("\n")

    case += 1
    x = int(input())
