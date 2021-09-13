# 6 [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]] 4

n = int(input())
m = int(input())
roads = []
for i in range(m):
    roads.append(list(map(int, input().split())))
k = int(input())

villages = [False for _ in range(n)]

def check ( node , spended_time, prev_node, used_loads):
    if not villages[node -1]:
        if spended_time <= k:
            villages[node -1] = True
        else: return # k 이상 시간이 걸리는 노드는 차단.
    # else: return # true node를 지나가는 경우를 차단함.

    for idx, road in enumerate(roads):
        new_spended_time = spended_time + road[2]
        try: used_loads.index(idx)
        except:
            used_loads.append(idx)
            if road[0] == node and road[1] != prev_node:
                check(road[1], new_spended_time, node, used_loads)
            elif road[1] == node and road[0] != prev_node:
                check(road[0], new_spended_time, node, used_loads)
check(1, 0, -1, [])
print(villages)
print(villages.count(True))

'''
def check ( node , spended_time):
    if not villages[node -1]: 
        if spended_time <= k:
            villages[node -1] = True
    else:
        return

    for road in roads:
        new_spended_time = spended_time + road[2]
        if road[0] == node:
            check(road[1], new_spended_time)
        elif road[1] == node:
            check(road[0], new_spended_time)

def solution(N, road, K):
    answer = 0
    global villages, roads, k
    villages = [False for _ in range(N)]
    roads = road
    k = K

    check(1, 0)
    
    return villages.count(True)
    '''