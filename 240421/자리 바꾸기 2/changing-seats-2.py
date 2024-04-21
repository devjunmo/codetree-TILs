n, k = tuple(map(int, input().split(' ')))

moves = [
    tuple(map(int, input().split(' ')))
    for _ in range(k)
]

# 좌석 리스트 
lst = [
    i for i in range(n+1)
]

"""
d = {
    key: 1 ~ n
    val: set(방문한 인덱스)
}
"""
d = dict()

for i in range(1, n+1):
    d[i] = set([i])


for _ in range(3):
    for mv in moves:
        idx1 = mv[0]
        idx2 = mv[1]

        # 자리 바꾸기
        v1 = lst[idx1]
        v2 = lst[idx2]

        lst[idx1] = v2
        lst[idx2] = v1

        # lst 값(딕셔너리의 key)의 인덱스를 value(hashset)에 add
        d[v1].add(idx2)
        d[v2].add(idx1)

for k, v in d.items():
    # print(f'key: {k}')
    print(len(v))
    # print(v)