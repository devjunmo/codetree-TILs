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
    if v in d:
        cnt+=1

print(int(cnt/2))