n, m = tuple(map(int, input().strip().split(' ')))
b_arr = [
    int(input().strip())
    for _ in range(n)
]


def find_boom():
    # m번 이상 반복되는 구간을 리스트에 넣기
    target_pos_lst = [] # [(a1, b1), (a2, b2), ...]
    left = 0
    right = 0
    while right < len(b_arr):
        lv = b_arr[left]
        rv = b_arr[right]
        if lv != rv:
            gap = right - left
            if gap >= m:
                target_pos_lst.append((left, right-1))
            left = right # 위치 동기화
        right += 1

        if right==len(b_arr) and lv==rv:
            target_pos_lst.append((left,right-1))
    
    # print(target_pos_lst)
    return target_pos_lst


def boom(target_pos_lst):
    global b_arr
    if not target_pos_lst:
        return 0
    # pos list의 범위를 모두 -1로 바꾸고
    for pos in target_pos_lst:
        a, b = pos
        for i in range(a, b+1):
            b_arr[i] = -1
    
    # -1이 아닌 값을 확보한 뒤 b_arr로 카피
    after_arr = []
    for b in b_arr:
        if b != -1:
            after_arr.append(b)
    b_arr = after_arr.copy()
    return 1


while True:
    res = boom(find_boom())
    if res == 0:
        break


print(len(b_arr))
for b in b_arr:
    print(b)