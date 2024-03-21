import heapq

n = int(input())
pq = []

for _ in range(n):
    v = int(input())
    if v == 0:
        if len(pq) == 0:
            print(0)
        else:
            min_v = heapq.heappop(pq)
            print(min_v)
    else:
        heapq.heappush(pq, v)