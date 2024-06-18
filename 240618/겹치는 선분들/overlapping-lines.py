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
segments=[]
for i, (x1,x2) in enumerate(points):
    segments.append((x1,1,i))
    segments.append((x2,-1,i))
segments.sort()
trigg=False
ans=0
segset=set()
# set에 1일때 i를 넣고 
# 길이가 k이상이면서 
# 트리거 False면 
# ans+=1 하고 트리거 True

# -1일때 i를빼고 
# 길이가 k미만이면 트리거 False
open_x=0
for x,v,i in segments:
    if v==1:
        segset.add(i)
        #print(segset)
        if len(segset)>=k and not trigg:
            #ans+=1
            trigg=True
            open_x = x

    else:
        segset.remove(i)
        #print(ans)
        if len(segset) < k:
            trigg=False
            ans+=abs(open_x-x)
            open_x=x


print(ans)