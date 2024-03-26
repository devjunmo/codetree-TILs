"""
4
1 2 4 3
3 2 2 3
3 1 6 2
4 5 4 4
2 3
"""

n = int(input())
arr = [
    list(map(int, input().strip().split(' ')))
    for _ in range(n)
]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

r, c = tuple(map(int, input().strip().split(' ')))
r -= 1
c -= 1

def check_range(i, j):
    if 0 <= i < n and 0 <= j < n:
        return True
    else:
        return False

# r, c 포인트에 대해 폭탄 터뜨리기
## 숫자만큼 반복 돌며 정상 배열 범위일 때 숫자를 0으로 만든다
boom_cnt = arr[r][c]
for i in range(boom_cnt):
    # 4방 탐색
    for d in range(4):
        nx = r + dx[d] * i
        ny = c + dy[d] * i
        if check_range(nx, ny):
            arr[nx][ny] = 0


# i-1 ~ 0 행까지에 대해 한칸씩 내리기 진행
## 만약 올라가는데 두번 연속 0이면 break
def grav(i, j):
    cur_i = i
    while cur_i > 0:
        up_i = cur_i - 1
        arr[cur_i][j] = arr[up_i][j]
        arr[up_i][j] = 0
        cur_i = up_i
        

# 배열을 돌며 중력을 적용시키기
## 마지막행부터 돌면서, 0값을 발견하면, 중력 적용
for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        if arr[i][j] == 0:
            grav(i, j)

for i in range(n):
    print(*arr[i])