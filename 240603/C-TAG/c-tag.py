from itertools import combinations

n, m=tuple(map(int, input().strip().split(' ')))

ga_grid = [
    list(input().strip())
    for _ in range(n)
]

gb_grid = [
    list(input().strip())
    for _ in range(n)
]

# 0~m-1 숫자 배열 중 3개 조합 뽑기
idx_lst = [i for i in range(m)]
case_lst = list(combinations(idx_lst, 3))

cnt = 0

for cl in case_lst:
    x, y, z = cl
    set_a = set()
    set_b = set()

    for ga in ga_grid:
        set_a.add((ga[x], ga[y], ga[z]))
    for gb in gb_grid:
        set_b.add((gb[x], gb[y], gb[z]))
    
    if set_a.isdisjoint(set_b):
        cnt+=1

print(cnt)