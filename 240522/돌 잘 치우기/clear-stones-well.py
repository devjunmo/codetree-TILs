from itertools import combinations

n,k,m=tuple(map(int,input().split(' ')))
grid=[
    list(map(int,input().strip().split(' ')))
    for _ in range(n)
]
start_pos=[
    tuple(map(lambda x:int(x)-1,input().strip().split(' ')))
    for _ in range(k)
]

stone_pos=[]

for i in range(n):
    for j in range(n):
        v = grid[i][j]
        if v == 1:
            stone_pos.append((i,j))

rm_stones=list(combinations(stone_pos,m))
print(rm_stones)