import sys

n = int(input())

seg = [
    tuple(map(int, input().strip().split(' ')))
    for _ in range(n)
]

points = []

for x1, x2 in seg:
    points.append((x1, 1))
    points.append((x2, -1))

points.sort()

max_val = -sys.maxsize
cur_val = 0
for p in points:
    cur_val += p[1]
    max_val = max(cur_val, max_val)

print(max_val)