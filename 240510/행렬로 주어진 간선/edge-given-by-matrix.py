n = int(input())

adj_lst = [
    [0]+list(map(int, input().strip().split(' ')))
    for _ in range(n)
]
adj_lst = [[0] * (n+1)] + adj_lst
# print(*adj_lst, sep='\n')

dist = [
    [0] * (n+1)
    for _ in range(n+1)
]

# 원래 갈수있는곳은 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if adj_lst[i][j] == 1:
            dist[i][j] = 1

# 제자리는 1
for i in range(1, n+1):
    dist[i][i] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dist[i][k] and dist[k][j]:
                dist[i][j] = 1

for i in range(1, n+1):
    buff = []
    for j in range(1, n+1):
        buff.append(dist[i][j])
    print(*buff)