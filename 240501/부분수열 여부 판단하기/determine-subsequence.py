n, m = map(int, input().split())

A = list(map(int, input().strip().split()))
B = list(map(int, input().strip().split()))

a_idx = 0
found = True  # 조금 더 직관적인 변수명

for b in B:
    while a_idx < n and A[a_idx] != b:
        a_idx += 1
    
    if a_idx == n:  # 더 이상 A에서 b를 찾을 수 없는 경우
        found = False
        break
    a_idx += 1  # 일치하는 경우 다음 인덱스에서 계속 검색

print("Yes" if found else "No")