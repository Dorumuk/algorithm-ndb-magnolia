# Union Find(합집합 찾기, 서로소 집합 알고리즘) 

# 부모 
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
    parent = [i for i in range(11)]
    unionParent(parent, 1, 2)
    unionParent(parent, 2, 3)
    unionParent(parent, 3, 4)
    unionParent(parent, 4, 5)
    unionParent(parent, 6, 7)
    unionParent(parent, 8, 9)
    unionParent(parent, 9, 10)
    print(findParent(parent, 2, 5))


main()