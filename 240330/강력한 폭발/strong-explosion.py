n = int(input().strip())
arr = [
    list(map(int, input().strip().split(' ')))
    for _ in range(n)
]

# 터진 맵
boom_map = [
    [0] * n
    for _ in range(n)
]

# 방향 리스트
b1x = [-1, -2, 1, 2]
b1y = [0, 0, 0, 0]
b2x = [-1, 0, 1, 0]
b2y = [0, 1, 0, -1]
b3x = [-1, 1, 1, -1]
b3y = [1, 1, -1, -1]

max_val = -1

m = 0 # 폭탄 놓을 자리 수 
pos_dict = dict()

cur_booms = [0] # 현재 선택 폭탄 저장 (인덱스 1부터)

# 배열 순회 해서 1인 위치를 딕셔너리에 저장 
## key: 1, 2, 3 ~ 10  / value: (x, y)
for i in range(n):
    for j in range(n):
        v = arr[i][j]
        if v != 0:
            m += 1
            pos_dict[m] = (i, j)


def boom1(boom_pos):
    boom_map[boom_pos[0]][boom_pos[1]] = 1
    for d in range(4):
        nx = boom_pos[0] + b1x[d]
        ny = boom_pos[1] + b1y[d]
        if 0<=nx<n and 0<=ny<n:
            boom_map[nx][ny] = 1


def boom2(boom_pos):
    boom_map[boom_pos[0]][boom_pos[1]] = 1
    for d in range(4):
        nx = boom_pos[0] + b2x[d]
        ny = boom_pos[1] + b2y[d]
        if 0<=nx<n and 0<=ny<n:
            boom_map[nx][ny] = 1


def boom3(boom_pos):
    boom_map[boom_pos[0]][boom_pos[1]] = 1
    for d in range(4):
        nx = boom_pos[0] + b3x[d]
        ny = boom_pos[1] + b3y[d]
        if 0<=nx<n and 0<=ny<n:
            boom_map[nx][ny] = 1


def map_reset():
    for i in range(n):
        for j in range(n):
            boom_map[i][j] = 0


def exec_boom():
    global max_val
    # 터뜨리기
    for i in range(1, m+1):
        boom_pos = pos_dict[i]
        boom_num = cur_booms[i]
        if boom_num == 1:
            boom1(boom_pos)
        elif boom_num == 2:
            boom2(boom_pos)
        elif boom_num == 3:
            boom3(boom_pos)

    # print(*boom_map, sep='\n')
    # print(' ')

    # 초토화 된곳 카운팅
    destr_cnt = 0
    for i in range(n):
        for j in range(n):
            if boom_map[i][j] != 0:
                destr_cnt += 1

    # print(destr_cnt)
    max_val = max(max_val, destr_cnt)
    map_reset()


# 6만 * 400 = 2400만 * 5 = 
def simulate(cnt):
    if cnt == m:
        exec_boom()
        return

    # 폭탄의 종류 1 ~ 3 
    for boom in range(1, 4):
        cur_booms.append(boom)
        simulate(cnt+1)
        cur_booms.pop()


simulate(0)
print(max_val)