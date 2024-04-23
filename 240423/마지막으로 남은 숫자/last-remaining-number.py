import heapq

n = int(input())
pq = list(map(int, input().strip().split(' ')))
pq = [-x for x in pq]
heapq.heapify(pq)

while len(pq) > 1:
    v1 = heapq.heappop(pq)
    v2 = heapq.heappop(pq)
    gap = abs(v1-v2)
    if gap != 0:
        heapq.heappush(pq, -gap)
    
if len(pq) == 1:
    print(-pq[0])

if len(pq) == 0:
    print(-1)