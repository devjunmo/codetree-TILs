lst = list(input().strip())
n = len(lst)
back = [0] * n

back_cnt = 0

for i in range(n-1, 1, -1):
    if lst[i] == ')' and lst[i-1] == ')':
        back_cnt += 1
    back[i] = back_cnt

pair = 0

for i in range(n-2):
    if lst[i] == '(' and lst[i+1] == '(':
        pair += back[i+2]

print(pair)