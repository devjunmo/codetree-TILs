n, s = tuple(map(int, input().strip().split(' ')))

arr = list(map(int, input().strip().split(' ')))
# arr = [0] + arr


min_len = 9999999
sum_val = 0

l_idx = 0

for r_idx in range(n):
    sum_val += arr[r_idx]

    # 합이 s 이상일 때 길이 잰다
    while sum_val >= s:
        min_len = min(min_len, r_idx-l_idx+1)
        # l_idx 전진          
        sum_val -= arr[l_idx]
        l_idx+=1

print(min_len)