from bisect import bisect_left, bisect_right

n, m = tuple(map(int, input().strip().split(' ')))

points = [
    tuple(map(int, input().strip().split(' ')))
    for _ in range(n)
]

targets = [
    tuple(map(int, input().strip().split(' ')))
    for _ in range(m)
]

# 1. points 정렬
points.sort(key=lambda x:(x[0], x[1]))
key_lst = [x[0] for x in points]
# print(key_lst)
# print(bisect_left(key_lst, 3))
# print(bisect_right(key_lst, 6))

for target in targets:
    x1, y1 = target
    x0_idx = bisect_left(key_lst, x1)
    if points[x0_idx][0] == x1:
        print(f'{points[x0_idx][0]} {points[x0_idx][1]}')
        continue
    x_idx = bisect_left(key_lst, x1+1)
    if points[x_idx][0] >= x1:
        print(f'{points[x_idx][0]} {points[x_idx][1]}')
        # print(f'ddd: {x_idx}')
        continue
    if x_idx >= n:
        print(*[-1, -1])
        continue
    else:
        print(*[-1, -1])