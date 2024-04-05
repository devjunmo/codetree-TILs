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
ans=[
    [0]*n
    for _ in range(n)
]

dx=[-1,0,1,0]
dy=[0,1,0,-1]


def can_go(x,y):
    if 0<=x<n and 0<=y<n and not vis[x][y] and (arr[x][y]==0 or arr[x][y]==3):
        return True
    else:
        return False


def bfs(sx,sy):
    dq=deque([(sx,sy)])
    vis[sx][sy]=False
    cnt=0
    while dq:
        cur_pos=dq.popleft()
        cx=cur_pos[0]
        cy=cur_pos[1]
        for d in range(4):
            nx=cx+dx[d]
            ny=cy+dy[d]
            if can_go(nx,ny):
                dq.append((nx,ny))
                vis[nx][ny]=True
                
    
    if cnt == 0:
        return -1
    else:
        return cnt



for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            #ans[i][j]=-1
            cur_cnt=bfs(i,j)
            ans[i][j]=cur_cnt


for row in arr:
    print(*row)