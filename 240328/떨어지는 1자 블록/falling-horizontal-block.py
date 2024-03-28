"""
4 3 1
0 0 0 0
0 0 0 1
1 0 0 1
1 1 1 1
"""

n, m, k = tuple(map(int, input().strip().split(' ')))
arr = [
    list(map(int, input().strip().split(' ')))
    for _ in range(n)
]
start_col = k-1
end_col = k-1 + m-1
start_row = 0
is_finish = False

if n == 1:
    for row in arr:
        print(*row)
else:
    while True:
        # 블럭조각 순회하며 밑에 있는 모든 블럭이 0인지 체크
        for j in range(start_col, end_col+1):
            if arr[start_row+1][j] == 1:
                is_finish = True
                break
        if is_finish:
            break
        
        # 모두 영이라면 블럭 전진
        start_row += 1
        for j in range(start_col, end_col+1):
            arr[start_row][j] = 1
            arr[start_row-1][j] = 0

    for row in arr:
        print(*row)