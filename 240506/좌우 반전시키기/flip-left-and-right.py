n = int(input().strip())
arr = list(map(int, input().strip().split(' ')))

cnt = 0

def flip(idx):
    if arr[idx] == 1:
        arr[idx] = 0
    else:
        arr[idx] = 1

for i in range(n-1):
    # 현재 자리가 0이면 다음 위치를 누른다
    # 누르면 전중후 반전
    if arr[i] == 0:
        cnt += 1
        for j in range(i, i+3):
            if j < n:
                flip(j)
    # print(arr)

if arr[-1] == 0:
    print(-1)
else:
    print(cnt)