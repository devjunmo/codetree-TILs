import sys

n = int(input())
lst = [list(map(int, input().strip().split(' '))) for _ in range(n)]

vis = [False] * n
max_val = -1

def simulation(lev, c_min):
    global max_val
    if lev == n:
        max_val = max(max_val, c_min)
        return
    
    for i in range(n):
        if not vis[i]:
            vis[i] = True
            cur_min = min(c_min, lst[lev][i])
            simulation(lev+1, cur_min)
            vis[i] = False

simulation(0, 99999999)
print(max_val)