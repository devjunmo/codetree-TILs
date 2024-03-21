import heapq

n, m = tuple(map(int, input().strip().split(' ')))
pq = []

# 최초 pq 구성 (거리, x, y)
for _ in range(n):
    cx, cy = tuple(map(int, input().strip().split(' ')))
    heapq.heappush(pq, [cx+cy, cx, cy])

# m번 돌며 가장 가까운 점을 잡아 2씩 더한 후 다시 pq에 넣는다 
for _ in range(m):
    lst = heapq.heappop(pq)
    lst[0] = lst[0] + 4
    lst[1] = lst[1] + 2
    lst[2] = lst[2] + 2
    heapq.heappush(pq, lst)

min_lst = heapq.heappop(pq)
print(f'{min_lst[1]} {min_lst[2]}')