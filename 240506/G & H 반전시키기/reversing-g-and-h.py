n = int(input().strip())
initial = input().strip()
target = input().strip()

i = 0
cnt = 0

while i < n:
    if initial[i] != target[i]:
        cnt += 1
        # 비매칭 되는 연속 구간 i 증가
        while i < n and initial[i] != target[i]:
            i+=1
    else:
        i += 1

print(cnt)