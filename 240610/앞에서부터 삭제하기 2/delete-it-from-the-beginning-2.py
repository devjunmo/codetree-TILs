"""

1 + 2
/
2

= 평균 * 3 - 3
/
2


하나 뺀 평균 구하기
기존 평균 * 기존 n - 뺄 숫자 / n-1

N=5 (k=1~3) -> 0~n-3 index 
3 1 9 2 7

"""

import heapq

n = int(input())
lst = list(map(int, input().strip().split(' ')))
lst_len = len(lst)
pq = []
max_avg = -1

# 0~k 인덱스까지를 없애면 남는 배열이 k+1~n-1 인덱스임 
# 맨 뒤에꺼 하나를 pq에 넣은 상태에서
# 그 다음 뒤에꺼를 하나씩 pq에 넣고 top을 sum 변수에서 뺀 다음 평균 구하기
# k인덱스 하나 뒤꺼를 추가한다고 생각 
heapq.heappush(pq, lst[-1])
cur_sum = lst[-1]
cur_len = 1

for k in range(n-2, 0, -1):
    heapq.heappush(pq, lst[k])
    cur_sum += lst[k]
    cur_len += 1
    cur_avg = (cur_sum-pq[0])/(cur_len-1)
    max_avg = max(max_avg, cur_avg)

print(f'{max_avg:.2f}')
# test = [1,2,3]
# print(f'{sum(test)/3:.4f}')