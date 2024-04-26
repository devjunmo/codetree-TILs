import heapq

n, q = tuple(map(int, input().split(' ')))
lst = list(map(int, input().split(' ')))

heapq.heapify(lst)

d = {}
cnt = 1

while lst:
    v = heapq.heappop(lst)
    d[v] = cnt
    cnt += 1

for _ in range(q):
    a, b = tuple(map(int, input().strip().split(' ')))
    ca = d[a]
    cb = d[b]
    # print(f'ca: {ca}, cb: {cb}')
    print(cb-ca+1)