n = int(input())
num_arr = [
    list(map(int, input().strip().split(' ')))
    for _ in range(n)
]
dir_arr = [
    list(map(int, input().strip().split(' ')))
    for _ in range(n)
]
vis = [
    [False] * n
    for _ in range(n)
]

# 1번째 부터 8방향 
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]

r, c = tuple(map(int, input().strip().split(' ')))
r -= 1
c -= 1

max_cnt = 0

def simulate(cnt, r, c):
    global max_cnt
    d = dir_arr[r][c]
    for i in range(1, 4):
        nx = r + (i * dx[d])
        ny = c + (i * dy[d])
        #print(f'>>{nx}, {ny}')
        # 정상범위면서 방문 안한곳일 때 
        if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny]:
            next_val = num_arr[nx][ny]
            cur_val = num_arr[r][c]
            #print(f'next_val: {next_val}')
            #print(f'cur_val: {cur_val}')
            # 만약 다음 방향의 값이 현재 값보다 같거나 작다면
            if next_val <= cur_val:
                # max랑 비교 후 return
                max_cnt = max(max_cnt, cnt)
                vis[r][c] = False
                #print('ff')
                #return
            else:
                #print('dd')
                vis[nx][ny] = True
                simulate(cnt+1, nx, ny)
        else:
            #print('움직 x')
            max_cnt = max(max_cnt, cnt)
            vis[r][c] = False
            #return
        if not (0 <= nx < n and 0 <= ny < n):
            return    

vis[r][c] = True
simulate(0, r, c)

print(max_cnt)