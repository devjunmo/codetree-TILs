import sys
from collections import deque

n=int(input())
r1,c1,r2,c2=tuple(map(lambda x:int(x)-1,input().strip().split(' ')))
#print(c2)

dist=[
    [-1]*n
    for _ in range(n)
]

dx=[-2,-1,1,2,2,1,-1,-2]
dy=[1,2,2,1,-1,-2,-2,-1]


def is_range(x,y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False


def bfs():
    dq=deque([(r1,c1)])
    dist[r1][c1]=0
    while dq:
        cx,cy=dq.pop()
        for d in range(8):
            nx=cx+dx[d]
            ny=cy+dy[d]
            if is_range(nx,ny) and dist[nx][ny]==-1:
                cur_dist=dist[cx][cy]
                if nx==r2 and ny==c2:
                    print(cur_dist+1)
                    sys.exit(0)
                dq.appendleft((nx,ny))
                dist[nx][ny]=cur_dist+1
                
if r1 == r2 and c1==c2:
    print(0)
    sys.exit(0)
else:
    bfs()
    
print(-1)