n, m = tuple(map(int, input().strip().split(' ')))
ans = []

def comb(lev, start):
    if lev == m:
        print(*ans)
        return
    
    for num in range(start, n+1):
        ans.append(num)
        comb(lev+1, num+1)
        ans.pop()

comb(0, 1)