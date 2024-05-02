import bisect

n, m = tuple(map(int, input().split(' ')))
arr = list(map(int, input().strip().split(' ')))

m_qrys = list(map(int, input().strip().split(' ')))

for mq in m_qrys:
    idx = bisect.bisect_left(arr, mq)
    if idx < n and arr[idx] == mq:
        print(idx+1)
    else:
        print(-1)