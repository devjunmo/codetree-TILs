from collections import deque

# 1. 인접 체크 -> 본인보다 작은곳으로 bfs 진행 가능
# 2. bfs 진행 -> 갈 수 있는곳을 돌며 최대 값을 찾기
# 3. 다시 n제곱 순회하며 찾은 최대값에 대해 좌표 저장하기 -> 행으로 오름차순 정렬 && 열로 오름차순 정렬 -> 첫번째 요소가 갈 곳 


# 1,2,3을 k번 반복
# 턴마다 vis reset 필요 
# k번 다 하지못하고 움직일 수 없으면 종료 -> -1리턴 등으로 break     


n, k = tuple(map(int, input().strip().split(' ')))
arr = [
    list(map(int, input().strip().split(' ')))
    for _ in range(n)
]
r, c = tuple(map(int, input().strip().split(' ')))
r -= 1
c -= 1
vis=[
    [False]*n
    for _ in range(n)
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def can_go(x, y, st_val):
    if 0<=x<n and 0<=y<n and arr[x][y] < st_val and vis[x][y] == False:
        return True
    else:
        return False


def reset():
    for i in range(n):
        for j in range(n):
            vis[i][j] = False


def bfs(sx, sy):
    dq = deque([(sx, sy)])
    vis[sx][sy] = True
    start_val = arr[sx][sy]
    # print(f'>> start: {sx} {sy} / startVal: {start_val}')
    max_val = -1
    while dq:
        cx, cy = dq.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if can_go(nx, ny, start_val):
                max_val = max(max_val, arr[nx][ny])
                vis[nx][ny] = True
                dq.append((nx, ny))
    
    if max_val != -1:
        # print(f'max_val: {max_val} // {coor_dict[max_val][0]}')
        # maxval의 최우선 좌표 get 후 리턴
        return coor_dict[max_val][0]

    else:
        # 갈곳 없으면 -1 리턴
        return (-1,-1)


# 전체 arr에 대해 key: arr값, val: 좌표 리스트 딕셔너리 생성 및 val 정렬
coor_dict = {}
for i, row in enumerate(arr):
    for j, value in enumerate(row):
        if value not in coor_dict:
            coor_dict[value] = []
        coor_dict[value].append((i, j))

for key in coor_dict:
    coor_dict[key] = sorted(coor_dict[key], key=lambda x: (x[0], x[1]))

# print(coor_dict)

for _ in range(k):
    nr, nc = bfs(r, c)
    # print(f'>>> {nr} {nc}')
    reset()
    if nr == -1:
        # print('dd')
        break
    else:
        r = nr
        c = nc


print(*[r+1, c+1])