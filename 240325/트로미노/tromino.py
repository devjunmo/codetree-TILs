n, m = tuple(map(int, input().strip().split(' ')))
arr = []
for _ in range(n):
    arr.append(list(map(int, input().strip().split(' '))))

max_val = -1

# 포인트가 정상 포인트인지 확인
def check_point(i, j):
    if 0<=i<n and 0<=j<m:
        return True
    else:
        return False

# ㄴ 도형에서 최대 찾기
## 포인트 기준 현위치 우 우하 하 방향의 총 4개에 대해
## 모두 더한 값에서 각 포인트 값을 한번씩 뺀 것들 중 최대값 찾고, max_val과 비교
for i in range(n):
    for j in range(m):
        # 모두 정상 범위일 때
        if check_point(i, j) and check_point(i, j+1) and check_point(i+1, j+1) and check_point(i+1, j):
            val1 = arr[i][j]
            val2 = arr[i][j+1]
            val3 = arr[i+1][j+1]
            val4 = arr[i+1][j]
            sum_val = val1 + val2 + val3 + val4
            cur_mx = max([sum_val-val1, sum_val-val2,sum_val-val3,sum_val-val4])
            max_val = max(max_val, cur_mx) # 최대값 갱신

# ㅡ 자 도형에서 최대 찾기
## 포인트, 우, 우우의 합과 max_val 비교
for i in range(n):
    for j in range(m):
        if check_point(i, j) and check_point(i, j+1) and check_point(i, j+2):
            val1 = arr[i][j]
            val2 = arr[i][j+1]
            val3 = arr[i][j+2]
            sum_val = val1 + val2 + val3
            max_val = max(max_val, sum_val) # 최대값 갱신

# ㅣ 자 도형에서 최대 찾기 
## 포인트, 하, 하하의 합과 max_val 비교
for i in range(n):
    for j in range(m):
        if check_point(i, j) and check_point(i+1, j) and check_point(i+2, j):
            val1 = arr[i][j]
            val2 = arr[i+1][j]
            val3 = arr[i+2][j]
            sum_val = val1 + val2 + val3
            max_val = max(max_val, sum_val) # 최대값 갱신


print(max_val)