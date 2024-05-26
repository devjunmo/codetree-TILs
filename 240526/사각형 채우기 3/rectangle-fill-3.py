MOD = 1000000007

n = int(input())
dp = [0] * (n + 1)
dp[0] = 1 # 아무것도 놓지 않음
dp[1] = 2

# dp 채우기 
for i in range(2, n+1):
    # 하나전, 두개전 동등 상황 처리
    dp[i] = (dp[i-1] * 2 + dp[i-2] * 3) % MOD
    # 세개 전부터 끝까지 동등 상황 처리
    for j in range(i-3, -1, -1):
        # dp 합연산 지속
        dp[i] = (dp[i] + dp[j] * 2) % MOD

print(dp[n])