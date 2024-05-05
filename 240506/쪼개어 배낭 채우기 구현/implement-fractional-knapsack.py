n, m = tuple(map(int, input().strip().split(' ')))

jry_lst = []

for _ in range(n):
    # (무게당 가격, 무게, 가격)
    w, v = map(int, input().strip().split(' '))
    v_per_w = v/w
    jry_lst.append((v_per_w, w, v))

jry_lst.sort(reverse=True)

sum_val = 0

for jry in jry_lst:
    if m <= 0:
        break
    
    if m - jry[1] >= 0:
        # 분할 필요 없음
        m = m - jry[1] # 도둑 소지 무게 빼주고 
        sum_val += jry[2] # 누적 가치에 현재 보석 더해주고

    else:
        # 분할 필요
        frac_val = jry[2] * (m/jry[1])
        sum_val += frac_val
        break  # 막타라서 더 돌 필요 없음 

print(f"{round(sum_val, 3):.3f}")