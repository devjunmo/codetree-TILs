n, m = tuple(map(int, input().strip().split(' ')))
lst = []
for _ in range(n):
    lst.append(int(input()))

k_max = min(lst)

left = 1
right = k_max

max_val = -1

while left <= right:
    cur_cnt = 0
    mid = (left + right) // 2
    for comp in lst:
        cur_cnt += comp // mid
    if cur_cnt >= m:
        max_val = max(max_val, mid)
        # 가능한 k값 중 더 큰값을 찾아보기
        left = mid + 1
    else:
        # 더 작은 k값 찾기
        right = mid -1

print(max_val)