# n, k = tuple(map(int, input().strip().split(' ')))

# points = []
# cur_st = 0  # 0점에서 시작
# for _ in range(n):
#     mv_cnt, d = tuple(input().strip().split(' '))
#     mv_cnt = int(mv_cnt)
    
#     if d == 'R':
#         end_point = cur_st + mv_cnt
#         points.append((cur_st, end_point))
#         cur_st = end_point
#     else:
#         end_point = cur_st - mv_cnt
#         points.append((end_point, cur_st))
#         cur_st = end_point
    
# points.sort()
# print(points)

# # (x1, -1, i)
# # (x2, +1, i)
# # 위 같은 형태로 튜플 적재
# segments=[]
# for i, (x1,x2) in enumerate(points):
#     segments.append((x1,-1,i))
#     segments.append((x2,1,i))
# segments.sort(key=lambda x:(x[0],x[2]))
# print(segments)
# trigg=False
# ans=0
# segset=set()
# # set에 1일때 i를 넣고 
# # 길이가 k이상이면서 
# # 트리거 False면 
# # ans+=1 하고 트리거 True

# # -1일때 i를빼고 
# # 길이가 k미만이면 트리거 False
# open_x=0
# for x,v,i in segments:
#     if v==-1:
#         segset.add(i)
#         if len(segset)>=k and not trigg:
#             #ans+=1
#             # print(segset)
#             trigg=True
#             open_x = x
#             # print('ddd')

#     else:
#         segset.remove(i)
#         #print(ans)
#         if len(segset) < k:
#             trigg=False
#             ans+=abs(open_x-x)
#             # open_x=x


# print(ans)

n, k = map(int, input().strip().split())

points = []
cur_st = 0  # 0점에서 시작
for _ in range(n):
    mv_cnt, d = input().strip().split()
    mv_cnt = int(mv_cnt)
    
    if d == 'R':
        end_point = cur_st + mv_cnt
        points.append((cur_st, end_point))
        cur_st = end_point
    else:
        end_point = cur_st - mv_cnt
        points.append((end_point, cur_st))
        cur_st = end_point
    
segments = []
for x1, x2 in points:
    segments.append((x1, 1))
    segments.append((x2, -1))

segments.sort()
ans = 0
current_count = 0
last_position = None

for x, value in segments:
    if last_position is not None and current_count >= k:
        ans += x - last_position
    current_count += value
    last_position = x

print(ans)