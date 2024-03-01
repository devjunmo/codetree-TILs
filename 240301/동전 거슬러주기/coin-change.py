n, m = tuple(map(int, input().strip().split(" "))) # m = 10
arr = list(map(int, input().strip().split(" "))) # 1 2 3 4 5 6 7

dp = [0] * (m+1) 

# 금액 i를 거슬러 주기 위한 
for i in range(1, m+1):
    cur_min_dp_cnt = 999999
    for j in arr:
        gap = i-j
        if gap >= 0 and (dp[gap] != 0 or gap == 0):
            cur_min_dp_cnt = min(cur_min_dp_cnt, dp[gap]+1)
            dp[i] = cur_min_dp_cnt

if dp[m] == 0:
    print(-1)
else:
    print(dp[m])