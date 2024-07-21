import sys

MAX_INT = sys.maxsize

# 입력 받기
N, M, P, Q = map(int, input().strip().split())

# 그래프 초기화
dist = [[MAX_INT] * (N + 1) for _ in range(N + 1)]
red_points = set(range(1, P + 1))

# 자기 자신으로 가는 거리는 0
for i in range(1, N + 1):
    dist[i][i] = 0

# 간선 정보 입력받기
for _ in range(M):
    src, tgt, cost = map(int, input().strip().split())
    dist[src][tgt] = cost

# 쿼리 정보 입력받기
queries = [tuple(map(int, input().strip().split())) for _ in range(Q)]

# 플로이드-워셜 알고리즘 수행
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist[i][k] < MAX_INT and dist[k][j] < MAX_INT:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

cnt = 0
cost_sum = 0

# 쿼리 처리
for s, t in queries:
    min_cost = MAX_INT
    for r in red_points:
        if dist[s][r] < MAX_INT and dist[r][t] < MAX_INT:
            min_cost = min(min_cost, dist[s][r] + dist[r][t])
    
    if min_cost < MAX_INT:
        cnt += 1
        cost_sum += min_cost

print(cnt)
print(cost_sum)