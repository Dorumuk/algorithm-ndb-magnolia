# 6 [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]] 4

n = int(input())
roads = list(input())
k = int(input())
villages = [False for _ in range(n)]
print(n, roads, k)

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

check(1, 0)
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