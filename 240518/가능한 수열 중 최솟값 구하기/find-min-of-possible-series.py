"""
4 4
4 5 4 5
"""

import sys

n = int(input())
num = []

# 가능한 수열인지 확인한다
def is_possible():
    k_max = int(len(num)/2)
    for k in range(1, k_max+1):
        for st_idx in range(len(num)):
            # 비교할 대상이 배열의 범위를 넘으면 안한다
            if st_idx + (2 * k) - 1 > len(num) - 1:
                break
            l_lst = []
            r_lst = []

            for i in range(st_idx, st_idx+k):
                l_lst.append(num[i])
            for i in range(st_idx+k, st_idx+(2*k)):
                r_lst.append(num[i])
            
            # print(l_lst)
            # print(r_lst)
            # print('====')
            if l_lst == r_lst:
                return False

    # 걸리는게 없으면 가능한 수열
    return True

def permutation():
    if len(num) == n:
        res = ''
        for i in num:
            res += str(i)
        print(res)
        sys.exit(0)
        return
    
    for i in range(4, 7):
        num.append(i)
        if not is_possible():
            # print('ddd')
            num.pop()
            continue
        permutation()
        num.pop()


permutation()