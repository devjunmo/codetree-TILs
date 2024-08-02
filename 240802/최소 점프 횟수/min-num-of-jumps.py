n = int(input())
lst = list(map(int, input().strip().split(' ')))

min_step = 999

def simul(idx, cur_step):
    global min_step
    if idx >= n-1:
        min_step = min(min_step, cur_step)
        return
    
    can_step = lst[idx]
    for cs in range(1, can_step+1):
        simul(idx+cs, cur_step+1)

simul(0, 0)
print(min_step)