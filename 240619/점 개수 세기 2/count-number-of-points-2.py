import bisect

MAX_M = 5000

# 변수 선언 및 입력
n, q = tuple(map(int, input().split()))
nums = []
mapper = {}
prefix_sum = [
    [0] * (MAX_M + 2)
    for _ in range(MAX_M + 2)
]

points = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

queries = [
    tuple(map(int, input().split()))
    for _ in range(q)
]


# x보다 같거나 큰 최초의 숫자를 구해
# 이를 좌표압축 했을 때의 결과를 반환합니다.
def get_lower_boundary(x):
    return bisect.bisect_left(nums, x) + 1


# x보다 같거나 작은 최초의 숫자를 구해
# 이를 좌표압축 했을 때의 결과를 반환합니다.
def get_upper_boundary(x):
    return bisect.bisect_right(nums, x)


# (x1, y1), (x2, y2) 직사각형 구간 내의 점의 개수를 반환합니다.
def get_sum(x1, y1, x2, y2):
    return prefix_sum[x2][y2]     - prefix_sum[x1 - 1][y2] - \
           prefix_sum[x2][y1 - 1] + prefix_sum[x1 - 1][y1 - 1]


# 주어진 x, y 좌표값들을 전부 리스트에 넣어줍니다.
for x, y in points:
    if x not in nums:
        nums.append(x)
    if y not in nums:
        nums.append(y)

# 리스트를 정렬합니다.
nums.sort()

cnt = 1
for num in nums:
    mapper[num] = cnt
    cnt += 1

# 주어진 점들에 대해 
# 누적합 배열을 완성합니다.
for x, y in points:
    # 좌표 압축을 진행합니다.
    new_x, new_y = mapper[x], mapper[y]
    prefix_sum[new_x][new_y] += 1

for i in range(1, cnt + 1):
    for j in range(1, cnt + 1):
        prefix_sum[i][j] += prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

# 각 질의에 대해
# 구간 내 점의 개수를 구합니다.
for x1, y1, x2, y2 in queries:
    # x1, y1의 경우 같거나 큰 최초의 위치를 lower_bound로,
    # x2, y2의 경우 같거나 작은 최초의 위치를 upper_bound - 1로 구해줍니다.

    new_x1 = get_lower_boundary(x1)
    new_y1 = get_lower_boundary(y1)
    new_x2 = get_upper_boundary(x2)
    new_y2 = get_upper_boundary(y2)

    # 구간 내 점의 개수를 
    # 누적합을 이용하여 계산합니다.
    ans = get_sum(new_x1, new_y1, new_x2, new_y2)
    print(ans)