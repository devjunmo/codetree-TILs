n, r, c = list(map(int, input().split(' ')))
r -= 1
c -= 1

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

arr = []
res = []

for _ in range(n):
    arr.append(list(map(int, input().strip().split(' '))))

res.append(arr[r][c])

break_flag = False
while not break_flag:
    # 상하좌우 순서대로 탐색하며 현재 위치보다 크다면 위치 갱신 및 숫자 저장 후 continue
    for d in range(4):
        nx = r + dx[d]
        ny = c + dy[d]

        # next가 정상범위면서 현재 위치보다 크다면
        if 0<=nx<=n-1 and 0<=ny<=n-1 and arr[nx][ny] > arr[r][c]:
            # 위치 갱신
            r = nx
            c = ny
            # 숫자 저장
            res.append(arr[nx][ny])
            break
        
        if d == 3:
            # 사방향의 요소들이 현재 위치보다 큰게 없다면 break
            break_flag = True
    

print(*res)