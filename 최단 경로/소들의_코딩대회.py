INF = int(1e9) # 1000000000.0
n, m = map(int, input().split()) # m : 간선, round
# 2차원 리스트(그래프를 표현)
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         if a == b:
#             graph[a][b] = INF

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1): # 거쳐가는 노드
    for a in range(1, n + 1): # 출발 노드
        for b in range(1, n + 1): # 도착 노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

sum_tmp = [0 for i in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한
        if graph[a][b] != INF:
            sum_tmp[a] += 1
            sum_tmp[b] += 1

cnt = 0
for i in sum_tmp:
	if i >= n - 1: cnt+=1

print(cnt)

# 수행된 결과를 출력
# for a in range(1, n + 1):
#     for b in range(1, n + 1):
#         # 도달할 수 없는 경우, 무한
#         if graph[a][b] == INF:
#             print("inf", end=" ")
#         else:
#             print(graph[a][b], end= " ")
#     print()