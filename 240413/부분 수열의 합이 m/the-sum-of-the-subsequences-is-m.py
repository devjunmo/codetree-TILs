n, m = tuple(map(int, input().strip().split(' ')))
arr = list(map(int, input().strip().split(' ')))

def min_length_subsequence(n, m, arr):
    # 초기에 모든 합의 경우에 대해 무한대로 설정합니다. 
    # 0을 만드는 경우는 0개의 원소가 필요하므로 dp[0] = 0으로 설정
    dp = [float('inf')] * (m + 1)
    dp[0] = 0
    
    # 모든 원소에 대해 반복
    for a in arr:
        # m부터 a까지 거꾸로 반복하면서 dp 배열을 업데이트
        for j in range(m, a - 1, -1):
            if dp[j - a] != float('inf'):  # j-a를 만드는 방법이 존재하는 경우
                dp[j] = min(dp[j], dp[j - a] + 1)
    
    # m을 만드는 최소 길이 수열이 존재하는지 확인하고 결과를 반환
    return dp[m] if dp[m] != float('inf') else -1

print(min_length_subsequence(n, m, arr))  # 예상 출력: 3