n=int(input())
arr=[
    list(map(int, input().strip().split(' ')))
    for _ in range(n)
]

vis=[
    [False]*n
    for _ in range(n)
]

c_cnt=0
p_cnt=0
ans=[]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(cx, cy):
    global p_cnt
    #can_move=False
    for d in range(4):
        nx=cx+dx[d]
        ny=cy+dy[d]
        if 0<=nx<n and 0<=ny<n and not vis[nx][ny] and arr[nx][ny]==1:
            #can_move=True
            vis[nx][ny]=True
            p_cnt+=1
            dfs(nx,ny)
    
    #if not can_move:
    #    ans.append(cnt)
    #    return


for i in range(n):
    for j in range(n):
        if not vis[i][j] and arr[i][j] == 1:
            c_cnt+=1
            dfs(i, j)
            ans.append(p_cnt)
            p_cnt=0

ans=sorted(ans)
print(c_cnt)
for a in ans:
    print(a)