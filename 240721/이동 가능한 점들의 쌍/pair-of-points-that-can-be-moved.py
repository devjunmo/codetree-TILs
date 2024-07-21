import sys

MAX_INT = sys.maxsize

# 빨간점일때만 위치 갱신 (1~P)
N, M, P, Q = tuple(map(int, input().strip().split(' ')))

dist = [
    [MAX_INT] * (N+1) for _ in range(N+1)
]

for m in range(M):
    src, tgt, cost = tuple(map(int, input().strip().split(' ')))
    dist[src][tgt] = cost

queries = []

for q in range(Q):
    queries.append(tuple(map(int, input().strip().split(' '))))

for k in range(1, P+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dist[i][k] == MAX_INT or dist[k][j] == MAX_INT:
                continue
            nxt_dst = dist[i][k] + dist[k][j]
            if dist[i][j] > nxt_dst:
                dist[i][j] = nxt_dst

cnt = 0
cost_sum = 0

for s, t in queries:
    v = dist[s][t]
    if v != MAX_INT:
        cnt+=1
        cost_sum+=v

print(cnt)
print(cost_sum)