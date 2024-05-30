from itertools import combinations

n,k=tuple(map(int,input().strip().split(' ')))
arr=list(map(int,input().strip().split(' ')))

d={}
vis=[False]*(n+10)

for i in range(len(arr)):
    if arr[i] in d:
        d[arr[i]].append(i)
        continue
    d[arr[i]]=[i]
#print(d)
cnt=0
for comp in arr:
    if vis[d[comp][0]]:
        continue
    v=k-comp
    if comp==v:
        #cnt+=len(list(combinations(d[comp],2)))
        clen=len(d[comp])
        cnt+=int((clen*(clen-1)/2))
        for idx in d[comp]:
            vis[idx]=True
        continue
    
    if comp in d and v in d:
        cnt+=(len(d[comp])*len(d[v]))
        for idx in d[comp]:
            vis[idx]=True
        for idx in d[v]:
            vis[idx]=True

print(int(cnt))