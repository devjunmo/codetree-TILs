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


# 배열을 돌며 중력을 적용시키기
tr_lst = [] # 중력 적용 배열, 90도 시계방향으로 돌아있음
for j in range(n):
    tmp_lst = [0] * n
    append_idx = 0
    for i in range(n-1, -1, -1):
        if arr[i][j] != 0:
            tmp_lst[append_idx] = arr[i][j]
            append_idx += 1
    tr_lst.append(tmp_lst)


# 반시계 90도 회전
def rotate_90_counter_clockwise(matrix):
    # 행렬 전치
    transposed = list(zip(*matrix))

    # 전치된 행렬의 각 열을 뒤집기
    rotated = [list(row) for row in transposed][::-1]

    return rotated


rotated_matrix = rotate_90_counter_clockwise(tr_lst)

for row in rotated_matrix:
    print(*row)