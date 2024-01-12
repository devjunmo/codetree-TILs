from collections import deque

n, m = tuple(map(int, input().strip().split(' ')))
ans = False

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = []
vis = []

for _ in range(n):
    arr.append(list(map(int, input().strip().split(' '))))
    vis.append([False] * m)

def can_go(x, y):
    # 정상범위면서, arr에 뱀이 없고, 방문 안한곳일때 True
    if 0<=x<n and 0<=y<m and arr[x][y] == 1 and not vis[x][y]:
        return True
    else:
        return False

def is_goal(x, y):
    if x == n-1 and y == m-1:
        return True
    else:
        return False

def bfs(st):
    global ans
    dq = deque([st])
    while dq:
        cx, cy = dq.popleft()
        if is_goal(cx, cy):
            ans = True
            return
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if can_go(nx, ny):
                vis[nx][ny] = True
                dq.append((nx, ny))


vis[0][0] = True
bfs((0,0))

if ans:
    print(1)
else:
    print(0)