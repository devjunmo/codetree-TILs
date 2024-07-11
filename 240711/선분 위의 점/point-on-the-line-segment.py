import bisect

n, m = tuple(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))
arr.sort()
ans = []
for _ in range(m):
    a, b = tuple(map(int, input().strip().split()))
    lv = bisect.bisect_left(arr, a)
    rv = bisect.bisect_right(arr, b)
    ans.append(rv-lv)

for a in ans:
    print(a)