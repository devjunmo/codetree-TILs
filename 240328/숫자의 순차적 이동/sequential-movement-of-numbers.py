n, m = tuple(map(int, input().strip().split(' ')))
arr = [
    list(map(int, input().strip().split(' ')))
    for _ in range(n)
]

# 8방 탐색
# 상 상우 우 우하 하 하좌 좌 좌상
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

pos_dict = dict()

# 순회하며 값에 대한 위치를 dict에 저장
for i in range(n):
    for j in range(n):
        v = arr[i][j]
        pos_dict[v] = (i, j)

# m 턴 진행 
for _ in range(m):
    for num in range(1, (n*n)+1):
        cur_max = -1
        # 8방 탐색 후 최대값 저장
        cx = pos_dict[num][0]
        cy = pos_dict[num][1]
        for d in range(8):
            nx = cx + dx[d]
            ny = cy + dy[d]
            # next가 정상범위일 때 진행
            if 0 <= nx < n and 0 <= ny < n:
                cur_max = max(cur_max, arr[nx][ny])
        cur_max_pos = pos_dict[cur_max]
        mx = cur_max_pos[0]
        my = cur_max_pos[1]
        # 배열상에서 위치 바꾸기
        tmp = -1
        tmp = arr[cx][cy]
        arr[cx][cy] = cur_max
        arr[mx][my] = tmp

        # posdict 상에서 위치 바꾸기
        pos_dict[cur_max] = pos_dict[num]
        pos_dict[num] = cur_max_pos


# print(pos_dict)
for row in arr:
    print(*row)