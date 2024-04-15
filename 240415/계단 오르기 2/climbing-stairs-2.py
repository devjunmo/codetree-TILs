def max_coins(n, coins):
    # dp[i][j] : i번째 계단에 도달했을 때, 1계단씩 오른 횟수가 j번일 때의 최대 동전 수
    dp = [[-float('inf')] * 4 for _ in range(n+1)]
    dp[0][0] = 0  # 시작점, 동전은 없음
    dp[1][1] = coins[0]  # 첫 번째 계단은 오직 1계단 오르기로만 도달 가능
    
    for i in range(2, n+1):
        for j in range(4):
            # 1계단 오르기 (이전 계단에서)
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + coins[i-1])
            # 2계단 오르기 (두 계단 전에서)
            if i >= 2:
                dp[i][j] = max(dp[i][j], dp[i-2][j] + coins[i-1])
    
    # print(*dp, sep='\n')
    
    # 최종 도달 가능한 최대 동전 수 찾기
    max_coins = -float('inf')
    for j in range(4):
        max_coins = max(max_coins, dp[n][j])
    
    return max_coins

# 예제 입력
n = int(input().strip())
coins = list(map(int, input().strip().split()))

# 결과 출력
print(max_coins(n, coins))