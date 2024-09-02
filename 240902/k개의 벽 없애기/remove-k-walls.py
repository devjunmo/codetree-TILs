'''
1. 없앨 벽 조합 케이스 구하기
2. 없애고 -> bfs 돌리고 -> 원복하고 / 도달 거리 체크
'''

from itertools import combinations
from collections import deque

MAX_SIZE=99999999

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, k = tuple(map(int, input().strip().split()))
arr = [
    list(map(int, input().strip().split())) for _ in range(n)
]

src_x, src_y = [int(x)-1 for x in input().strip().split()]
tgt_x, tgt_y = [int(x)-1 for x in input().strip().split()]

wall_pos = []

# 벽 위치 저장
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            wall_pos.append((i, j))

# 벽 위치 조합 구하기
wall_pos_combs = list(combinations(wall_pos, k))

# 벽 위치 조합에 대해
# 1. 벽 지우기
# 2. bfs
# 3. 벽 원복하기

def is_range(x, y, vis):
    if 0<=x<n and 0<=y<n and arr[x][y] != 1 and vis[x][y] == 0:
        return True
    else:
        return False


def bfs():
    dist = [
        [0] * n for _ in range(n)
    ]
    dq = deque([(src_x, src_y)])
    dist[src_x][src_y] = 1 # vis 역할 때문에 1로 함. 최종 dist에서 1 뺀값으로 해야 함
    while dq:
        cx, cy = dq.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if nx == tgt_x and ny == tgt_y:
                return dist[cx][cy]
            if is_range(nx, ny, dist):
                dq.append((nx, ny))
                dist[nx][ny] = dist[cx][cy] + 1

    return -2

min_steps = MAX_SIZE

for wall_pos_cases in wall_pos_combs:
    # 벽 지우기
    for wall_pos in wall_pos_cases:
        wx, wy = wall_pos
        arr[wx][wy] = 0
    
    steps = bfs()
    if steps == -2:
        pass
    else:
        min_steps = min(min_steps, steps)

    # 벽 원복하기
    for wall_pos in wall_pos_cases:
        wx, wy = wall_pos
        arr[wx][wy] = 1

if min_steps == MAX_SIZE:
    print(-1)
else:
    print(min_steps)