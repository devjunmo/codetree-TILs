n, m, k = tuple(map(int, input().strip().split(' ')))

# 말이 선택되는 경우의 수 -> 4의 12승? -> 2의 24승 -> 2^10 2^10 2^4 = 16 * 100만 
# 주어지는 수가 1만 될수도 있으니 시간초과 가능할수 있다..

turn_mvs = list(map(int, input().strip().split(' ')))

# 각 순간에 어떤 말을 움직일지를 바로바로 선택

pon = [1] * k # 인덱스 = 폰 이름, 값= 폰이 어디있는지 값
max_val = -1

def calc_pon():
    res = 0
    for p in pon:
        if p >= m:
            res += 1
    return res


def simulate(cur_turn):
    global max_val
    calc_val = calc_pon()
    max_val = max(calc_val, max_val)
    if cur_turn == n:
        calc_val = calc_pon()
        max_val = max(calc_val, max_val)
        return
    
    for i in range(k):
        # 만약 i번 폰 값이 m 미만일 때
        # 폰에게 현재 값 더해줌
        if pon[i] < m:
            pon[i] = pon[i] + turn_mvs[cur_turn]
            simulate(cur_turn+1)
            pon[i] = pon[i] - turn_mvs[cur_turn]



simulate(0)  # 턴: 0~n-1로 생각
print(max_val)