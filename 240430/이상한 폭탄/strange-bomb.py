n, k = tuple(map(int, input().split(' ')))

d = {}

for i in range(1, n+1):
    v = int(input())
    if v in d:
        d[v].append(i)
    else:
        d[v] = [i]

max_boom_num = -1

for key, val in d.items():
    val.sort()
    for i in range(len(val)-1):
        gap = abs(val[i]-val[i+1])
        if gap <= k:
            # print(f'key: {key} val: {val}')
            max_boom_num = max(max_boom_num, key)

print(max_boom_num)