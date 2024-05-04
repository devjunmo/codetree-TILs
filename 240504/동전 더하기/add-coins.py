n, k = tuple(map(int, input().strip().split(' ')))
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)

cnt = 0

while k > 0:
    for c in coins:
        if c > k:
            continue
        else:
            cnt += 1
            k -= c
            break

print(cnt)