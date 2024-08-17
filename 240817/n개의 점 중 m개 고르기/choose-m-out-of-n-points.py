# 1. 모든 케이스 구하기 = 10만
# 2. 각 케이스에 대해 최장 거리 구하기 = 10*10 = 100
# 3. 거리값 최소 갱신 
# 도합 100만이라 완탐 ok

from itertools import combinations
import math
import sys

n, m = tuple(map(int, input().strip().split(' ')))
points=[]
points_idx=[i for i in range(n)]
comb_idx_lst=list(combinations(points_idx, m))

for _ in range(n):
    points.append(tuple(map(int, input().strip().split(' '))))

def get_dist(p1, p2):
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
    # return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

ans = sys.maxsize

for comb_idx in comb_idx_lst:
    # comb_idx들에 대해서도 조합 구해야 함
    cur_comb_lst = list(combinations(comb_idx, 2))
    max_dist = -1
    max_x_idx = -1
    max_y_idx = -1
    for cur_point_idx in cur_comb_lst:
        i1, i2 = cur_point_idx
        cur_dst = get_dist(points[i1], points[i2])
        if cur_dst > max_dist:
            max_dist = cur_dst
            max_x_idx = i1
            max_y_idx = i2
    ans = min(ans, max_dist)

# print(int(ans**2))
print(ans)