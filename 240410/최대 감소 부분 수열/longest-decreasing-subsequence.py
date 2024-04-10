n = int(input())
nums = list(map(int, input().split()))

# dp[i]는 nums[i]를 마지막으로 하는 가장 긴 감소하는 부분 수열의 길이를 저장
dp = [1] * n  # 각 요소는 적어도 자기 자신을 포함하는 부분 수열이므로 1로 초기화

# 모든 가능한 부분 수열에 대해 검사하여 dp 배열을 업데이트
for i in range(1, n):
    for j in range(0, i):
        if nums[j] > nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)
            
max_length = max(dp)

print(max_length)