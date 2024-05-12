import copy

n, m = tuple(map(int, input().strip().split(' ')))

grid = [
    list(map(int, input().strip().split(' ')))
    for _ in range(n)
]

querys = [
    tuple(map(int, input().strip().split(' ')))
    for _ in range(m)
]

dist_matrix = copy.deepcopy(grid)
for i in range(n):
    dist_matrix[i][i] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist_matrix[i][j] = min(dist_matrix[i][j], dist_matrix[i][k] + dist_matrix[k][j])

for i in range(m):
    a, b = querys[i]
    print(dist_matrix[a-1][b-1])