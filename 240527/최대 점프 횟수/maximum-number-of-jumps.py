"""
dp 값: 현재 포인트까지 오는데 점프 횟수
dp 현재값을 채우기 위해 ..
하나전, 두개전, ... 첫번째 까지 본다 (n^2)
숫자가 현재 포인트로 올 수 있는 숫자라면 해당 숫자 dp + 1 값과 현재 dp값 중 큰걸 넣어준다 
"""

import sys

n = int(input())
arr = list(map(int, input().strip().split(' ')))
dp = [0] * (n)

if n == 1:
    print(0)
    sys.exit(0)

for i in range(1, n):
    for j in range(i):
        if arr[j] != 0 and arr[j] + j >= i and dp[i] < dp[j] + 1:
            if j == 0 or dp[j] != 0:
                dp[i] = dp[j] + 1

print(max(dp))
# print(dp)