n, k = tuple(map(int, input().strip().split(' ')))

points = []
cur_st = 0  # 0점에서 시작
for _ in range(n):
    mv_cnt, d = tuple(input().strip().split(' '))
    mv_cnt = int(mv_cnt)
    
    if d == 'R':
        end_point = cur_st + mv_cnt
        points.append((cur_st, end_point))
        cur_st = end_point
    else:
        end_point = cur_st - mv_cnt
        points.append((end_point, cur_st))
        cur_st = end_point
    
points.sort()

# (x1, +1, i)
# (x2, -1, i)
# 위 같은 형태로 튜플 적재

#