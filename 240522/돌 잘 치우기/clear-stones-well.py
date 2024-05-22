from itertools import combinations
from collections import deque

n,k,m=tuple(map(int,input().split(' ')))
grid=[
    list(map(int,input().strip().split(' ')))
    for _ in range(n)
]
vis=[
    [False]*n
    for _ in range(n)
]
start_pos=[
    tuple(map(lambda x:int(x)-1,input().strip().split(' ')))
    for _ in range(k)
]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

stone_pos=[]

for i in range(n):
    for j in range(n):
        v = grid[i][j]
        if v == 1:
            stone_pos.append((i,j))

rm_stones_lst=list(combinations(stone_pos,m))

def bfs(cur_map, st_pos):
    global max_v
    steps=0
    dq = deque([])
    sx,sy=st_pos
    vis[sx][sy]=True
    dq.appendleft(st_pos)
    while dq:
        cx,cy=dq.pop()
        for d in range(4):
            nx=cx+dx[d]
            ny=cy+dy[d]
            if is_range(nx,ny) and cur_map[nx][ny]==0 and not vis[nx][ny]:
                dq.appendleft((nx,ny))
                steps+=1
                vis[nx][ny]=True
    
    return steps


def is_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False


def reset_vis():
    for i in range(n):
        for j in range(n):
            vis[i][j]=False


def remove_stone(cur_map, rm_stones):
    for rmst in rm_stones:
        rx,ry=rmst
        cur_map[rx][ry]=0

max_v=-1

for rm_stones in rm_stones_lst:
    cur_map=grid.copy()
    remove_stone(cur_map,rm_stones)
    for st_pos in start_pos:
        v= bfs(cur_map, st_pos)
        max_v=max(max_v,v)
        reset_vis()

print(max_v)