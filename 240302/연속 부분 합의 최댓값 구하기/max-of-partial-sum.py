import sys
INT_MIN = -sys.maxsize

n = int(input())
arr = list(map(int, input().strip().split(' ')))
dp = [INT_MIN] * (n+1)
dp[0] = 4

for i in range(1, n):
    dp[i] = max((dp[i-1] + arr[i]), arr[i])

print(max(dp))