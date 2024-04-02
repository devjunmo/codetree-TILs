n=int(input())
arr=[
    list(map(int, input().strip().split(' ')))
    for _ in range(n)
]
max_val=0
picks=[]
vis=[False]*n

def simul(lev):
    global max_val
    if lev==n:
        max_val=max(max_val, sum(picks))
        return
    
    for i in range(n):
        if not vis[i]:
            vis[i]=True
            #print(lev)
            #print(i)
            #print()
            picks.append(arr[lev][i])
            simul(lev+1)
            picks.pop()
            vis[i]=False


simul(0)
print(max_val)