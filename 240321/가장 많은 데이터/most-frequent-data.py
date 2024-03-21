n = int(input())
d = {}

for _ in range(n):
    s = input().strip()
    if s not in d:
        d[s] = 1
    else:
        d[s] = d[s] + 1

ans = -1

for k, v in d.items():
    ans = max(v, ans)

print(ans)