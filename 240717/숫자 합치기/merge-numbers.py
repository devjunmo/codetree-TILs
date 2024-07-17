import heapq

n=int(input())
lst=list(map(int, input().strip().split(' ')))

heapq.heapify(lst)
#print(lst)

cnt=0

while len(lst)>1:
    a=heapq.heappop(lst)
    b=heapq.heappop(lst)
    s=a+b
    cnt+=s
    heapq.heappush(lst,s)

print(cnt)