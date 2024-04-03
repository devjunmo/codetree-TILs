from itertools import combinations

n = int(input())
lst = list(map(int, input().strip().split(' ')))

mid_val = sum(lst)/2

gap_min_val = 99999
gap_min_case = ()

comb = list(combinations(lst, n))

for cb in comb:
    cur_sum = sum(cb)
    mid_gap = abs(mid_val-cur_sum)
    if gap_min_val > mid_gap:
        gap_min_val = mid_gap
        gap_min_case = cb

g2 = []

for mc in gap_min_case:
    lst.remove(mc)

g2 = lst
ans = abs(sum(gap_min_case) - sum(g2))

print(ans)