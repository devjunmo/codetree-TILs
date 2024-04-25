import sys

n,k=tuple(map(int,input().split(' ')))
lst=list(map(int,input().split(' ')))

sum_lst=[0]*n

for i in range(1,n):
    sum_lst[i]=sum_lst[i-1]+lst[i]

max_val=-sys.maxsize

for i in range(n-k):
    max_val=max(max_val,sum_lst[i+k-1]-sum_lst[i]+lst[i])

print(max_val)