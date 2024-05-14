"""
5
1 1
.....
#####
.....
.....
.....


5
2 2
#####
.....
##...
##...
.....


3
1 1
...
#.#
.#.

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

# vis_arr = [
#     [False] * n
#     for _ in range(n)
# ]
# vis_arr[x][y] = True


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
def is_right_wall(cur_dir, x, y):
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
## -> 오른쪽에 벽이 있으면서 앞에 벽이 없고,                           
### -> 이동했을 기준 오른쪽에 벽이 있다면 2 리턴 (단순 전진)
### -> 이동했을 기준 오른쪽에 벽이 없다면 3 리턴 (전진 - 시계 - 전진)
def calc_dir():
    if is_right_wall(cur_dir, x, y):
        if is_front_wall():
            return 1
        else:
            nx = x + dx[cur_dir]
            ny = y + dy[cur_dir]
            if is_right_wall(cur_dir, nx, ny):
                return 2
            else:
                return 3
            

# 맵 밖으로 나가면 게임 종료
def is_end():
    if 0 <= x < n and 0 <= y < n:
        return False
    else:
        return True


def move():
    global mv_cnt, x, y
    mv_cnt += 1
    nx = x + dx[cur_dir]
    ny = y + dy[cur_dir]
    
    # # 방문한곳을 또 간다면 뺑뺑이라서 -1리턴하고 끝내야함
    # if 0<=nx<n and 0<=ny<n and vis_arr[nx][ny]:
    #     return -1
    
    x = nx
    y = ny
    # if 0<=nx<n and 0<=ny<n:
    #     vis_arr[x][y] = True
    
    if is_end():
        print(mv_cnt)
        return 0
    
    return 1
    

def simulate():
    while True:
        if mv_cnt > 100000000:
            print(-1)
            return
        # print(f'cur_dir: {cur_dir}')
        # print(f'x: {x}, y: {y}')
        # 방향 결정
        res_code = calc_dir()
        if res_code == 1:
            change_dir(-1)
            continue
        elif res_code == 2:
            mv_code = move()
            if mv_code == -1:
                 print(-1)
                 return
        elif res_code == 3:
            # 전진
            mv_code = move()
            if mv_code == -1:
                # print(*vis_arr, sep='\n')
                # print(f'mv_cnt: {mv_cnt}')
                # print(f'cur_dir: {cur_dir}')
                # print('ddd')
                print(-1)
                return
            if mv_code == 0:
                return
            # 시계
            change_dir(1)
            
            # 전진
            mv_code = move()
            if mv_code == -1:
                # print(*vis_arr, sep='\n')
                # print(f'mv_cnt: {mv_cnt}')
                # print(f'cur_dir: {cur_dir}')
                # print('ddd')
                print(-1)
                return
            if mv_code == 0:
                return
    
simulate()