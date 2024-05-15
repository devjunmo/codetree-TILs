t = int(input().strip())

dir_idx = {"U": 0, "D": 1, "L": 2, "R": 3}

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def is_range(x, y):
    if 0<=x<n and 0<=y<n:
        return True
    else:
        return False


def get_flip_dir(d_idx):
    if d_idx == 0:
        return 1
    elif d_idx == 1:
        return 0
    elif d_idx == 2:
        return 3
    elif d_idx == 3:
        return 2


def set_next_pos(x, y, d):
    if (x, y) in next_pos_dict:
        # 만약 next pos에 중복이 있다면 구슬이 부딪힌거니까 제거한다
        next_pos_dict.pop((x, y))
    else:
        # 중복이 없다면 next pos dict에 넣는다
        next_pos_dict[(x, y)] = d


def simulate():
    global pos_dict
    for pos, d in pos_dict.items():
        x, y = pos
        nx = x + dx[d]
        ny = y + dy[d]
        if is_range(nx, ny):
            set_next_pos(nx, ny, d)
        else:
            # 정상 범위가 아니라면 방향을 바꾼다
            flip_d = get_flip_dir(d)
            set_next_pos(x, y, flip_d)
    # 다 돌았으면 next pos dict을 pos dict에 카피한다
    pos_dict = next_pos_dict.copy()
    next_pos_dict.clear()

for _ in range(t):
    pos_dict = {}
    next_pos_dict = {}
    sec = 0

    n, m = tuple(map(int, input().strip().split(' ')))
    for _ in range(m):
        x, y, d = input().strip().split(' ')
        x = int(x)
        y = int(y)
        pos_dict[(x-1,y-1)] = dir_idx[d]

    while sec < 2*n:
        # print(pos_dict)
        simulate()
        sec += 1

    print(len(pos_dict))