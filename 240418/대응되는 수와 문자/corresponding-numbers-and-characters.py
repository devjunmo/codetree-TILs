n, m = tuple(map(int, input().strip().split(' ')))

d = dict()

for i in range(1, n+1):
    v = input()
    d[str(i)]=v
    d[v]=i

# print(d)

for i in range(m):
    k = input()
    print(d[k])