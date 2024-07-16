import sys
MAX_NUM = sys.maxsize

n = int(input())

def get_num_cnt(mid):
    # 1~mid
    m_cnt = mid//3 + mid//5 - mid//15
    return mid-m_cnt


left = 1
right = MAX_NUM
min_num = MAX_NUM

while left <= right:
    mid = (left + right) // 2
    if get_num_cnt(mid) >= n:
        right = mid -1
        min_num = min(min_num, mid)
    else:
        left = mid + 1

print(min_num)