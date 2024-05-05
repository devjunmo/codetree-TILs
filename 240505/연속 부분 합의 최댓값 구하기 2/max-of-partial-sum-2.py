n = int(input().strip())
nums = list(map(int, input().strip().split()))

# max(cur_max + cur_val, cur_val)

cur_max = 0

for num in nums:
    cur_max = max(cur_max + num, num)

print(cur_max)