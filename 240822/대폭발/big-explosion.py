# 격자의 크기를 나타내는 n과 시간을 나타내는 m, 그리고 초기 폭탄의 위치 r, c
n, m, r, c = tuple(map(int, input().split(' ')))
cur_time = 0
boom_lst=[(r-1, c-1)]

# 상우하좌
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

vis = [
    [False] * n
    for _ in range(n)
]
vis[r-1][c-1] = True


def is_range(x, y):
    if 0<=x<n and 0<=y<n and not vis[x][y]:
        return True
    else:
        return False


def set_vis(pos_lst):
    for pos in pos_lst:
        cx = pos[0]
        cy = pos[1]
        vis[cx][cy] = True


def get_new_pos(time, pos_tup):
    res = []
    move_size = 2**(time-1)
    cx = pos_tup[0]
    cy = pos_tup[1]
    for d in range(4):
        nx = cx + dx[d]
        ny = cy + dy[d]
        if is_range(nx, ny):
            res.append((nx, ny))

    # is_range 인것만 리턴해야 함 
    return res


def append_pos_lst(pos_lst):
    for pos in new_pos_lst:
        boom_lst.append(pos)


while cur_time < m:
    # 시간 1초 흐른다
    cur_time+=1
    # 폭탄이 터진다
    new_pos_lst = []
    for boom_pos in boom_lst:
        new_poses = get_new_pos(cur_time, boom_pos)
        # print(new_pos_lst)
        new_pos_lst += new_poses
        set_vis(new_pos_lst)
    append_pos_lst(new_pos_lst)


print(len(boom_lst))