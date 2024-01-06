k, n = tuple(map(int, input().split(' '))) # n: 자리수


res = []

def print_res():
    print(*res)

def permutation(lev):
    if lev == n:
        print_res()
        return
    
    for cur_k in range(1, k+1):
        res.append(cur_k)
        permutation(lev+1)
        res.pop()



permutation(0)