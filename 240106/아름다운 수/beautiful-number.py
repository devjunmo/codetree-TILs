# 4^10 -> 100만 -> 시간 ok
# 2천만 int -> 80MB. 공간 ok


n = int(input())
cur_num = []
res = 0

# 1. 모든 경우의 10자리 수 구하기
def permutation(lev):
    if lev == n:
        chk_pretty_num()
        return
    
    for cn in range(1, 5):
        cur_num.append(cn)
        permutation(lev+1)
        cur_num.pop()


# 2. 아름다운 수 인지 판단하기. 맞다면 res++
def chk_pretty_num():
    global res
    if cond1() or cond2():
        res+=1


# 3. 조건 1) 1~4, 숫자 만큼 연달아 같은숫자
def cond1_chk(idx):
    # 인덱스를 받으면 해당 인덱스 값을 구하고
    cur_val = cur_num[idx]

    # 해당 인덱스부터 해당 값만큼의 범위를 체크
    for i in range(idx, idx+cur_val):
        # 연속된 수가 아니라면
        if i >= n or cur_num[i] != cur_val:
            return -1
    
    # 모두 연속된 수라면 다음 index 리턴
    return idx + cur_val

def cond1():
    cur_idx = 0
    while True:
        if cur_idx >= n:
            return True
        nxt_idx = cond1_chk(cur_idx)
        if nxt_idx == -1:
            return False
        cur_idx = nxt_idx


# 조건 2) 갯수가 해당 숫자의 배수만큼 있을 때
# 현재 인덱스부터 현재 인덱스의 값과 동일하지 않을때까지 카운트 세기
#   해당 카운트를 현제 인덱스의 값과 나눴을때 나머지가 영이면 다음 인덱스, 아니면 return False

def cond2_chk(idx):
    cnt= 0
    # 인덱스를 받으면 해당 인덱스 값을 구하고
    cur_val = cur_num[idx]
    for i in range(idx, n):
        if(cur_num[i] != cur_val):
            break
        cnt += 1
    if cnt % cur_val == 0:
        return cnt + idx
    else:
        return -1


def cond2():
    cur_idx = 0
    while True:
        if cur_idx >= n:
            return True
        nxt_idx = cond2_chk(cur_idx)
        if nxt_idx == -1:
            return False
        cur_idx = nxt_idx


permutation(0)

print(res)