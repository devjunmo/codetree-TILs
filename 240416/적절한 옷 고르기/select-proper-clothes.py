"""
동일한 상태 -> 현재까지 날짜, 현재까지 만족도, 마지막에 입은 옷 
현재까지 픽한 옷이 주어지고 마지막의 옷이 정해졌을 때 만족도 최대여야 함 
그래야 다음껄 뭘 선택하던지간에 현재까진 동등

dp[i][j] -> i번째 날 까지 입을 옷을 모두 정했고, 마지막 날 입을 옷이 j일 때 최대 만족도


"""

n, m = tuple(map(int, input().strip().split(' ')))

cl_info = [] # (st, ed, h)
for i in range(n):
    cl_comp = tuple(map(int, input().strip().split(' ')))
    cl_info.append(cl_comp)

# 현재 날의 최대 만족도
dp = [0] * m



"""
같은 날짜에 같은 옷을 선택했을 때 만족도가 높을수록 좋다

    1      2.     3
1d. 0      0.     0
2d  39-39.vs 39-20 vs x
3d
4d
5d
"""

for day in range(1, m):
  for c in range(n):
    st = cl_info[c][0]-1
    ed = cl_info[c][1]-1
    h = cl_info[c][2]
    if st <= day <= ed:
      for c_past in range(n):
        st_p = cl_info[c_past][0]-1
        ed_p = cl_info[c_past][1]-1
        h_p = cl_info[c_past][2]
        if st_p <= day-1 <= ed_p:
          h_gap = abs(h_p-h)
          dp[day] = max(dp[day], h_gap)

print(dp[m-1])