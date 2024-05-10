n, m = tuple(map(int, input().strip().split(' ')))

arr = [
   list(map(int, input().strip().split(' ')))
    for _ in range(n)
]

# print(arr)

# 중앙값과 현재위치, k를 주면 맨하탄 거리 인지 여부 리턴
def get_mht_dist(center_pos, cur_pos, k):
    ct_x, ct_y = center_pos
    cur_x, cur_y = cur_pos
    return (abs(ct_x-cur_x) + abs(ct_y-cur_y)) <= k


def get_cost(k):
    return k * k + (k + 1) * (k + 1)


max_gold = 0


for i in range(n):
    for j in range(n):
        # 중앙 (i, j)에 대해 
        for k in range(n):
            # k값이 주어졌을 때
            mining_cost = get_cost(k)
            gold_cnt = 0
            for p in range(n):
                for q in range(n):
                    # (p, q)점을 돌면서 맨하탄 거리 체크
                    # if 맨하탄 이내면 
                    if get_mht_dist((i,j),(p,q), k):
                        # # if 맨하탄 이내 이면서 코인이 있으면
                        # #   골드 cnt += 1
                        if arr[p][q] == 1:
                            gold_cnt += 1
                            # print(gold_cnt)
                    
                    # if 골드 카운트 * m - 맨하탄 size > 0 일 때 
                    #    최대 금 갯수 갱신
                    if (gold_cnt * m) - mining_cost >= 0 and max_gold < gold_cnt:
                        # max_gold = max(max_gold, gold_cnt)
                        max_gold = gold_cnt
                        # print(f'i: {i}, j: {j}, p: {p}, q: {q}, k: {k}, gold: {gold_cnt}, mining_cost: {mining_cost}')


print(max_gold)