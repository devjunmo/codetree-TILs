"""
앞에서 부터 가는데, 골라진 선분의 범위에 해당되는 모든 라인들 중 끝점이 가장 빠르게 끝나는걸 고르고 나머진 지워버린다 
- 만약 골라진 선분이 두개 이상이라면 끝나는게 빠른 라인을 기준으로 한다 

고르면 카운트 += 1

고른 선분의 끝점을 다음 탐색 시작 점으로 한다

"""


# n = int(input().strip())
# line_lst = [
#     tuple(map(int, input().strip().split(' ')))
#     for _ in range(n)
# ]

# line_lst.sort()

# cur_idx = 1

# # 현재 포인트에 매치되는 라인 중 가장 끝나는게 빠른 라인 고르기
# def get_range_line():
#     mat_lines = []
#     for line in line_lst:
#         x, y = line
#         if x <= cur_idx <= y:
#             mat_lines.append(line)
#     # sorted_lines = sorted(mat_lines, key=lambda x:x[1])
#     mat_lines.sort(key=lambda x:x[1])
#     if not mat_lines:
#         return False
#     return mat_lines[0]


# # line_lst의 선분들을 순회하여 픽한 라인의 범위에 있으면 해당 라인은 tmp_lst에 넣는다
# # 안골라진 선분들은 remain list에 넣고, line_lst에 덮어씌우기 한다
# # tmp_lst 중 가장 end가 빠른애를 고르고, 다음 순회는 end+1부터 진행한다
# cnt = 0
# while cur_idx <= 1000:
#     tmp_lst = []
#     remain_lst = []
#     rl = get_range_line()
#     # print(rl)
#     if rl:
#         rx, ry = rl
#         for line in line_lst:
#             cx, cy = line
#             if rx <= cx <= ry or rx <= cy <= ry:
#                 tmp_lst.append(line)
#             else:
#                 remain_lst.append(line)

#         # print(tmp_lst)
#         # print(remain_lst)
#         line_lst = remain_lst.copy()
#         tmp_lst.sort(key=lambda x:x[1])
#         pick_y = tmp_lst[0][1]
#         cur_idx = pick_y + 1
#         cnt +=1
#     else:
#         cur_idx += 1

# print(cnt)


# 입력 받기
n = int(input().strip())
line_lst = [tuple(map(int, input().strip().split())) for _ in range(n)]

# 끝나는 지점을 기준으로 정렬
line_lst.sort(key=lambda x: x[1])

# 현재 선택한 선분의 끝나는 지점
end_point = 0
cnt = 0

for line in line_lst:
    if line[0] > end_point:
        # 현재 선분이 겹치지 않으면 선택
        end_point = line[1]
        cnt += 1

print(cnt)