n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip().split(' '))))

dp = []
for _  in range(n):
    dp.append([0]*n)

dp[0][0] = arr[0][0]

# 초기값 채우기
for i in range(1, n):
    dp[0][i] = dp[0][i-1] + arr[0][i]

for i in range(1, n):
    dp[i][0] = dp[i-1][0] + arr[i][0]

# dp 채우기
# 위쪽 왼쪽 
res = -1
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j]+arr[i][j], dp[i][j-1]+arr[i][j])
        res = max(res, dp[i][j])

if res == -1:
    print(dp[0][0])

else:
    print(res)