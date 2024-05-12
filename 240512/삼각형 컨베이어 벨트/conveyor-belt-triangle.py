n,t=tuple(map(int,input().strip().split(' ')))

grid=[
    list(map(int,input().strip().split(' ')))
    for _ in range(3)
]

tmp_arr = []

def push_right(lst):
    tmp_arr.append(lst[n-1]) # 맨 끝값 백업 
    # 한칸 밀기
    for i in range(n-2, -1, -1):
        lst[i+1] = lst[i]


def set_tmp(t_idx):
    if t_idx == 2:
        grid[0][0] = tmp_arr[t_idx]
    else:
        grid[t_idx+1][0] = tmp_arr[t_idx]


def clean_tmp_arr():
    tmp_arr = []


for sec in range(t):
    for row in grid:
        push_right(row)
    
    for tmp_i in range(3):
        set_tmp(tmp_i)


for row in grid:
    print(*row)