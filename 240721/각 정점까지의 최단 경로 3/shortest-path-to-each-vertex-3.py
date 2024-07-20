import sys, heapq

MAX_INT = sys.maxsize

n, m = tuple(map(int, input().strip().split(' ')))

adj_lst = [
    [] for _ in range(n+1)
]

dist = [MAX_INT] * (n+1)
dist[1] = 0

for _ in range(m):
    a, b, e = tuple(map(int, input().strip().split(' ')))
    adj_lst[a].append((b, e))

pq = []
# dist, V
heapq.heappush(pq, (0, 1))

while pq:
    d, v = heapq.heappop(pq)
    if d != dist[v]:
        continue
    for tv, e in adj_lst[v]:
        if dist[tv] > dist[v] + e:
            dist[tv] = dist[v] + e
            heapq.heappush(pq, (dist[tv], tv))

for i in range(len(dist)):
    if i != 0 and i != 1:
        if dist[i] == MAX_INT:
            print(-1)
        else:
            print(dist[i])