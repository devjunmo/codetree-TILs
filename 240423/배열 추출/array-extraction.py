import heapq

n = int(input())
pq = []

for _ in range(n):
    v = int(input())
    if v == 0:
        if not pq:
            print(0)
        else:
            pv = heapq.heappop(pq)
            print(-pv)
    else:
        heapq.heappush(pq, -v)