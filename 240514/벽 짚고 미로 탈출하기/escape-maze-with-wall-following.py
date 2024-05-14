"""
5
1 1
.....
#####
.....
.....
.....

"""
n = int(input().strip())
x, y = tuple(map(int, input().strip().split(' ')))
x-=1
y-=1

mv_cnt = 0

# 시계: 우하좌상
# 반시계: 우상좌하
# 시계일때는 정방향, 반시계일때는 역방향 순회
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
cur_dir = 0 # 0이면 우

map_arr = [
    list(input().strip())
    for _ in range(n)
]


# 시계: 1, 반시계: -1
def get_nxt_dir(cd, rot):
    if rot == 1:
        cd += 1
        if cd == 4:
            cd = 0
    elif rot == -1:
        cd -= 1
        if cd == -1:
            cd = 3
    return cd


# 시계: 1, 반시계: -1
def change_dir(rot):
    global cur_dir
    
    nxt_dir = get_nxt_dir(cur_dir, rot)
    cur_dir = nxt_dir


# 현재 방향 갈 수 있는지 확인
# 오른쪽에 벽이 있어야 움직이기 가능
def can_go():
    pass


# 현재 격자 & 방향 기준 오른쪽에 벽이 있는지 확인
def is_right_wall():
    nxt_dir = get_nxt_dir(cur_dir, 1)
    nx = x + dx[nxt_dir]
    ny = y + dy[nxt_dir]
    if 0 <= nx < n and 0 <= ny < n and map_arr[nx][ny] == '#':
        return True
    else:
        return False


# 현재 격자 & 방향 기준 앞에 벽이 있는지 확인
def is_front_wall():
    nx = x + dx[cur_dir]
    ny = y + dy[cur_dir]
    if 0 <= nx < n and 0 <= ny < n and map_arr[nx][ny] == '#':
        return True
    else:
        return False


# 방향 계산
## -> 오른쪽에 벽이 있으면서 앞에 벽이 있다면 1 리턴 (반시계로 틀어야 함)
## -> 오른쪽에 벽이 있으면서 앞에 벽이 없다면 2 리턴  (전진)
## -> 오른쪽에 벽이 없으면서 앞에 벽이 있다면 0 리턴 (시계방향으로 틀어야 함)
## -> 오른쪽에 벽이 없으면서 앞에 벽이 없다면 -1 리턴 (움직이지 못함. -1 출력 후 종료)
def calc_dir():
    if is_right_wall():
        if is_front_wall():
            return 1
        else:
            return 2
    else:
        if is_front_wall():
            return 0
        else:
            return -1

# 맵 밖으로 나가면 게임 종료
def is_end():
    if 0 <= x < n and 0 <= y < n:
        return False
    else:
        return True


def move():
    global mv_cnt, x, y
    mv_cnt += 1
    x = x + dx[cur_dir]
    y = y + dy[cur_dir]


def simulate():
    while True:
        # 방향 결정
        res_code = calc_dir()
        if res_code == -1:
            print(-1)
            return
        elif res_code == 1:
            change_dir(-1)
            continue
        elif res_code == 2:
            move()
            if is_end():
                print(mv_cnt)
                return
        elif res_code == 0:
            change_dir(1)
            continue
    
simulate()