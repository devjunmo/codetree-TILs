n = int(input().strip())
s1 = set(list(map(int, input().strip().split(' '))))
m = int(input().strip())
s2 = (list(map(int, input().strip().split(' '))))

ans = []
for s2_comp in s2:
    if s2_comp in s1:
        ans.append(1)
    else:
        ans.append(0)

print(*ans)