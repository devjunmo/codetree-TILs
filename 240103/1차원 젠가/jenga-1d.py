import sys

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

# print(arr)

s1, e1 = list(map(int, input().split(' ')))
s2, e2 = list(map(int, input().split(' ')))

# print(s2, e2)

def del_block(arr, s, e):
    res_lst = []

    # arr를 앞에서 부터 순회하는데 현재 인덱스가 s<= i <= e라면 continue
    for i in range(len(arr)):
        idx = i+1
        if s <= idx <= e:
            continue
        res_lst.append(arr[i])

    return res_lst


arr = del_block(arr, s1, e1)
arr = del_block(arr, s2, e2)

print(len(arr))
for i in range(len(arr)):
    print(arr[i])