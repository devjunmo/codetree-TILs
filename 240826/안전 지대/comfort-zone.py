from collections import deque

n, m = tuple(map(int, input().strip().split()))
arr = [
    list(map(int, input().strip().split())) for _ in range(n)
]

# 인덱스: 높이 값: 위치 리스트
h_pos = [
    [] for _ in range(101)
]


for i in range(n):
    for j in range(m):
        v = arr[i][j]
        h_pos[v].append((i, j))

max_k = -1
max_k_val = -1

# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def is_range(x, y):
    if 0<=x<n and 0<=y<m:
        return True
    else:
        return False
    

def bfs(x, y, vis):
    dq = deque([(x, y)])
    vis[x][y] = True
    while dq:
        cx, cy = dq.popleft()
        for d in range(4):
            nx = cx + dx[d]
            ny = cy + dy[d]
            if is_range(nx, ny) and not vis[nx][ny]:
                dq.append((nx, ny))
                vis[nx][ny] = True


for k in range(1, 101):
    vis = [
        [False] * m for _ in range(n)
    ]

    # k 이하인 위치들 True
    for ck in range(1, k+1):
        cur_pos_lst = h_pos[ck]
        for cpos in cur_pos_lst:
            vis[cpos[0]][cpos[1]] = True
    
    # 모든 위치에 대해 bfs를 돌며 방문 배열 True화
    bfs_cnt = 0
    for i in range(n):
        for j in range(m):
            if not vis[i][j]:
                bfs_cnt+=1
                bfs(i, j, vis)
    
    if bfs_cnt > max_k_val:
        max_k_val = bfs_cnt
        max_k = k

print(f'{max_k} {max_k_val}')