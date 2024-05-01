n, m = tuple(map(int, input().split(' ')))

A = list(map(int, input().strip().split(' ')))
B = list(map(int, input().strip().split(' ')))

a_idx = 0

is_seq = True

for b_idx in range(m):
    b_val = B[b_idx]
    # a_idx가 정상범위면서 b_val이랑 같을 때까지 a_idx 증가
    while a_idx<n and A[a_idx] != b_val:
        a_idx += 1
    
    # 일치 한다면
    if a_idx < n and A[a_idx] == b_val:
        pass
    else:
        print('No')
        is_seq = False
        break

if is_seq:
    print('Yes')