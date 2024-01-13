from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

MAX_VAL = 99999999

n, m = tuple(map(int, input().strip().split(' ')))
arr = []
dist_arr = []

for _ in range(n):
    arr.append(list(map(int, input().strip().split(' '))))
    dist_arr.append([MAX_VAL] * m)

def can_go(x, y):
    # 정상범위 & 방문x & 뱀 없는경우
    if 0<=x<n and 0<=y<m and dist_arr[x][y] == MAX_VAL and arr[x][y] == 1:
        return True
    else:
        return False

def push_dq(dq, x, y, nxt_dist):
    # 방문체크 후
    dist_arr[x][y] = nxt_dist
    # 큐에 넣기
    dq.append((x, y))

def bfs():
    dq = deque([(0, 0)])
    dist_arr[0][0] = 0
    while dq:
        cx, cy = dq.popleft()
        curr_dist = dist_arr[cx][cy]
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if can_go(nx, ny):
                push_dq(dq, nx, ny, curr_dist+1)

bfs()

print(dist_arr[n-1][m-1])