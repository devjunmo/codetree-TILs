import sys

n, m = tuple(map(int, input().strip().split(' ')))
dist = [
    [sys.maxsize]*(n+1)
    for _ in range(n+1)
]

# 자신은 0으로 초기화
for i in range(1, n+1):
    dist[i][i] = 0

# 거리배열 초기화
for _ in range(m):
    x, y, z = tuple(map(int, input().strip().split(' ')))
    dist[x][y] = min(z, dist[x][y])


# 모든 정점을 거쳐보기
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


# 출력
for i in range(1, n+1):
    buff = []
    for j in range(1, n+1):
        if dist[i][j] == sys.maxsize:
            buff.append(-1)
        else:
            buff.append(dist[i][j])
    print(*buff)