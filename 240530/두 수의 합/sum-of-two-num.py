n,k=tuple(map(int,input().strip().split(' ')))
arr=list(map(int,input().strip().split(' ')))

d={}
for comp in arr:
    if comp in d:
        continue
    d[comp]=True

cnt=0
for comp in arr:
    v=k-comp
    if v in d and d[v] and comp in d and d[comp]:
        cnt+=1
        d[comp]=False
        d[v]=False

print(int(cnt))