import math

s = int(input())
s_mx = int(math.sqrt(s))


left = 1
right = s_mx
max_num = s_mx+1

while left <= right:
    # 가운데 위치 선택
    mid = (left + right) // 2 
    print(mid)
    # 1~mid 까지의 합이 s 이하 라면, mid보다 더 오른쪽에서 큰 값을 찾는다 
    if mid * (mid + 1) // 2 <= s:
        left = mid + 1
        max_num = max(max_num, mid)
    else:
        # s보다 크다면 mid 보다 더 왼쪽에서 찾아야 함
        right = mid-1

print(max_num)