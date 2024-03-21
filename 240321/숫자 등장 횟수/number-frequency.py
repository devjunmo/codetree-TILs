n, m = tuple(map(int, input().strip().split(' ')))

lst = list(map(int, input().strip().split(' ')))
m_lst = list(map(int, input().strip().split(' ')))
ans = []

cnt_dict = {}

# lst를 순회하며 숫자:갯수로 dict 채우기
for l in lst:
    if not cnt_dict.get(l):
        cnt_dict[l] = 1
    else:
        cnt_dict[l] = cnt_dict[l] + 1

# m에 대해 값 구하기
for m in m_lst:
    if not cnt_dict.get(m):
        ans.append(0)
    else:
        ans.append(cnt_dict[m])

print(*ans)