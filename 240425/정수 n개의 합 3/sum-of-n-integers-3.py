n, k = map(int, input().split())

# 원본 배열을 입력받아 초기화
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# 2차원 누적 합 배열
sum_grid = [[0] * (n + 1) for _ in range(n + 1)]

# 누적 합 계산
for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum_grid[i][j] = grid[i-1][j-1] + sum_grid[i-1][j] + sum_grid[i][j-1] - sum_grid[i-1][j-1]

# 최대 k*k 구역의 합을 찾음
max_sum = 0
for i in range(k, n + 1):
    for j in range(k, n + 1):
        current_sum = sum_grid[i][j] - sum_grid[i-k][j] - sum_grid[i][j-k] + sum_grid[i-k][j-k]
        max_sum = max(max_sum, current_sum)

print(max_sum)