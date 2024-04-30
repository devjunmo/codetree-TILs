"""
7: [1]
3: [2, 5]
4: [3, 6]
2: [4]

"""

n, k = tuple(map(int, input().split(' ')))

d = {}

for i in range(1, n+1):
    v = int(input())
    if v in d:
        d[v].append(i)
    else:
        d[v] = [i]

max_boom_num = -1

for k, v in d.items():
    v.sort()
    for i in range(len(v)-1):
        gap = abs(v[i]-v[i+1])
        if gap <= k:
            max_boom_num = max(max_boom_num, k)

print(max_boom_num)