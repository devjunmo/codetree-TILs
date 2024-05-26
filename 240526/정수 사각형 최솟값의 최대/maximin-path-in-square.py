n = int(input())
grid = [
    list(map(int, input().strip().split(' ')))
    for _ in range(n)
]
dp = [
    [0] * n
    for _ in range(n)
]

dp[0][0] = grid[0][0]

# 우측으로만 갈 때 채우기
for i in range(1, n):
    dp[0][i] = min(dp[0][i-1], grid[0][i])

# 아래로만 갈 때 채우기 
for i in range(1, n):
    dp[i][0] = min(dp[i-1][0], grid[i][0])

# 현재 포인트에 대해 직전 경로 dp 중 최대값을 적용하기
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(min(grid[i][j], dp[i-1][j]), min(grid[i][j], dp[i][j-1]))

print(dp[n-1][n-1])