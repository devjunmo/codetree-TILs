"""
1부터 n까지의 자연수의 합이 s이하인 경우 중 가능한 n의 최댓값을 구하는 프로그램을 작성하세요.

출력: 가능한 n 값

200 / 19

1~n 합이 200 이하인 값 중 n의 최대

n의 최대를 200(s)이라고 하고... 이분탐색

100 -> sum하면 200이하인가? 

1+끝/2 * 끝  => 200 초과이므로 pass

1 2 3 4 5 -> 15
1+끝/2 * 끝 


"""

import bisect
import math

s = int(input())
is_fin = False

while not is_fin:
    if s == 2:
        print(3)
        break
    if s == 1:
        print(1)
    mid_val = int(math.ceil(s/2))
    
    sum_val = (mid_val*(mid_val+1))/2
    print(sum_val)
    break