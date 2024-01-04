"""
4 3 1
1 2 2 3
3 5 10 15
3 8 11 2
4 5 4 4
2 2
3 4
4 2

"""
import copy

n, m, t = tuple(map(int, input().strip().split(' ')))

arr = []
vis = []
vis_nxt = []

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for _ in range(n):
    arr.append(list(map(int, input().strip().split(' '))))
    vis.append([0]*n)

for _ in range(m):
    r, c = list(map(int, input().strip().split(' ')))
    vis[r-1][c-1] = 1

# vis_nxt 초기화
def reset_vis_nxt():
    global vis_nxt
    vis_nxt = []
    for _ in range(n):
        vis_nxt.append([0]*n)

reset_vis_nxt()

# vis 배열 돌면서 1이면 해당 포인트에서 상하좌우 체크 및 더 큰쪽으로 이동
def search_object_and_move():
    for i in range(n):
        for j in range(n):
            if vis[i][j] == 1:
                check_and_move(i, j)

# 상하좌우 체크 후 만약 이동한다면 next_vis에 +1
def check_and_move(i, j):
    max_val = -999
    max_r = -10
    max_c = -10
    for d in range(4):
        nx = dx[d] + i
        ny = dy[d] + j
        # 정상범위이면서 현재 값보다 크고 최대값일때 해당 위치 기록
        if 0<=nx<n and 0<=ny<n and arr[nx][ny] > arr[i][j] and arr[nx][ny] > max_val:
            max_val =arr[nx][ny]
            max_r = nx
            max_c = ny
    if max_r != -10 and max_c != -10:
        vis_nxt[max_r][max_c] += 1
            

# next_vis를 돌면서 2 이상인 요소들을 0으로 바꾸고 vis에 copy
def copy_vis_and_reset_nxt_vis():
    for i in range(n):
        for j in range(n):
            if vis_nxt[i][j] >= 2:
                vis_nxt[i][j] = 0
    
    vis = copy.deepcopy(vis_nxt)
    reset_vis_nxt()

for _ in range(t):
    search_object_and_move()
    copy_vis_and_reset_nxt_vis()

res = 0

for i in range(n):
    for j in range(n):
        if vis[i][j] == 1:
            res += 1

print(res)