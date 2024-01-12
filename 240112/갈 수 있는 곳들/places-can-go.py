from collections import deque

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, k = tuple(map(int, input().strip().split(' ')))
arr = []
vis = []
st_lst = []
ans = 0

for _ in range(n):
    arr.append(list(map(int, input().strip().split(' '))))
    vis.append([False]*n)

for _ in range(k):
    kx, ky = tuple(map(int, input().strip().split(' ')))
    st_lst.append((kx-1, ky-1))


def can_go(x, y):
    # 정상범위면서 갈수있는곳이면서 방문안한곳일때 간다
    if 0<=x<n and 0<=y<n and arr[x][y] == 0 and not vis[x][y]:
        return True
    else:
        return False


def q_push(dq, x, y):
    # 큐에 푸쉬 후 방문 체크
    dq.append((x,y))
    vis[x][y] = True


def bfs():
    global ans
    dq = deque([])
    for st in st_lst:
        sx, sy = st
        vis[sx][sy] = True
        dq.append(st)
        ans += 1
    while dq:
        cx, cy = dq.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if can_go(nx, ny):
                q_push(dq, nx, ny)
                ans+=1

bfs()
print(ans)