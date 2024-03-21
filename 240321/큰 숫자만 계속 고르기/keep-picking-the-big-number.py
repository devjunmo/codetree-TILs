import heapq

n, m = tuple(map(int, input().strip().split(' ')))
input_lst = list(map(int, input().strip().split(' ')))
input_lst = [x * -1 for x in input_lst]

heapq.heapify(input_lst)

for _ in range(m):
    v = heapq.heappop(input_lst)
    heapq.heappush(input_lst, v+1)

print(-1 * heapq.heappop(input_lst))