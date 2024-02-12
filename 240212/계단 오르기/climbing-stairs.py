n = int(input())

dp = [-1] * 10000

dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 1

# n번째 칸으로 오려면 하나 전을 닿으면 안됨
# 두개전 케이스 + 세개전 케이스

for i in range(5, n+1):
    dp[i] = dp[i-2] + dp[i-3]

print(dp[n]%10007)