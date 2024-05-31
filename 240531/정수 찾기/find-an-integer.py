n=int(input())
a=set(map(int,input().strip().split()))
m=int(input())
b=list(map(int,input().strip().split()))
for bc in b:
    if bc in a:
        print(1)
    else:
        print(0)