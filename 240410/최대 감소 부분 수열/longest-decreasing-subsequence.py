# 순서 + 계속 감소

n = int(input())
nums = list(map(int, input().strip().split(' ')))

dp = [
    [0] * n
    for _ in range(n)
]

for j in range(n):
    # 초기값 초기화
    dp[0][j] = 1

# print(*dp, sep='\n')

"""
r: 현재 뽑은 자리
c: 주어진 수열 인덱스
값: 길이

  0 1 2 3 4 5
0 1 1 1 1 1 1
1 x 2 2 2 2 2
2 x x 2 2 3 2
3 x x x 2 3 2
4 x x x x 3 2
5 x x x x x 2

"""

# 현재 자리에 뽑을 수열 인덱스를 보고
# 만약 [i-1][0~j-1] 스캔했을 때 주어진 순열에서 현재 넣을 값 보다 크다면
## dp배열 값 + 1인데, 그 값들 중 최대값을 
# 예상 시간복잡도 n^3

for i in range(1, n):
    for j in range(i, n):
        # j: 수열에서 현재 넣을 값의 인덱스
        # i-1 ~ j-1 nums에 대해 조사
        for k in range(i-1, j):
            # print(f'i: {i}, j: {j}, k: {k}')
            # 이전 자리에 넣은 수열 값보다 작아야 뽑을 수 있다
            if nums[k] > nums[j] and dp[i-1][k] > dp[i][j]:
                # print('dd')
                dp[i][j] = dp[i-1][k] + 1
        # 탐색했는데 해당하는 값이 없다면 이전 길이 그대로 유지
        if dp[i][j] == 0:
            dp[i][j] = dp[i-1][j]


max_val = -1

for i in range(n):
    for j in range(n):
        max_val = max(max_val, dp[i][j])


# print(*dp, sep='\n')

print(max_val)