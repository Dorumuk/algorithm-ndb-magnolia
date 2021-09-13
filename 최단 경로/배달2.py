# 6 [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]] 4

n = int(input())
m = int(input())
roads = []
for i in range(m):
    roads.append(list(map(int, input().split())))
k = int(input())
villages = [False for _ in range(n)]

def check ( node , spended_time, prev_node):
    villages[node -1] = True

    for road in roads:
        new_spended_time = spended_time + road[2]
        if (new_spended_time <=k):
            if road[0] == node and road[1] != prev_node:
                check(road[1], new_spended_time, node)
            elif road[1] == node and road[0] != prev_node:
                check(road[0], new_spended_time, node)
check(1, 0, -1)
print(villages.count(True))