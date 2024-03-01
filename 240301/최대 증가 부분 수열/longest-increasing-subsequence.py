n = int(input())
arr = list(map(int, input().strip().split(' ')))

# k인덱스까지 왔을 때 길이가 최대여야 한다
dp = [0] * n
dp[0] = 1

for i in range(1, n):
    # 현 인덱스보다 이전 것들 중
    # 값이 현재보다 작은 애들의
    # dp 값(길이 값) 중 최대 값 + 1을 현재 dp에 넣기
    cur_dp_max = -1
    for j in range(i):
        if arr[j] >= arr[i]:
            continue
        if dp[j] + 1 > cur_dp_max:
            cur_dp_max = dp[j] + 1
    dp[i] = cur_dp_max

print(max(dp))