n,t = list(map(int,input().split()))

lst21 = list(map(int,input().split()))

lst22 = list(map(int,input().split()))

#for i in range(len(lst2)-1,-1,-1):
#    lst1.append(lst2[i])

#print(lst1)
lst1=lst21+lst22

for i in range(t):
    tmp=-1
    tmp=lst1[-1]
    for j in range(len(lst1)-1,0,-1):
        lst1[j]=lst1[j-1]
    lst1[0]=tmp

print(*lst1[0:n])
print(*lst1[n:2*n])