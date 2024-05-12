n,t=tuple(map(int,input().strip().split(' ')))

grid=[
    list(map(int,input().strip().split(' ')))
    for _ in range(n)
]

tmp_arr = []

def push_right(lst):
    pass


def set_tmp(t_idx):
    pass


def clean_tmp_arr():
    pass


for sec in range(t):
    for row in grid:
        push_right(row)
    
    for tmp_i in range(len(tmp_arr)):
        set_tmp(tmp_i)


for row in grid:
    print(*row)