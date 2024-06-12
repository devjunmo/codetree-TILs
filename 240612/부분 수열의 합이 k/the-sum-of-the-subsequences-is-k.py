n, k = tuple(map(int, input().strip().split(' ')))
lst = list(map(int, input().strip().split(' ')))
lst = [0] + lst
prefix_sum = [0]*(n+1)

# 누적합 채우기
for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + lst[i]
    
cnt = 0

for i in range(0, n+1):
    for j in range(i, n+1):
        range_sum = prefix_sum[j] - prefix_sum[i]
        if range_sum == k:
            cnt += 1

print(cnt)