from itertools import permutations
import sys

n = int(input())
adj_lst = [
    list(map(int, input().strip().split(' ')))
    for _ in range(n)
]

point_lst = [i for i in range(1,n)]

vis_case = list(permutations(point_lst, n-1))

def calc(case_lst):
    case_lst = [0] + case_lst + [0]
    sum_v = 0
    for i in range(len(case_lst)-1):
        p1 = case_lst[i]
        p2 = case_lst[i+1]
        sum_v += adj_lst[p1][p2]
    return sum_v
    

min_val = sys.maxsize

for cs in vis_case:
    val = calc(list(cs))
    #print(cs)
    min_val = min(min_val, val)

print(min_val)