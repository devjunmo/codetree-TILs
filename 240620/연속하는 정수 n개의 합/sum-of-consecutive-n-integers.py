n, m = map(int, input().strip().split())
lst = list(map(int, input().strip().split()))

i, j = 0, 0
cur_sum = 0
ans = 0

while j < n:
    cur_sum += lst[j]
    j += 1
    
    while cur_sum > m and i < j:
        cur_sum -= lst[i]
        i += 1
    
    if cur_sum == m:
        ans += 1

print(ans)