n, q = tuple(map(int, input().strip().split(' ')))
points = []

for _ in range(n):
    points.append(tuple(map(int, input().strip().split(' '))))

# x1, y1, x2, y2
qrys = []
for _ in range(q):
    qrys.append(tuple(map(int, input().strip().split(' '))))


def is_range(point, qry):
    x1, y1, x2, y2 = qry
    x, y = point
    if x1 <= x <= x2 and y1 <= y <= y2:
        return True
    return False


res = [0] * q
idx = 0
for qry in qrys:
    cnt = 0
    for point in points:
        if is_range(point, qry):
            cnt += 1
    res[idx] = cnt
    idx += 1

for r in res:
    print(r)