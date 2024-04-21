n, k = tuple(map(int, input().split(' ')))

"""
d = {
    key: 1 ~ n
    val: set(방문한 인덱스)
}
"""

moves = [
    tuple(map(int, input().split(' ')))
    for _ in range(k)
]

lst = [
    i for i in range(n+1)
]

d = dict()

for i in range(1, n+1):
    d[i] = set([i])


for _ in range(k):
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
    print(len(v))