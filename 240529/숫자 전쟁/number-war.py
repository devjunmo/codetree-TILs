n = int(input())
a = [0]+list(map(int, input().split()))
b = [0]+list(map(int, input().split()))

# dp[i][j] = 첫번째 플레이어가 i번째 카드까지, 두번째 플레이어가 j번째 카드까지 버렸을 때 얻을 수 있는 최대 점수
dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
dp[0][0] = 0

for i in range(n):
    for j in range(n):
        # 카드 대결 - a < b
        if a[i + 1] < b[j + 1]:
            # a 카드 버리고 점수 올린다
            dp[i+1][j] = max(dp[i+1][j], dp[i][j])

        # 카드 대결 - a > b
        if a[i + 1] > b[j + 1]:
            # b카드 버리고 점수 올린다 
            dp[i][j+1] = max(dp[i][j+1], dp[i][j]+b[j+1])
        
        # 카드 버리기
        dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])

ans = 0
for i in range(n+1):
    for j in range(n+1):
        ans = max(ans, dp[i][j])

print(ans)