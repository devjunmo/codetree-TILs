import heapq
import sys

n, m = tuple(map(int, input().strip().split(' ')))
k = int(input().strip())

# x, y, 가중치
graph = [
    [] for _ in range(n+1)
]

dist = [sys.maxsize] * (n+1)

for _ in range(m):
    x, y, z = tuple(map(int, input().strip().split(' ')))
    graph[x].append((y, z))
    graph[y].append((x, z))

dist[k] = 0

pq = []

heapq.heappush(pq, (0, k)) # (거리, 정점) push

while pq:
    min_dst, min_v = heapq.heappop(pq)
    # 최신 거리 배열과 다르다면 pass
    if min_dst != dist[min_v]:
        continue
    
    for tgt_v, tgt_dst in graph[min_v]:
        new_dist = dist[min_v] + tgt_dst
        if dist[tgt_v] > new_dist:
            dist[tgt_v] = new_dist
            heapq.heappush(pq, (new_dist, tgt_v))

for i in range(1, n+1):
    if dist[i] == sys.maxsize:
        print(-1)
    else:
        print(dist[i])