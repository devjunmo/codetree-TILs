n = int(input())
points = []
for _ in range(n):
    p = tuple(map(int, input().split(' ')))
    points.append(p)

ld = [0] * n
rd = [0] * n

def calc_dist(p1, p2):
    return abs(p1[0]-p2[0])+abs(p1[1]-p2[1])


# ld 계산
for i in range(1, n):
    ld[i] = ld[i-1] + calc_dist(points[i-1], points[i])

# rd 계산
for i in range(n-2, -1, -1):
    rd[i] = rd[i+1] + calc_dist(points[i], points[i+1])


# 최소거리 계산
# i=skip point
min_val = float('inf')
for i in range(1, n-1):
    dst = ld[i-1]+rd[i+1]+calc_dist(points[i-1], points[i+1])
    min_val = min(min_val, dst)

print(min_val)