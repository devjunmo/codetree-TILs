n = int(input())

ans = []
vis = [False] * (n+1)

def perm(lev):
    if lev == n:
        print(*ans)
        return
    
    for cn in range(1, n+1):
        if not vis[cn]:
            ans.append(cn)
            vis[cn] = True
            perm(lev+1)
            ans.pop()
            vis[cn] = False

perm(0)