"""

숫자는 1~9

S 1 2 3 E
S 1 2 4 E
S 1 2 5 E 
...
S 7 8 9 E

각 케이스에 대해 최단거리 구하고, 거기서 제일 작은 값 출력
간 위치 중복 허용..

S 1 2 3 E
각 포인트로 갈때마다 bfs + vis 초기화 

"""

from itertools import combinations
import sys

n = int(input().strip())
arr = [
    list(input().strip())
    for _ in range(n)
]

coin_nums = []
pos_dict = {}

def get_dist(p1, p2):
    p1_x, p1_y = p1
    p2_x, p2_y = p2
    return abs(p1_x-p2_x) + abs(p2_y-p1_y)


def get_S_c3_E_dist(coins_3):
    c1, c2, c3 = coins_3
    d1 = get_dist(pos_dict['S'], pos_dict[c1])
    d2 = get_dist(pos_dict[c1], pos_dict[c2])
    d3 = get_dist(pos_dict[c2], pos_dict[c3])
    d4 = get_dist(pos_dict[c3], pos_dict['E'])
    return d1 + d2 + d3 + d4

num_cnt = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] != '.' and arr[i][j] != 'S' and arr[i][j] != 'E':
            num = int(arr[i][j])
            coin_nums.append(num)
            pos_dict[num] = (i, j)
            num_cnt += 1
        elif arr[i][j] == 'S':
            pos_dict['S'] = (i, j)
        elif arr[i][j] == 'E':
            pos_dict['E'] = (i, j)

if num_cnt < 3:
    print(-1)
    sys.exit(0)

coin_nums.sort()
coin_combs = list(combinations(coin_nums, 3))
# print(coin_combs)
# print(pos_dict)


min_dist = 99999999
for coins in coin_combs:
    dist = get_S_c3_E_dist(coins)
    min_dist = min(min_dist, dist)

print(min_dist)