k, n = tuple(map(int, input().strip().split(' ')))  # k이하의 숫자, n자리수

ans = []

def chk_append_passible(lev, cn):
    if n < 3 or lev < 2:
        return True
    if cn == ans[lev-1] and cn == ans[lev-2]:
        return False
    return True

# 같은숫자가 연속 세번인 경우는 제외
def perm(lev):
    if lev == n:
        print(*ans)
        return
    
    for cn in range(1, k+1):
        # 같은 숫자가 연속 세번이 아닐때만 append
        if chk_append_passible(lev, cn):
            ans.append(cn)
            perm(lev+1)
            ans.pop()

perm(0)