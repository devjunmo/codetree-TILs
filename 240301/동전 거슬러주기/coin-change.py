n, m = tuple(map(int, input().strip().split(" "))) # m = 11
arr = list(map(int, input().strip().split(" "))) # 3 5 7

dp = [0] * (m+1) 

# 금액 i를 거슬러 주기 위한 
for i in range(1, m+1):
    # print(i)
    cur_max_dp_cnt = -1
    for j in arr:
        gap = i-j
        if gap >= 0 and (dp[gap] != 0 or gap == 0):
            cur_max_dp_cnt = max(cur_max_dp_cnt, dp[gap]+1)
            dp[i] = cur_max_dp_cnt
    # print(dp)

print(max(dp))