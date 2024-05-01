n=int(input())
arr = list(map(int, input().strip().split(' ')))
cnt_arr = [0] * 100100

max_len = -1
left = 0

for right in range(n):
    cnt_arr[arr[right]] += 1

    # 현재 숫자에 대해 중복이 있을 때
    while cnt_arr[arr[right]] > 1:
        # left를 옮긴다
        cnt_arr[arr[left]] -= 1
        left += 1
    
    # 길이 계산
    max_len = max(max_len, right-left+1)

print(max_len)