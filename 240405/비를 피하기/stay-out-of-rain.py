from collections import deque

n,h,m=tuple(map(int,input().strip().split(' ')))
arr=[
    list(map(int,input().strip().split(' ')))
    for _ in range(n)
]
vis=[
    [False]*n
    for _ in range(n)
]
step=[
    [0]*n
    for _ in range(n)
]

ans=[
    [0]*n
    for _ in range(n)
]

dx=[-1,0,1,0]
dy=[0,1,0,-1]


def can_go(x,y):
    if 0<=x<n and 0<=y<n and not vis[x][y] and not arr[x][y]==1:
        return True
    else:
        return False


def bfs(sx,sy):
    dq=deque([(sx,sy)])
    vis[sx][sy]=True
    while dq:
        cx, cy = dq.popleft()
        for d in range(4):
            nx=cx+dx[d]
            ny=cy+dy[d]
            if can_go(nx,ny):
                dq.append((nx,ny))
                vis[nx][ny]=True
                step[nx][ny] = step[cx][cy]+1
                if arr[nx][ny]==3:
                    return step[nx][ny]
    return -1


def reset():
    for i in range(n):
        for j in range(n):
            step[i][j]=0
            vis[i][j]=False


for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            cur_cnt=bfs(i,j)
            ans[i][j]=cur_cnt
            reset()


for row in ans:
    print(*row)