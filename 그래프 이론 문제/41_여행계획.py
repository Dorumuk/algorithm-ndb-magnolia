# 2 3 4 3
def getParent(parent, x):
    if(parent[x] == x):
        return x
    else:
        parent[x] = getParent(parent, parent[x])
        return parent[x]

# 각 노드를 합친다
def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if (a < b): parent[b] = a
    else: parent[a] = b
    
# 같은 부모 노드를 가지고 있는 지 확인한다.
def findParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if (a == b): return 1
    else: return 0
    
def main():
    n, m = map(int, input().split()) # 여행지 수, 여행 계획에 속한 도시 수
    parent = [i for i in range(n + 1)]
    table = []
    for _ in range(n): table.append(list(map(int, input().split())))
    travel_plan = list(map(int, input().split()))

    for i in range(n):
        for j  in range(n):
            if (i == j): break
            if (table[i][j] == 1):
                unionParent(parent, i, j)

    sum = 0
    for k in range(m - 1):
        sum += findParent(parent, travel_plan[k], travel_plan[k + 1])

    if sum == m -1 : print("Yes")
    else : print("No")

main()