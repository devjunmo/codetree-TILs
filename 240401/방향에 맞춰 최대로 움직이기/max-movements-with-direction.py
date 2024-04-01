"""
3
7 1 4
2 6 3
9 8 5
5 3 1
6 3 7
2 4 8
3 3
"""

n = int(input())
num_arr = [
    list(map(int, input().strip().split(' ')))
    for _ in range(n)
]
dir_arr = [
    list(map(int, input().strip().split(' ')))
    for _ in range(n)
]

# 1번째 부터 8방향 
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]

r, c = tuple(map(int, input().strip().split(' ')))
r -= 1
c -= 1

max_cnt = -1

def simulate(cnt, r, c):
    global max_cnt

    d = dir_arr[r][c]
    nx = r + dx[d]
    ny = c + dy[d]
    # 정상범위 일 때
    if 0 <= nx < n and 0 <= ny < n:
        next_val = num_arr[nx][ny]
        cur_val = num_arr[r][c]
        # 만약 다음 방향의 값이 현재 값보다 같거나 작다면
        if next_val <= cur_val:
            # max랑 비교 후 return
            max_cnt = max(max_cnt, cnt)
            return
        else:
            simulate(cnt+1, nx, ny)

simulate(1, r, c)

print(max_cnt)