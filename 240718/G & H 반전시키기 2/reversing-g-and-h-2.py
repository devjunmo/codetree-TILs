n = int(input())
src = list(input().strip())
tgt = list(input().strip())

# 4번째를 변화시키려면 4번째를 눌러야함 -> 따라서 다르다면 반드시 변화시켜야 함 
# 3번째는 4번째, 3번째 -> 이긴 한데,, 앞에꺼는 이미 고려되었으므로 신경안써도 됨;;

def flip(c):
    if c == 'G':
        return 'H'
    else:
        return 'G'

cnt = 0

for i in range(n-1, -1, -1):
    if src[i] != tgt[i]:
        # 다르면 첨부터 싹 뒤집는다 
        cnt+=1
        for j in range(0, i+1):
            cur_c = src[j]
            nxt_c = flip(cur_c)
            src[j] = nxt_c
    else:
        pass

print(cnt)