n = int(input())

ans = []
vis = [False] * (n+1)

def perm_rev(lev):
    if lev == n:
        print(*ans)
        return
    
    for cn in range(n, 0, -1):
        if not vis[cn]:
            ans.append(cn)
            vis[cn] = True       
            perm_rev(lev+1)
            vis[cn] = False
            ans.pop()           

perm_rev(0)