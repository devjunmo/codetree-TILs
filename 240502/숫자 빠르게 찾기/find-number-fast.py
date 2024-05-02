import bisect

n, m = tuple(map(int, input().split(' ')))
arr = list(map(int, input().strip().split(' ')))

for i in range(m):
    cur_m = int(input())
    idx = bisect.bisect_left(arr, cur_m)
    if arr[idx] == cur_m:
        print(idx+1)
    else:
        print(-1)