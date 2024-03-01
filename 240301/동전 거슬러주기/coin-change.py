n, m = tuple(map(int, input().strip().split(" ")))
arr = list(map(int, input().strip().split(" ")))

dp = [0] * (m+1)
dp[1] = 1

for i in range(2, m+1):
    cur_max_dp_cnt = -1
    for j in arr:
        gap = j-i
        if gap >= 0:
            cur_max_dp_cnt = max(cur_max_dp_cnt, dp[gap]+1)
            dp[i] = cur_max_dp_cnt
    # print(dp)=

print(max(dp))