n, m, q = tuple(map(int, input().strip().split(' ')))
arr = [
    list(map(int, input().strip().split(' ')))
    for _ in range(n)
]
cmds = [
    tuple(input().strip().split(' ')) # r, d // r -> 1 이상
    for _ in range(q)
]

vis = [False] * n  # 행 방문 체크

# 전파 체크 후 전파 가능하면 재귀
# 방문 안한 배열에 한해서 들어와야 함
def propag(r, d):
    up_pass = False
    down_pass = False

    # 위 배열과 비교
    if 0 <= r-1 < n:
        for j in range(m):
            if arr[r][j] == arr[r-1][j]:
                up_pass = True
                break
        if up_pass:
            # [true_value] if [condition] else [false_value]
            simulate(r-1, 'L') if d == 'R' else simulate(r-1, 'R')

    # 아래 배열과 비교
    if 0 <= r+1 < n:
        for j in range(m):
            if arr[r][j] == arr[r+1][j]:
                down_pass = True
                break
        if down_pass:
            simulate(r+1, 'L') if d == 'R' else simulate(r+1, 'R')


def push_arr(r, d):
    tmp = 0
    if d == 'L':
        tmp = arr[r][m-1] # 맨 오른쪽꺼를 tmp에 저장하고
        for j in range(m-1, 0, -1):
            arr[r][j] = arr[r][j-1]
        arr[r][0] = tmp # 맨 왼쪽꺼를 tmp값으로 채운다
    elif d == 'R':
        tmp = arr[r][0] # 맨 왼쪽꺼를 tmp에 저장하고
        for j in range(0, m-1):
            arr[r][j] = arr[r][j+1]
        arr[r][m-1] = tmp # 맨 오른쪽꺼를 tmp값으로 채운다


# 대상 행과 방향을 주면 리스트 요소를 밀어준다
def simulate(r, d):
    if vis[r]:
        return
    
    # 해당 r 방문 체크
    vis[r] = True

    # 배열 밀기
    push_arr(r, d)
    
    # 전파 진행
    propag(r, d)



for r, d in cmds:
    r = int(r)
    r_idx = r-1
    simulate(r_idx, d)

    # 방문 배열 초기화
    for i in range(n):
        vis[i] = False


for row in arr:
    print(*row)