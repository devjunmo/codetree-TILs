n, m = tuple(map(int, input().strip().split(' ')))

ans = []
max_val = -1

def calc_xor(a, b):
    return a^b

def comb(lev, st):
    global max_val

    if lev == m:
        cur_xor_val = ans[0]
        for i in range(1, len(ans)):
            cur_xor_val = calc_xor(cur_xor_val, ans[i])
        max_val = max(max_val, cur_xor_val)
        return
    
    for num in range(st, n):
        ans.append(num)
        comb(lev+1, st+1)
        ans.pop()

comb(0, 1)
print(max_val)