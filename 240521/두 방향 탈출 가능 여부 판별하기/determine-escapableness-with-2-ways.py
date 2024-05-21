import sys

n,m=tuple(map(int,input().split(' ')))
grid=[
    list(map(int,input().strip().split(' ')))
    for _ in range(n)
]

#하우
dx=[1,0]
dy=[0,1]

vis=[
    [False] * m
    for _ in range(n)
]

def is_range(x,y):
    if 0<=x<n and 0<=y<m and grid[x][y]==1:
        return True
    else:
        return False


def dfs(x, y):
    if x==(n-1) and y==(m-1):
        print(1)
        sys.exit(0)
    for d in range(2):
        nx=x+dx[d]
        ny=y+dy[d]
        if is_range(nx,ny) and not vis[nx][ny]:
            vis[nx][ny]=True
            dfs(nx,ny)



vis[0][0]=True
dfs(0,0)

print(0)