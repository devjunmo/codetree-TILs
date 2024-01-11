n,m = tuple(map(int,input().strip().split(' ')))

arr=[]
vis=[False] * (n+1)
ans=-1

for _ in range(n+1):
    arr.append([0]*(n+1))

for _ in range(m):
    a, b = tuple(map(int,input().split(' ')))
    arr[a][b] = 1
    arr[b][a] = 1

def dfs(v):
    global ans
    ans+=1
    vis[v] = True
    for i in range(n+1):
        if arr[v][i]==1 and not vis[i]:
            dfs(i)

dfs(1)
print(ans)