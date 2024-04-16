n, m = tuple(map(int, input().strip().split(' ')))

cl_info = []  # (st, ed, h)
for i in range(n):
    cl_comp = tuple(map(int, input().strip().split(' ')))
    cl_info.append(cl_comp)

# dp[day][clothing] : day일 때 clothing 번 옷을 입었을 때의 최대 만족도
dp = [[-float('inf')] * n for _ in range(m)]

# 첫 번째 날 각 옷을 입는 경우 초기화
for c in range(n):
    st, ed, h = cl_info[c]
    if st == 1:
        dp[0][c] = 0  # 첫 날에는 만족도 차이가 없으므로 0으로 시작

# 이후 날짜에 대해 계산
for day in range(1, m):
    for c in range(n):
        st, ed, h = cl_info[c]
        if st <= day + 1 <= ed:  # c 옷을 day 날짜에 입을 수 있는 경우
            for c_past in range(n):
                st_p, ed_p, h_p = cl_info[c_past]
                if st_p <= day <= ed_p:  # c_past 옷을 day-1 날짜에 입을 수 있었던 경우
                    h_gap = abs(h_p - h)
                    dp[day][c] = max(dp[day][c], dp[day - 1][c_past] + h_gap)

# 최대 만족도 찾기
max_satisfaction = max(dp[m-1])  # 마지막 날 입을 수 있는 모든 옷의 만족도 중 최대값
print(max_satisfaction)


# n, m = tuple(map(int, input().strip().split(' ')))

# cl_info = [] # (st, ed, h)
# for i in range(n):
#     cl_comp = tuple(map(int, input().strip().split(' ')))
#     cl_info.append(cl_comp)

# # 현재 날의 최대 만족도
# dp = [0] * m


# for day in range(1, m):
#   tmp_max = 0
#   for c in range(n):
#     st = cl_info[c][0]-1
#     ed = cl_info[c][1]-1
#     h = cl_info[c][2]
    
#     if st <= day <= ed:
#       for c_past in range(n):
#         st_p = cl_info[c_past][0]-1
#         ed_p = cl_info[c_past][1]-1
#         h_p = cl_info[c_past][2]
#         if st_p <= day-1 <= ed_p:
#           h_gap = abs(h_p-h)
#           tmp_max = max(h_gap + dp[day-1], tmp_max)
#   dp[day] = tmp_max

# print(dp[m-1])
# # print(dp)