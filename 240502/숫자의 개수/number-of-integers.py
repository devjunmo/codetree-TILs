import bisect

n, m = tuple(map(int, input().split(' ')))
arr = list(map(int, input().strip().split(' ')))

for i in range(m):
    cur_m = int(input())
    idx_l = bisect.bisect_left(arr, cur_m)
    idx_r = bisect.bisect_right(arr, cur_m)
    if idx_l < n and arr[idx_l] == cur_m:
        print(idx_r - idx_l)
    else:
        print(0)