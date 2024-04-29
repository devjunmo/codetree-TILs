n = int(input())
seg = [
    tuple(map(int, input().strip().split(' ')))
    for _ in range(n)
]

points = []

for i, (x1, x2) in enumerate(seg):
    points.append((x1, +1, i))
    points.append((x2, -1, i))

points.sort()

buff = set()

ans = 0

for x, v, idx in points:
    if v == 1:
        if not buff:
            ans += 1
        buff.add(idx)
    else:
        buff.remove(idx)

print(ans)